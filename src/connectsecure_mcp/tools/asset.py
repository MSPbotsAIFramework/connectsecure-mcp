import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import ConnectSecureClient, ConnectSecureError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], ConnectSecureClient | None]) -> None:

    @mcp.tool()
    async def connectsecure_get_asset_application_count(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/application_count

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
            result = await client.get("/r/report_queries/application_count", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_application_vulnerabilities_patching_asset_details(id: int, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/application_vulnerabilities_patching_asset_details

        Args:
            id: Required. ID.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"id": id, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/application_vulnerabilities_patching_asset_details", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_application_vulnerabilities_v2(software_type: str, agent_type: str, platform: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/application_vulnerabilities_v2

        Args:
            software_type: Required. Software Type.
            agent_type: Required. Agent Type.
            platform: Required. Platform.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"software_type": software_type, "agent_type": agent_type, "platform": platform, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/application_vulnerabilities_v2", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_asset_critical_vulnerabilities(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/asset_critical_vulnerabilities

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
            result = await client.get("/r/report_queries/asset_critical_vulnerabilities", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_asset_firewall_rules(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve asset firewall rules.

        API: GET /report_queries/asset_firewall_rules

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
            result = await client.get("/report_queries/asset_firewall_rules", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_asset_iptables_rules(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve asset iptables rules.

        API: GET /report_queries/asset_iptables_rules

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
            result = await client.get("/report_queries/asset_iptables_rules", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_asset_open_ports(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve asset open ports.

        API: GET /report_queries/asset_open_ports

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
            result = await client.get("/report_queries/asset_open_ports", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_asset_patches_info(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve asset patches info.

        API: GET /report_queries/asset_patches_info

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
            result = await client.get("/report_queries/asset_patches_info", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_asset_ports_view(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/asset_ports_view

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
            result = await client.get("/r/report_queries/asset_ports_view", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_asset_processes_running(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve asset processes running.

        API: GET /report_queries/asset_processes_running

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
            result = await client.get("/report_queries/asset_processes_running", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_asset_registry_misconfiguration(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve asset registry misconfiguration.

        API: GET /report_queries/asset_registry_misconfiguration

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
            result = await client.get("/report_queries/asset_registry_misconfiguration", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_asset_security_report_data(asset_id: int, company_id: int, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/asset_security_report_data

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
            result = await client.get("/r/report_queries/asset_security_report_data", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_asset_services(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve asset services.

        API: GET /report_queries/asset_services

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
            result = await client.get("/report_queries/asset_services", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_asset_software(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/asset_software

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
            result = await client.get("/r/report_queries/asset_software", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_asset_stats(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve asset stats.

        API: GET /r/report_queries/asset_stats

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
            result = await client.get("/r/report_queries/asset_stats", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_asset_users(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve asset users.

        API: GET /report_queries/asset_users

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
            result = await client.get("/report_queries/asset_users", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_asset_view(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve asset view.

        API: GET /r/asset/asset_view

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
            result = await client.get("/r/asset/asset_view", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_asset_view_by_id(id: int) -> str:
        """Retrieve asset view.

        API: GET /r/asset/asset_view/{id}

        Args:
            id: Required. id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/r/asset/asset_view/{id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_asset_wise_vulnerabilities(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/asset_wise_vulnerabilities

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
            result = await client.get("/r/report_queries/asset_wise_vulnerabilities", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_assets(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve assets.

        API: GET /r/report_queries/assets

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
            result = await client.get("/r/report_queries/assets", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_assets_by_application(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/assets_by_application

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
            result = await client.get("/r/report_queries/assets_by_application", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_assets_by_application_suppressed(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/assets_by_application_suppressed

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
            result = await client.get("/r/report_queries/assets_by_application_suppressed", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_cert_info_view(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/cert_info_view

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
            result = await client.get("/r/report_queries/cert_info_view", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_companies_by_application(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/companies_by_application

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
            result = await client.get("/r/report_queries/companies_by_application", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_companies_by_application_suppressed(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/companies_by_application_suppressed

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
            result = await client.get("/r/report_queries/companies_by_application_suppressed", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_companies_by_problem_group(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/companies_by_problem_group

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
            result = await client.get("/r/report_queries/companies_by_problem_group", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_companies_by_problem_group_suppressed(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/companies_by_problem_group_suppressed

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
            result = await client.get("/r/report_queries/companies_by_problem_group_suppressed", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_compliance_count(compliance_type: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/compliance_count

        Args:
            compliance_type: Required. Compliance Type.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"compliance_type": compliance_type, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/compliance_count", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_cron_jobs(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve cron jobs.

        API: GET /report_queries/cron_jobs

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
            result = await client.get("/report_queries/cron_jobs", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_distinct_agents_name(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/distinct_agents_name

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
            result = await client.get("/r/report_queries/distinct_agents_name", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_distinct_asset_ip(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/distinct_asset_ip

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
            result = await client.get("/r/report_queries/distinct_asset_ip", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_distinct_asset_name(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/distinct_asset_name

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
            result = await client.get("/r/report_queries/distinct_asset_name", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_distinct_discovered_protocols(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/distinct_discovered_protocols

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
            result = await client.get("/r/report_queries/distinct_discovered_protocols", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_distinct_os(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/distinct_os

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
            result = await client.get("/r/report_queries/distinct_os", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_distinct_platform(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/distinct_platform

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
            result = await client.get("/r/report_queries/distinct_platform", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_distinct_software(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/distinct_software

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
            result = await client.get("/r/report_queries/distinct_software", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_distinct_tags(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/distinct_tags

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
            result = await client.get("/r/report_queries/distinct_tags", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_external_asset_externalscan(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/external_asset_externalscan

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
            result = await client.get("/r/report_queries/external_asset_externalscan", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_external_asset_ports_data(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/external_asset_ports_data

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
            result = await client.get("/r/report_queries/external_asset_ports_data", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_external_asset_ssl_attack(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/external_asset_ssl_attack

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
            result = await client.get("/r/report_queries/external_asset_ssl_attack", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_external_asset_ssl_ciphers(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/external_asset_ssl_ciphers

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
            result = await client.get("/r/report_queries/external_asset_ssl_ciphers", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_external_asset_vulnerabilities(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/external_asset_vulnerabilities

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
            result = await client.get("/r/report_queries/external_asset_vulnerabilities", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_get_asset_remediation_plan(having: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/asset/get_asset_remediation_plan

        Args:
            having: Required. Online Filter.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"having": having, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/asset/get_asset_remediation_plan", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_get_assets_by_problem(problem_name: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/get_assets_by_problem

        Args:
            problem_name: Required. Problem Name.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"problem_name": problem_name, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/get_assets_by_problem", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_get_assets_problem(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/get_assets_problem

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
            result = await client.get("/r/report_queries/get_assets_problem", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_get_patch_settings(company_id: str) -> str:
        """Retrieve records.

        API: GET /r/company/get_patch_settings

        Args:
            company_id: Required. Company Id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"company_id": company_id}
        try:
            result = await client.get("/r/company/get_patch_settings", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_get_remediate_records(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/get_remediate_records

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
            result = await client.get("/r/report_queries/get_remediate_records", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_get_remediation(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/get_remediation

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
            result = await client.get("/r/report_queries/get_remediation", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_kernel_modules(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve kernel modules.

        API: GET /report_queries/kernel_modules

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
            result = await client.get("/report_queries/kernel_modules", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_lightweight_assets(company_id: int, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/lightweight_assets

        Args:
            company_id: Required. Company id.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"company_id": company_id, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/lightweight_assets", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_notification_tickets_view(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/notification_tickets_view

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
            result = await client.get("/r/report_queries/notification_tickets_view", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_notification_tickets_view_report_queries(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve notification tickets view.

        API: GET /report_queries/notification_tickets_view

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
            result = await client.get("/report_queries/notification_tickets_view", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_os_pending_patches(num_days: int, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/os_pending_patches

        Args:
            num_days: Required. Number of days.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"num_days": num_days, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/os_pending_patches", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_os_pending_patches_companies(os_name: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/os_pending_patches_companies

        Args:
            os_name: Required. OS Name.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"os_name": os_name, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/os_pending_patches_companies", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_ports_assets_details(service_name: str, company_id: int, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/ports_assets_details

        Args:
            service_name: Required. Service Name.
            company_id: Required. Company id.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"service_name": service_name, "company_id": company_id, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/ports_assets_details", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_ports_count(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/ports_count

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
            result = await client.get("/r/report_queries/ports_count", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_ports_view(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/ports_view

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
            result = await client.get("/r/report_queries/ports_view", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_problem_group_summary(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/problem_group_summary

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
            result = await client.get("/r/report_queries/problem_group_summary", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_problem_group_summary_asset_company_count(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/problem_group_summary_asset_company_count

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
            result = await client.get("/r/report_queries/problem_group_summary_asset_company_count", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_problems_info(problem_name: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/problems_info

        Args:
            problem_name: Required. Online Filter.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"problem_name": problem_name, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/problems_info", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_problems_remediations_summary(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/problems_remediations_summary

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
            result = await client.get("/r/report_queries/problems_remediations_summary", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_problems_ssl_for_asset(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/problems_ssl_for_asset

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
            result = await client.get("/r/report_queries/problems_ssl_for_asset", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_problems_summary(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/problems_summary

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
            result = await client.get("/r/report_queries/problems_summary", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_problems_summary_asset_details(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/problems_summary_asset_details

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
            result = await client.get("/r/report_queries/problems_summary_asset_details", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_problems_summary_global(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/problems_summary_global

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
            result = await client.get("/r/report_queries/problems_summary_global", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_problems_summary_group_by_companies(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/problems_summary_group_by_companies

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
            result = await client.get("/r/report_queries/problems_summary_group_by_companies", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_problems_summary_tag(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/problems_summary_tag

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
            result = await client.get("/r/report_queries/problems_summary_tag", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_registry_problems_company(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/registry_problems_company

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
            result = await client.get("/r/report_queries/registry_problems_company", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_registry_problems_remediation(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/registry_problems_remediation

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
            result = await client.get("/r/report_queries/registry_problems_remediation", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_registry_problems_remediation_asset_details(asset_id: int, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/registry_problems_remediation_asset_details

        Args:
            asset_id: Required. ID.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"asset_id": asset_id, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/registry_problems_remediation_asset_details", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_registry_problems_summary(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/registry_problems_summary

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
            result = await client.get("/r/report_queries/registry_problems_summary", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_remediate_records(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/remediate_records

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
            result = await client.get("/r/report_queries/remediate_records", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_remediate_records_asset(asset_id: int) -> str:
        """Retrieve records.

        API: GET /r/get_data/remediate_records_asset

        Args:
            asset_id: Required. Asset id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"asset_id": asset_id}
        try:
            result = await client.get("/r/get_data/remediate_records_asset", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_remediate_records_assets(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/remediate_records_assets

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
            result = await client.get("/r/report_queries/remediate_records_assets", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_remediate_records_companies(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/remediate_records_companies

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
            result = await client.get("/r/report_queries/remediate_records_companies", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_remediate_records_companies_get_data(company_id: int) -> str:
        """Retrieve records.

        API: GET /r/get_data/remediate_records_companies

        Args:
            company_id: Required. Company id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"company_id": company_id}
        try:
            result = await client.get("/r/get_data/remediate_records_companies", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_remediate_records_days(having: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/remediate_records_days

        Args:
            having: Required. No of Days.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"having": having, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/remediate_records_days", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_remediate_records_global() -> str:
        """Retrieve records.

        API: GET /r/get_data/remediate_records_global

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/r/get_data/remediate_records_global", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_remediated_registry_solution_plan(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/remediated_registry_solution_plan

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
            result = await client.get("/r/report_queries/remediated_registry_solution_plan", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_remediation_companies(software_name: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/remediation_companies

        Args:
            software_name: Required. Software Name.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"software_name": software_name, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/remediation_companies", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_remediation_plan_asset(asset_id: int) -> str:
        """Retrieve records.

        API: GET /r/get_data/remediation_plan_asset

        Args:
            asset_id: Required. Asset id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"asset_id": asset_id}
        try:
            result = await client.get("/r/get_data/remediation_plan_asset", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_remediation_plan_asset_details(having: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/remediation_plan_asset_details

        Args:
            having: Required. Online Filter.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"having": having, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/remediation_plan_asset_details", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_remediation_plan_asset_details_by_epss(having: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/remediation_plan_asset_details_by_epss

        Args:
            having: Required. Online Filter.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"having": having, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/remediation_plan_asset_details_by_epss", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_remediation_plan_asset_epss_details(having: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/remediation_plan_asset_epss_details

        Args:
            having: Required. Online Filter.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"having": having, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/remediation_plan_asset_epss_details", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_remediation_plan_by_company(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/remediation_plan_by_company

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
            result = await client.get("/r/report_queries/remediation_plan_by_company", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_remediation_plan_companies(company_id: int) -> str:
        """Retrieve records.

        API: GET /r/get_data/remediation_plan_companies

        Args:
            company_id: Required. Company id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"company_id": company_id}
        try:
            result = await client.get("/r/get_data/remediation_plan_companies", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_remediation_plan_global() -> str:
        """Retrieve records.

        API: GET /r/get_data/remediation_plan_global

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/r/get_data/remediation_plan_global", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_remediation_plan_include_company(having: str, company_id: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/remediation_plan_include_company

        Args:
            having: Required. Online Filter.
            company_id: Required. Company ID.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"having": having, "company_id": company_id, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/remediation_plan_include_company", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_remediation_plan_include_company_days(having: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/remediation_plan_include_company_days

        Args:
            having: Required. No of Days.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"having": having, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/remediation_plan_include_company_days", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_remediation_velocity_application(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/remediation_velocity_application

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
            result = await client.get("/r/report_queries/remediation_velocity_application", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_remediation_velocity_application_asset_details(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/remediation_velocity_application_asset_details

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
            result = await client.get("/r/report_queries/remediation_velocity_application_asset_details", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_remediation_velocity_company(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/remediation_velocity_company

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
            result = await client.get("/r/report_queries/remediation_velocity_company", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_resolved_remediation(company_id: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/resolved_remediation

        Args:
            company_id: Required. Company ID.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"company_id": company_id, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/resolved_remediation", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_risk_score(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/risk_score

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
            result = await client.get("/r/report_queries/risk_score", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_selinux_settings(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve selinux settings.

        API: GET /report_queries/selinux_settings

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
            result = await client.get("/report_queries/selinux_settings", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_suid_permissions(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve suid permissions.

        API: GET /report_queries/suid_permissions

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
            result = await client.get("/report_queries/suid_permissions", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_suppressed_problems(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/suppressed_problems

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
            result = await client.get("/r/report_queries/suppressed_problems", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_sw_problems_remediations_view(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/sw_problems_remediations_view

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
            result = await client.get("/r/report_queries/sw_problems_remediations_view", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_sw_problems_remediations_view_assetwise(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/sw_problems_remediations_view_assetwise

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
            result = await client.get("/r/report_queries/sw_problems_remediations_view_assetwise", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_sw_problems_remediations_view_vul(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/sw_problems_remediations_view_vul

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
            result = await client.get("/r/report_queries/sw_problems_remediations_view_vul", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_system_events_view(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve system events view.

        API: GET /report_queries/system_events_view

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
            result = await client.get("/report_queries/system_events_view", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_system_events_view_ticketid(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve system events view.

        API: GET /report_queries/system_events_view_ticketid

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
            result = await client.get("/report_queries/system_events_view_ticketid", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_tags_view(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/tags_view

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
            result = await client.get("/r/report_queries/tags_view", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_total_asset_count(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/total_asset_count

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
            result = await client.get("/r/report_queries/total_asset_count", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_ufw_firewall_rules(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve ufw firewall rules.

        API: GET /report_queries/ufw_firewall_rules

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
            result = await client.get("/report_queries/ufw_firewall_rules", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_unconfirmed_key_check(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/unconfirmed_key_check

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
            result = await client.get("/r/report_queries/unconfirmed_key_check", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_unconfirmed_open_ports_key_check(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/unconfirmed_open_ports_key_check

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
            result = await client.get("/r/report_queries/unconfirmed_open_ports_key_check", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_vulnerabilities_count(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/vulnerabilities_count

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
            result = await client.get("/r/report_queries/vulnerabilities_count", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_vulnerabilities_details(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/vulnerabilities_details

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
            result = await client.get("/r/report_queries/vulnerabilities_details", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_asset_vulnerabilities_details_suppressed(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve records.

        API: GET /r/report_queries/vulnerabilities_details_suppressed

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
            result = await client.get("/r/report_queries/vulnerabilities_details_suppressed", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"
