import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import ConnectSecureClient, ConnectSecureError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], ConnectSecureClient | None]) -> None:

    @mcp.tool()
    async def connectsecure_get_active_directory_ad_basic_info(company_id: int, source: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve ad basic info.

        API: GET /report_queries/ad_basic_info

        Args:
            company_id: Required. Company id.
            source: Required. Source.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"company_id": company_id, "source": source, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/report_queries/ad_basic_info", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_active_directory_ad_computers_view(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve ad computers view.

        API: GET /report_queries/ad_computers_view

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
            result = await client.get("/report_queries/ad_computers_view", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_active_directory_ad_domain_details(company_id: int, source: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve ad domain details.

        API: GET /report_queries/ad_domain_details

        Args:
            company_id: Required. Company id.
            source: Required. Source.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"company_id": company_id, "source": source, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/report_queries/ad_domain_details", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_active_directory_ad_gpos_details(company_id: int, domains_id: str, source: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve ad gpos details.

        API: GET /report_queries/ad_gpos_details

        Args:
            company_id: Required. Company id.
            domains_id: Required. Domains id.
            source: Required. Source.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"company_id": company_id, "domains_id": domains_id, "source": source, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/report_queries/ad_gpos_details", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_active_directory_ad_gpos_view(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve ad gpos view.

        API: GET /report_queries/ad_gpos_view

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
            result = await client.get("/report_queries/ad_gpos_view", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_active_directory_ad_group_computers(company_id: int, object_guid: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve ad group computers.

        API: GET /report_queries/ad_group_computers

        Args:
            company_id: Required. Company id.
            object_guid: Required. Object Guid.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"company_id": company_id, "object_guid": object_guid, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/report_queries/ad_group_computers", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_active_directory_ad_group_users(company_id: int, object_guid: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve ad group users.

        API: GET /report_queries/ad_group_users

        Args:
            company_id: Required. Company id.
            object_guid: Required. Object Guid.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"company_id": company_id, "object_guid": object_guid, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/report_queries/ad_group_users", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_active_directory_ad_groups_view(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve ad groups view.

        API: GET /report_queries/ad_groups_view

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
            result = await client.get("/report_queries/ad_groups_view", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_active_directory_ad_ous_view(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve ad ous view.

        API: GET /report_queries/ad_ous_view

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
            result = await client.get("/report_queries/ad_ous_view", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_active_directory_ad_password_policies(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve ad password policies.

        API: GET /report_queries/ad_password_policies

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
            result = await client.get("/report_queries/ad_password_policies", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_active_directory_ad_roles(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve ad roles.

        API: GET /report_queries/ad_roles

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
            result = await client.get("/report_queries/ad_roles", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_active_directory_ad_roles_details(company_id: int, object_guid: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve ad roles details.

        API: GET /report_queries/ad_roles_details

        Args:
            company_id: Required. Company id.
            object_guid: Required. Object Guid.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"company_id": company_id, "object_guid": object_guid, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/report_queries/ad_roles_details", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_active_directory_ad_roles_member(company_id: int, object_guid: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve ad roles member.

        API: GET /report_queries/ad_roles_member

        Args:
            company_id: Required. Company id.
            object_guid: Required. Object Guid.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"company_id": company_id, "object_guid": object_guid, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/report_queries/ad_roles_member", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_active_directory_ad_user_licenses(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve ad user licenses.

        API: GET /report_queries/ad_user_licenses

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
            result = await client.get("/report_queries/ad_user_licenses", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_active_directory_ad_users_view(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve ad users view.

        API: GET /report_queries/ad_users_view

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
            result = await client.get("/report_queries/ad_users_view", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_active_directory_azure_ad_logs(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve azure ad logs.

        API: GET /report_queries/azure_ad_logs

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
            result = await client.get("/report_queries/azure_ad_logs", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_active_directory_azure_licenses(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve azure licenses.

        API: GET /report_queries/azure_licenses

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
            result = await client.get("/report_queries/azure_licenses", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_active_directory_azure_secure_score(condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve azure secure score.

        API: GET /report_queries/azure_secure_score

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
            result = await client.get("/report_queries/azure_secure_score", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_active_directory_get_computer_details(company_id: int, object_guid: str, source: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve get computer details.

        API: GET /report_queries/get_computer_details

        Args:
            company_id: Required. Company id.
            object_guid: Required. Object Guid.
            source: Required. Source.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"company_id": company_id, "object_guid": object_guid, "source": source, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/report_queries/get_computer_details", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_active_directory_get_groups_details(company_id: int, object_guid: str, source: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve get groups details.

        API: GET /report_queries/get_groups_details

        Args:
            company_id: Required. Company id.
            object_guid: Required. Object Guid.
            source: Required. Source.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"company_id": company_id, "object_guid": object_guid, "source": source, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/report_queries/get_groups_details", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_active_directory_get_ous_details(company_id: int, object_guid: str, source: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve get ous details.

        API: GET /report_queries/get_ous_details

        Args:
            company_id: Required. Company id.
            object_guid: Required. Object Guid.
            source: Required. Source.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"company_id": company_id, "object_guid": object_guid, "source": source, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/report_queries/get_ous_details", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def connectsecure_get_active_directory_get_user_details(company_id: int, object_guid: str, source: str, condition: str | None = None, skip: int | None = None, limit: int | None = None, order_by: str | None = None) -> str:
        """Retrieve get user details.

        API: GET /report_queries/get_user_details

        Args:
            company_id: Required. Company id.
            object_guid: Required. Object Guid.
            source: Required. Source.
            condition: Optional. Query Condition.
            skip: Optional. Skip No of Records.
            limit: Optional. Limit.
            order_by: Optional. Order By.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"company_id": company_id, "object_guid": object_guid, "source": source, "condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/report_queries/get_user_details", params=params)
            return json.dumps(result, indent=2)
        except ConnectSecureError as e:
            return f"Error: {e}"
