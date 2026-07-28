import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import ConnectSecureClient, ConnectSecureError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], ConnectSecureClient | None]) -> None:

    @mcp.tool()
    async def connectsecure_get_backup_software_backup_software(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve backup software.

        API: GET /r/company/backup_software

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
            result = await client.get("/r/company/backup_software", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_backup_software_backup_software_by_id(id: int) -> str:
        """Retrieve backup software.

        API: GET /r/company/backup_software/{id}

        Args:
            id: Required. id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/r/company/backup_software/{id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"
