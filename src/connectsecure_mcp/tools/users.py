from collections.abc import Callable

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

from .._json import dump_json_capped
from ..api_client import ConnectSecureClient, ConnectSecureError
from ._common import NO_TOKEN, ConditionParam, LimitParam, OrderByParam, SkipParam

_MAX_LIMIT = 200


def register(mcp: FastMCP, client_factory: Callable[[], ConnectSecureClient | None]) -> None:

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def connectsecure_get_users_get_users(
        condition: ConditionParam = None,
        skip: SkipParam = None,
        limit: LimitParam = None,
        order_by: OrderByParam = None,
    ) -> str:
        """ConnectSecure platform user accounts (portal/API users), not a company's own AD users.

        Distinct from ad_users_view, which covers a client company's Active
        Directory accounts rather than ConnectSecure platform logins.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        if limit is not None:
            limit = min(limit, _MAX_LIMIT)
        params = {"condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/user/get_users", params=params)
            return dump_json_capped(result)
        except ConnectSecureError as e:
            return e.to_envelope()
