from collections.abc import Callable
from typing import Annotated

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from .._json import dump_json_capped
from ..api_client import ConnectSecureClient, ConnectSecureError
from ._common import NO_TOKEN, ConditionParam, LimitParam, OrderByParam, SkipParam

_MAX_LIMIT = 200

CompanyIdParam = Annotated[
    int,
    Field(description="ConnectSecure company id to scope the report to, obtained from connectsecure_get_company_companies."),
]
# No accepted-value enumeration for `source` exists anywhere in this codebase,
# its tests, or its README. The description below is an inference — flagged
# as such — from this tool category also containing a dedicated
# azure_secure_score report, which implies "source" distinguishes which
# directory backend (on-prem AD vs Azure AD/Entra) the report reads from.
SourceParam = Annotated[
    str,
    Field(
        description=(
            "Directory source to scope the report to. Likely distinguishes on-premises Active "
            "Directory from Azure AD/Entra (this category has a separate azure_secure_score "
            "report for Azure-specific posture), but the exact accepted values are not documented "
            "anywhere in this codebase — confirm against ConnectSecure's own API reference."
        )
    ),
]


def register(mcp: FastMCP, client_factory: Callable[[], ConnectSecureClient | None]) -> None:
    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def connectsecure_get_active_directory_ad_basic_info(
        company_id: CompanyIdParam,
        source: SourceParam,
        condition: ConditionParam = None,
        skip: SkipParam = None,
        limit: LimitParam = None,
        order_by: OrderByParam = None,
    ) -> str:
        """High-level Active Directory summary for one company: domain identity and AD health counters.

        Summary-level only; see ad_domain_details for the full domain
        configuration and ad_users_view/ad_groups_view for per-object detail.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        if limit is not None:
            limit = min(limit, _MAX_LIMIT)
        params = {"company_id": company_id, "source": source, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/report_queries/ad_basic_info", params=params)
            return dump_json_capped(result)
        except ConnectSecureError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def connectsecure_get_active_directory_ad_domain_details(
        company_id: CompanyIdParam,
        source: SourceParam,
        condition: ConditionParam = None,
        skip: SkipParam = None,
        limit: LimitParam = None,
        order_by: OrderByParam = None,
    ) -> str:
        """Detailed Active Directory domain configuration for one company (domain/forest settings).

        More granular than ad_basic_info's summary counters.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        if limit is not None:
            limit = min(limit, _MAX_LIMIT)
        params = {"company_id": company_id, "source": source, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/report_queries/ad_domain_details", params=params)
            return dump_json_capped(result)
        except ConnectSecureError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def connectsecure_get_active_directory_ad_groups_view(
        condition: ConditionParam = None,
        skip: SkipParam = None,
        limit: LimitParam = None,
        order_by: OrderByParam = None,
    ) -> str:
        """Active Directory group inventory: group names, types, and membership rollups.

        Group-level view; see ad_users_view for individual AD user accounts
        instead.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        if limit is not None:
            limit = min(limit, _MAX_LIMIT)
        params = {"condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/report_queries/ad_groups_view", params=params)
            return dump_json_capped(result)
        except ConnectSecureError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def connectsecure_get_active_directory_ad_password_policies(
        condition: ConditionParam = None,
        skip: SkipParam = None,
        limit: LimitParam = None,
        order_by: OrderByParam = None,
    ) -> str:
        """Active Directory password/account-lockout policy settings (complexity, min length, lockout).

        Configuration/compliance data, not individual user account status —
        see ad_users_view for that.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        if limit is not None:
            limit = min(limit, _MAX_LIMIT)
        params = {"condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/report_queries/ad_password_policies", params=params)
            return dump_json_capped(result)
        except ConnectSecureError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def connectsecure_get_active_directory_ad_users_view(
        condition: ConditionParam = None,
        skip: SkipParam = None,
        limit: LimitParam = None,
        order_by: OrderByParam = None,
    ) -> str:
        """Active Directory user account inventory: usernames, enabled/disabled status, attributes.

        A client company's own AD accounts, not ConnectSecure's platform
        logins — see connectsecure_get_users_get_users for those. Per-user
        view; see ad_groups_view for group membership instead.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        if limit is not None:
            limit = min(limit, _MAX_LIMIT)
        params = {"condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/report_queries/ad_users_view", params=params)
            return dump_json_capped(result)
        except ConnectSecureError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def connectsecure_get_active_directory_azure_secure_score(
        condition: ConditionParam = None,
        skip: SkipParam = None,
        limit: LimitParam = None,
        order_by: OrderByParam = None,
    ) -> str:
        """Microsoft Secure Score for a company's Azure AD / Microsoft 365 tenant.

        Azure/Entra-specific aggregate security posture rating, distinct from
        the on-prem AD reports above (ad_basic_info, ad_domain_details, etc.).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        if limit is not None:
            limit = min(limit, _MAX_LIMIT)
        params = {"condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/report_queries/azure_secure_score", params=params)
            return dump_json_capped(result)
        except ConnectSecureError as e:
            return e.to_envelope()
