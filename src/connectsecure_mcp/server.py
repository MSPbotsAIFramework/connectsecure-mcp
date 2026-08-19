import contextvars
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.types import ASGIApp, Receive, Scope, Send

from .api_client import ConnectSecureClient
from .config import Settings

# Per-request credential isolation via contextvars.
# GatewayTokenMiddleware sets this before the MCP handler runs.
# Python asyncio copies context per task, so concurrent SSE connections are isolated.
# Value is (access_token, user_id, base_url) — all three required, since
# ConnectSecure has no single default host (each tenant is provisioned on its
# own pod) and auth needs both the JWT and the user id returned alongside it.
_gateway_creds_var: contextvars.ContextVar[tuple[str, str, str] | None] = contextvars.ContextVar(
    "connectsecure_gateway_creds", default=None
)


def get_client_from_context(settings: Settings) -> ConnectSecureClient | None:
    """Resolve the active ConnectSecureClient for the current request context."""
    creds = _gateway_creds_var.get()
    if not creds:
        return None
    token, user_id, base_url = creds
    return ConnectSecureClient(token, user_id, base_url)


class GatewayTokenMiddleware:
    """ASGI middleware.

    Reads X-ConnectSecure-Access-Token, X-ConnectSecure-User-Id, and
    X-ConnectSecure-Base-Url (all required) from request headers and stores
    them in the contextvar. Returns 401 if any is missing on /mcp requests.
    """

    def __init__(self, app: ASGIApp, settings: Settings):
        self.app = app
        self.settings = settings

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        path = scope.get("path", "")
        if not path.startswith("/mcp"):
            await self.app(scope, receive, send)
            return

        request = Request(scope)
        token = request.headers.get("x-connectsecure-access-token")
        user_id = request.headers.get("x-connectsecure-user-id")
        base_url = request.headers.get("x-connectsecure-base-url")
        if not token or not user_id or not base_url:
            response = JSONResponse(
                {
                    "error": "Missing credentials",
                    "message": (
                        "This server requires the X-ConnectSecure-Access-Token, "
                        "X-ConnectSecure-User-Id, and X-ConnectSecure-Base-Url headers"
                    ),
                    "required_headers": [
                        "X-ConnectSecure-Access-Token",
                        "X-ConnectSecure-User-Id",
                        "X-ConnectSecure-Base-Url",
                    ],
                    "optional_headers": [],
                },
                status_code=401,
            )
            await response(scope, receive, send)
            return

        ctx_token = _gateway_creds_var.set((token, user_id, base_url))
        try:
            await self.app(scope, receive, send)
        finally:
            _gateway_creds_var.reset(ctx_token)


def create_mcp_server(settings: Settings) -> FastMCP:
    """Build the FastMCP server instance and register all ConnectSecure tools."""
    # DNS-rebinding protection is a browser-oriented safeguard that rejects
    # non-localhost Host headers with 421. Disable it so the server works
    # correctly behind a reverse proxy or docker network.
    mcp = FastMCP(
        name="connectsecure-mcp",
        instructions=(
            "ConnectSecure is a vulnerability management and IT security "
            "compliance platform MSPs use to assess client networks — "
            "vulnerability scanning, Active Directory security posture, and "
            "per-client asset/risk visibility. All 19 tools are read-only "
            "queries; there are no write/delete tools in this service. Tool "
            "categories: company (connectsecure_get_company_companies to list "
            "clients and get a company_id, company_stats for summary counts); "
            "asset (vulnerabilities_details, asset_critical_vulnerabilities, "
            "external_asset_vulnerabilities, remediate_records, risk_score for "
            "vulnerability/remediation questions; assets, asset_view, "
            "asset_stats, sw_problems_remediations_view for inventory); "
            "active_directory (ad_users_view, ad_basic_info, ad_domain_details, "
            "ad_groups_view, ad_password_policies, azure_secure_score for AD/"
            "Azure AD security posture); users (get_users for platform user "
            "accounts). Typical flow: call connectsecure_get_company_companies "
            "first to resolve a company_id, then pass it (or filter via the "
            "condition param) into the asset/active_directory report tools. "
            "Most list tools take optional condition/skip/limit/order_by "
            "params for filtering and pagination."
        ),
        transport_security=TransportSecuritySettings(enable_dns_rebinding_protection=False),
    )

    client_factory: Callable[[], ConnectSecureClient | None] = lambda: get_client_from_context(
        settings
    )

    from .tools import (
        active_directory,
        asset,
        company,
        users,
    )

    active_directory.register(mcp, client_factory)
    asset.register(mcp, client_factory)
    company.register(mcp, client_factory)
    users.register(mcp, client_factory)

    return mcp
