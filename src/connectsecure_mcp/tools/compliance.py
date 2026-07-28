import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import ConnectSecureClient, ConnectSecureError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], ConnectSecureClient | None]) -> None:

    @mcp.tool()
    async def connectsecure_get_compliance_asset_compliance_details(asset_id: int, platform: str, compliance_type: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/asset_compliance_details

        Args:
            asset_id: Required. Asset id.
            platform: Required. Platform.
            compliance_type: Required. Compliance Type.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"asset_id": asset_id, "platform": platform, "compliance_type": compliance_type, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/asset_compliance_details", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_compliance_asset_compliance_report_data(asset_id: int, company_id: int, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/asset_compliance_report_data

        Args:
            asset_id: Required. Asset id.
            company_id: Required. Company id.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"asset_id": asset_id, "company_id": company_id, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/asset_compliance_report_data", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_compliance_compliance_asset_info(compliance_status: str, platform: str, check_id: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/compliance_asset_info

        Args:
            compliance_status: Required. Compliance status.
            platform: Required. Platform type.
            check_id: Required. Check identifier.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"compliance_status": compliance_status, "platform": platform, "check_id": check_id, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/compliance_asset_info", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_compliance_compliance_check_asset_count(platform: str, section: str, compliance_type: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/compliance_check_asset_count

        Args:
            platform: Required. Platform.
            section: Required. Section.
            compliance_type: Required. Compliance Type.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"platform": platform, "section": section, "compliance_type": compliance_type, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/compliance_check_asset_count", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_compliance_compliance_check_company_count(platform: str, section: str, compliance_type: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/compliance_check_company_count

        Args:
            platform: Required. Platform.
            section: Required. Section.
            compliance_type: Required. Compliance Type.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"platform": platform, "section": section, "compliance_type": compliance_type, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/compliance_check_company_count", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_compliance_compliance_check_count(platform: str, compliance_type: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/compliance_check_count

        Args:
            platform: Required. Platform.
            compliance_type: Required. Compliance Type.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"platform": platform, "compliance_type": compliance_type, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/compliance_check_count", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_compliance_compliance_check_count_by_section(platform: str, compliance_status: str, compliance_type: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/compliance_check_count_by_section

        Args:
            platform: Required. Platform.
            compliance_status: Required. Compliance Status.
            compliance_type: Required. Compliance Type.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"platform": platform, "compliance_status": compliance_status, "compliance_type": compliance_type, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/compliance_check_count_by_section", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_compliance_compliance_internal_checks(compliance_type: str, description: str, platform: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/compliance_internal_checks

        Args:
            compliance_type: Required. Type of Compliance.
            description: Required. Description.
            platform: Required. Platform.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"compliance_type": compliance_type, "description": description, "platform": platform, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/compliance_internal_checks", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_compliance_compliance_maturity(platform: str, compliance_type: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/compliance_maturity

        Args:
            platform: Required. Platform.
            compliance_type: Required. Compliance Type.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"platform": platform, "compliance_type": compliance_type, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/compliance_maturity", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_compliance_types() -> str:
        """Retrieve Compliance Types.

        API: GET /r/compliance/types

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/r/compliance/types", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"
