"""tools/list snapshot + error-envelope mapping tests.

No network calls: tool enumeration goes through FastMCP's in-process
list_tools(), and the error-code mapping is tested directly against
ConnectSecureError, independent of any real HTTP request.
"""

import pytest

from connectsecure_mcp.api_client import ConnectSecureError
from connectsecure_mcp.config import Settings
from connectsecure_mcp.server import create_mcp_server

EXPECTED_TOOLS = {
    "connectsecure_get_active_directory_ad_basic_info": {"company_id", "source"},
    "connectsecure_get_active_directory_ad_domain_details": {"company_id", "source"},
    "connectsecure_get_active_directory_ad_groups_view": set(),
    "connectsecure_get_active_directory_ad_password_policies": set(),
    "connectsecure_get_active_directory_ad_users_view": set(),
    "connectsecure_get_active_directory_azure_secure_score": set(),
    "connectsecure_get_asset_asset_critical_vulnerabilities": set(),
    "connectsecure_get_asset_asset_stats": set(),
    "connectsecure_get_asset_asset_view": set(),
    "connectsecure_get_asset_assets": set(),
    "connectsecure_get_asset_external_asset_vulnerabilities": set(),
    "connectsecure_get_asset_remediate_records": set(),
    "connectsecure_get_asset_risk_score": set(),
    "connectsecure_get_asset_sw_problems_remediations_view": set(),
    "connectsecure_get_asset_vulnerabilities_details": set(),
    "connectsecure_get_company_companies": set(),
    "connectsecure_get_company_companies_by_id": {"id"},
    "connectsecure_get_company_company_stats": set(),
    "connectsecure_get_users_get_users": set(),
}


@pytest.mark.asyncio
async def test_tools_list_snapshot():
    mcp = create_mcp_server(Settings())
    tools = await mcp.list_tools()
    names = {t.name for t in tools}
    assert names == set(EXPECTED_TOOLS), f"unexpected tool set: {names}"

    by_name = {t.name: t for t in tools}
    for name, expected_required in EXPECTED_TOOLS.items():
        tool = by_name[name]
        required = set(tool.inputSchema.get("required", []))
        assert required == expected_required, f"{name}: required={required}"
        assert tool.annotations is not None and tool.annotations.readOnlyHint is True
        assert len(tool.description or "") <= 500, f"{name}: description too long"
        assert "API:" not in (tool.description or ""), f"{name}: leaks implementation detail"
        first_line = (tool.description or "").strip().splitlines()[0]
        assert len(first_line) <= 100, f"{name}: first line too long: {first_line!r}"


@pytest.mark.asyncio
async def test_service_instructions_present_and_bounded():
    mcp = create_mcp_server(Settings())
    assert mcp.instructions
    assert len(mcp.instructions) <= 1500


@pytest.mark.parametrize(
    "status_code,expected_code,expected_retryable",
    [
        (0, "upstream_error", True),
        (400, "invalid_argument", False),
        (401, "unauthorized", False),
        (403, "unauthorized", False),
        (404, "not_found", False),
        (422, "invalid_argument", False),
        (429, "rate_limited", True),
        (500, "upstream_error", True),
        (503, "upstream_error", True),
    ],
)
def test_error_envelope_mapping(status_code, expected_code, expected_retryable):
    import json

    err = ConnectSecureError(status_code, "boom")
    envelope = json.loads(err.to_envelope())
    assert envelope["error"]["code"] == expected_code
    assert envelope["error"]["retryable"] is expected_retryable
    assert envelope["error"]["message"] == "boom"
