from collections.abc import Callable
from typing import Annotated

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from .._json import dump_json_capped
from ..api_client import ConnectSecureClient, ConnectSecureError
from ._common import NO_TOKEN, ConditionParam, LimitParam, OrderByParam, SkipParam

_MAX_LIMIT = 200


def register(mcp: FastMCP, client_factory: Callable[[], ConnectSecureClient | None]) -> None:
    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def connectsecure_get_company_companies(
        condition: ConditionParam = None,
        skip: SkipParam = None,
        limit: LimitParam = None,
        order_by: OrderByParam = None,
    ) -> str:
        """List of client companies (tenants) configured in ConnectSecure, with each company's id.

        Call this first to resolve a company_id for the asset/active_directory
        report tools that require one.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        if limit is not None:
            limit = min(limit, _MAX_LIMIT)
        params = {"condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/company/companies", params=params)
            return dump_json_capped(result)
        except ConnectSecureError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def connectsecure_get_company_companies_by_id(
        id: Annotated[
            int,
            Field(description="ConnectSecure company id, obtained from connectsecure_get_company_companies."),
        ],
    ) -> str:
        """Single company record by its ConnectSecure company id."""
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/r/company/companies/{id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return dump_json_capped(result)
        except ConnectSecureError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def connectsecure_get_company_company_stats(
        condition: ConditionParam = None,
        skip: SkipParam = None,
        limit: LimitParam = None,
        order_by: OrderByParam = None,
    ) -> str:
        """Aggregate per-company statistics/counters, not the company list itself.

        Use connectsecure_get_company_companies for the actual company
        records.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        if limit is not None:
            limit = min(limit, _MAX_LIMIT)
        params = {"condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/company/company_stats", params=params)
            return dump_json_capped(result)
        except ConnectSecureError as e:
            return e.to_envelope()
