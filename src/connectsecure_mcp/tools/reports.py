import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import ConnectSecureClient, ConnectSecureError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], ConnectSecureClient | None]) -> None:

    @mcp.tool()
    async def connectsecure_get_reports_cover_page() -> str:
        """Report Settings.

        API: GET /report_builder/cover_page

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/report_builder/cover_page", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_reports_download_default_template() -> str:
        """Report Settings.

        API: GET /report_builder/download_default_template

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/report_builder/download_default_template", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_reports_get_report_link(job_id: str, isGlobal: bool) -> str:
        """Download report.

        API: GET /report_builder/get_report_link

        Args:
            job_id: Required. Job id.
            isGlobal: Required. Is Global report.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"job_id": job_id, "isGlobal": isGlobal}
        try:
            result = await client.get("/report_builder/get_report_link", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_reports_get_standard_report_settings(reporttype: str, isGlobal: bool) -> str:
        """Report Settings.

        API: GET /report_builder/get_standard_report_settings

        Args:
            reporttype: Required. Report Type.
            isGlobal: Required. Is Global report.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"reporttype": reporttype, "isGlobal": isGlobal}
        try:
            result = await client.get("/report_builder/get_standard_report_settings", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_reports_report_jobs_view(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve report jobs view.

        API: GET /r/company/report_jobs_view

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
            result = await client.get("/r/company/report_jobs_view", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_reports_report_jobs_view_by_id(id: int) -> str:
        """Retrieve report job view.

        API: GET /r/company/report_jobs_view/{id}

        Args:
            id: Required. id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/r/company/report_jobs_view/{id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_reports_standard_reports(isGlobal: bool, skip: int | None = None, limit: int | None = None) -> str:
        """List standard report.

        API: GET /report_builder/standard_reports

        Args:
            isGlobal: Required. Is Global report.
            skip: Optional. Skip.
            limit: Optional. Limit.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"skip": skip, "limit": limit, "isGlobal": isGlobal}
        try:
            result = await client.get("/report_builder/standard_reports", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"
