import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import ConnectSecureClient, ConnectSecureError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], ConnectSecureClient | None]) -> None:

    @mcp.tool()
    async def connectsecure_get_application_baseline_app_baseline_plan_assets(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve app baseline plan assets.

        API: GET /r/company/app_baseline_plan_assets

        Args:
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/company/app_baseline_plan_assets", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_application_baseline_app_baseline_plan_assets_by_id(id: int) -> str:
        """Retrieve app baseline plan asset.

        API: GET /r/company/app_baseline_plan_assets/{id}

        Args:
            id: Required. id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/r/company/app_baseline_plan_assets/{id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_application_baseline_app_baseline_plan_company(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve app baseline plan company.

        API: GET /r/company/app_baseline_plan_company

        Args:
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/company/app_baseline_plan_company", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_application_baseline_app_baseline_plan_company_by_id(id: int) -> str:
        """Retrieve app baseline plan company.

        API: GET /r/company/app_baseline_plan_company/{id}

        Args:
            id: Required. id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/r/company/app_baseline_plan_company/{id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_application_baseline_app_baseline_plan_global(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve app baseline plan global.

        API: GET /r/company/app_baseline_plan_global

        Args:
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/company/app_baseline_plan_global", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_application_baseline_app_baseline_plan_global_by_id(id: int) -> str:
        """Retrieve app baseline plan global.

        API: GET /r/company/app_baseline_plan_global/{id}

        Args:
            id: Required. id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/r/company/app_baseline_plan_global/{id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_application_baseline_application_baseline_rules(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve application baseline rules.

        API: GET /r/company/application_baseline_rules

        Args:
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/company/application_baseline_rules", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_application_baseline_application_baseline_rules_by_id(id: int) -> str:
        """Retrieve application baseline rule.

        API: GET /r/company/application_baseline_rules/{id}

        Args:
            id: Required. id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/r/company/application_baseline_rules/{id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"
