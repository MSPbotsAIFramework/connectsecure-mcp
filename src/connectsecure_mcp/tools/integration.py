import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import ConnectSecureClient, ConnectSecureError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], ConnectSecureClient | None]) -> None:

    @mcp.tool()
    async def connectsecure_get_integration_company_mappings(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve company mappings.

        API: GET /r/integration/company_mappings

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
            result = await client.get("/r/integration/company_mappings", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_integration_company_mappings_by_id(id: int) -> str:
        """Retrieve company mapping.

        API: GET /r/integration/company_mappings/{id}

        Args:
            id: Required. id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/r/integration/company_mappings/{id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_integration_integration_credentials(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve integration credentials.

        API: GET /r/integration/integration_credentials

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
            result = await client.get("/r/integration/integration_credentials", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_integration_integration_credentials_by_id(id: int) -> str:
        """Retrieve integration credential.

        API: GET /r/integration/integration_credentials/{id}

        Args:
            id: Required. id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/r/integration/integration_credentials/{id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_integration_integration_rules(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve integration rules.

        API: GET /r/integration/integration_rules

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
            result = await client.get("/r/integration/integration_rules", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_integration_integration_rules_by_id(id: int) -> str:
        """Retrieve integration rule.

        API: GET /r/integration/integration_rules/{id}

        Args:
            id: Required. id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/r/integration/integration_rules/{id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"
