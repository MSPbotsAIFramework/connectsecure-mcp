# connectsecure-mcp

MCP server for **ConnectSecure** — a vulnerability management / IT security
assessment platform. Exposes ConnectSecure's read-only query API (companies,
assets, vulnerabilities, Active Directory, firewall, compliance, credentials,
and more) as MCP tools.

## Overview

- Stateless HTTP service. No credentials are ever persisted — each request
  supplies its own credentials via headers, used only for the lifetime of
  that single request.
- Supports concurrent requests; per-request credential isolation is done via
  Python `contextvars`, not a global/shared client instance.
- Entry points: `POST /mcp` (MCP protocol) and `GET /health` (health check).
- Default port: `8080` (configurable via `MCP_HTTP_PORT`).

## Scope

**285 read-only (`GET`) tools**, covering every query-style endpoint in
ConnectSecure's public API (28 categories: Asset, Asset Data, Vulnerabilities,
Active Directory, Firewall, Compliance, Company, Application Baseline,
Reports, Integration, Credentials, Discovery Settings, Attack Surface, Tags,
Ad Audit, Agent, Event Set, Ticket Template, Scheduler, Backup Software, EDR,
PII, External Scan, Settings, Compliance Assessment, Jobs, Patch Management,
Users). MSPbots itself only calls 11 of these (report/company/user/asset
queries); per user decision this MCP builds all read/query operations across
the full public spec, deferring the ~78 write operations (`POST`/`PATCH`/`DELETE`)
for now — see **Known Gaps**.

## Authentication

ConnectSecure is multi-tenant: every tenant is provisioned on its own pod
hostname (e.g. `https://pod1.connectsecure.com`), and auth is a JWT access
token obtained out-of-band via:

```
POST {base_url}/w/authorize
Client-Auth-Token: base64(tenant_name + client_id : client_secret)
```

which returns `{"data": {"access_token": "...", "user_id": "..."}}`. This
server does not perform that exchange itself — like the other OAuth2-based
vendor MCPs in this program (Acronis, ConnectWise Asio, Bloom Growth), it only
receives the already-obtained access token (plus the user id and pod
hostname) via request headers, and forwards them upstream as
`Authorization: Bearer <token>` and `X-USER-ID: <user_id>` on every call.

### HEADER 授权参数说明

| Header | 类型 | 是否必填 | 默认值 | 枚举值 | 字段描述 | Example |
|---|---|---|---|---|---|---|
| `X-ConnectSecure-Access-Token` | string | 是 | 无 | 无 | `POST {base_url}/w/authorize` 返回的 JWT access_token，原样转发为上游 `Authorization: Bearer <token>` | `eyJhbGciOi...` |
| `X-ConnectSecure-User-Id` | string | 是 | 无 | 无 | 同一次 `/w/authorize` 调用返回的 `user_id`，原样转发为上游 `X-USER-ID` 请求头 | `1234` |
| `X-ConnectSecure-Base-Url` | string | 是 | 无 | 无 | 该租户的 ConnectSecure pod 主机名（每个租户独立，不固定） | `https://pod1.connectsecure.com` |

Missing any of the three headers returns `401`:
```json
{
  "error": "Missing credentials",
  "message": "This server requires the X-ConnectSecure-Access-Token, X-ConnectSecure-User-Id, and X-ConnectSecure-Base-Url headers",
  "required_headers": ["X-ConnectSecure-Access-Token", "X-ConnectSecure-User-Id", "X-ConnectSecure-Base-Url"],
  "optional_headers": []
}
```

## Environment Variables

| Variable | 类型 | 是否必填 | 默认值 | 说明 |
|---|---|---|---|---|
| `MCP_HTTP_PORT` | int | 否 | `8080` | HTTP 监听端口 |
| `MCP_HTTP_HOST` | string | 否 | `0.0.0.0` | HTTP 监听地址 |

(No `*_BASE_URL` env var — the pod hostname is per-tenant and always supplied
via the `X-ConnectSecure-Base-Url` header, never a fixed default.)

## MCP Endpoint

- `POST /mcp` — MCP protocol (streamable HTTP transport)
- `GET /health` — health check, returns `{"status": "ok", "service": "connectsecure-mcp", "transport": "http"}`

## Tool List

Every list-style tool shares the same optional pagination/filter params —
`condition` (a ConnectSecure query-condition string), `skip`, `limit`,
`order_by` — in addition to whatever's listed below. Get-by-id tools take a
single required `id` path parameter. Several report/detail tools additionally
require a `company_id` (get it from `connectsecure_get_company_companies`)
and/or an `object_guid`/`asset_id` (get it from the corresponding list tool
first).

| Category | Tool | 功能 | 参数 |
|---|---|---|---|
| Asset | `connectsecure_get_asset_application_count` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_application_vulnerabilities_patching_asset_details` | Retrieve records | id(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_application_vulnerabilities_v2` | Retrieve records | software_type(必填), agent_type(必填), platform(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_asset_critical_vulnerabilities` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_asset_firewall_rules` | Retrieve asset firewall rules | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_asset_iptables_rules` | Retrieve asset iptables rules | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_asset_open_ports` | Retrieve asset open ports | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_asset_patches_info` | Retrieve asset patches info | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_asset_ports_view` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_asset_processes_running` | Retrieve asset processes running | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_asset_registry_misconfiguration` | Retrieve asset registry misconfiguration | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_asset_security_report_data` | Retrieve records | asset_id(必填), company_id(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_asset_services` | Retrieve asset services | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_asset_software` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_asset_stats` | Retrieve asset stats | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_asset_users` | Retrieve asset users | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_asset_view` | Retrieve asset view | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_asset_view_by_id` | Retrieve asset view | id(必填) |
| Asset | `connectsecure_get_asset_asset_wise_vulnerabilities` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_assets` | Retrieve assets | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_assets_by_application` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_assets_by_application_suppressed` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_cert_info_view` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_companies_by_application` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_companies_by_application_suppressed` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_companies_by_problem_group` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_companies_by_problem_group_suppressed` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_compliance_count` | Retrieve records | compliance_type(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_cron_jobs` | Retrieve cron jobs | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_distinct_agents_name` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_distinct_asset_ip` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_distinct_asset_name` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_distinct_discovered_protocols` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_distinct_os` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_distinct_platform` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_distinct_software` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_distinct_tags` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_external_asset_externalscan` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_external_asset_ports_data` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_external_asset_ssl_attack` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_external_asset_ssl_ciphers` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_external_asset_vulnerabilities` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_get_asset_remediation_plan` | Retrieve records | having(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_get_assets_by_problem` | Retrieve records | problem_name(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_get_assets_problem` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_get_patch_settings` | Retrieve records | company_id(必填) |
| Asset | `connectsecure_get_asset_get_remediate_records` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_get_remediation` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_kernel_modules` | Retrieve kernel modules | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_lightweight_assets` | Retrieve records | company_id(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_notification_tickets_view` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_notification_tickets_view_report_queries` | Retrieve notification tickets view | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_os_pending_patches` | Retrieve records | num_days(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_os_pending_patches_companies` | Retrieve records | os_name(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_ports_assets_details` | Retrieve records | service_name(必填), company_id(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_ports_count` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_ports_view` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_problem_group_summary` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_problem_group_summary_asset_company_count` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_problems_info` | Retrieve records | problem_name(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_problems_remediations_summary` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_problems_ssl_for_asset` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_problems_summary` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_problems_summary_asset_details` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_problems_summary_global` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_problems_summary_group_by_companies` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_problems_summary_tag` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_registry_problems_company` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_registry_problems_remediation` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_registry_problems_remediation_asset_details` | Retrieve records | asset_id(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_registry_problems_summary` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_remediate_records` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_remediate_records_asset` | Retrieve records | asset_id(必填) |
| Asset | `connectsecure_get_asset_remediate_records_assets` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_remediate_records_companies` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_remediate_records_companies_get_data` | Retrieve records | company_id(必填) |
| Asset | `connectsecure_get_asset_remediate_records_days` | Retrieve records | having(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_remediate_records_global` | Retrieve records | 无 |
| Asset | `connectsecure_get_asset_remediated_registry_solution_plan` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_remediation_companies` | Retrieve records | software_name(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_remediation_plan_asset` | Retrieve records | asset_id(必填) |
| Asset | `connectsecure_get_asset_remediation_plan_asset_details` | Retrieve records | having(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_remediation_plan_asset_details_by_epss` | Retrieve records | having(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_remediation_plan_asset_epss_details` | Retrieve records | having(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_remediation_plan_by_company` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_remediation_plan_companies` | Retrieve records | company_id(必填) |
| Asset | `connectsecure_get_asset_remediation_plan_global` | Retrieve records | 无 |
| Asset | `connectsecure_get_asset_remediation_plan_include_company` | Retrieve records | having(必填), company_id(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_remediation_plan_include_company_days` | Retrieve records | having(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_remediation_velocity_application` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_remediation_velocity_application_asset_details` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_remediation_velocity_company` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_resolved_remediation` | Retrieve records | company_id(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_risk_score` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_selinux_settings` | Retrieve selinux settings | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_suid_permissions` | Retrieve suid permissions | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_suppressed_problems` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_sw_problems_remediations_view` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_sw_problems_remediations_view_assetwise` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_sw_problems_remediations_view_vul` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_system_events_view` | Retrieve system events view | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_system_events_view_ticketid` | Retrieve system events view | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_tags_view` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_total_asset_count` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_ufw_firewall_rules` | Retrieve ufw firewall rules | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_unconfirmed_key_check` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_unconfirmed_open_ports_key_check` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_vulnerabilities_count` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_vulnerabilities_details` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_vulnerabilities_details_suppressed` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset Data | `connectsecure_get_asset_data_asset_firewall_policy` | Retrieve asset firewall policy | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset Data | `connectsecure_get_asset_data_asset_firewall_policy_by_id` | Retrieve asset firewall policy | id(必填) |
| Asset Data | `connectsecure_get_asset_data_asset_installed_drivers` | Retrieve asset installed drivers | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset Data | `connectsecure_get_asset_data_asset_installed_drivers_by_id` | Retrieve asset installed driver | id(必填) |
| Asset Data | `connectsecure_get_asset_data_asset_interface` | Retrieve asset interface | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset Data | `connectsecure_get_asset_data_asset_interface_by_id` | Retrieve asset interface | id(必填) |
| Asset Data | `connectsecure_get_asset_data_asset_msdt` | Retrieve asset msdt | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset Data | `connectsecure_get_asset_data_asset_msdt_by_id` | Retrieve asset msdt | id(必填) |
| Asset Data | `connectsecure_get_asset_data_asset_ports` | Retrieve asset ports | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset Data | `connectsecure_get_asset_data_asset_ports_by_id` | Retrieve asset port | id(必填) |
| Asset Data | `connectsecure_get_asset_data_asset_security_report_data` | Retrieve asset security report data | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset Data | `connectsecure_get_asset_data_asset_security_report_data_bulk` | Retrieve asset security report data | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset Data | `connectsecure_get_asset_data_asset_security_report_data_by_id` | Retrieve asset security report datum | id(必填) |
| Asset Data | `connectsecure_get_asset_data_asset_shares` | Retrieve asset shares | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset Data | `connectsecure_get_asset_data_asset_shares_by_id` | Retrieve asset share | id(必填) |
| Asset Data | `connectsecure_get_asset_data_asset_storages` | Retrieve asset storages | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset Data | `connectsecure_get_asset_data_asset_storages_by_id` | Retrieve asset storage | id(必填) |
| Asset Data | `connectsecure_get_asset_data_asset_unqouted_services` | Retrieve asset unqouted services | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset Data | `connectsecure_get_asset_data_asset_unqouted_services_by_id` | Retrieve asset unqouted service | id(必填) |
| Asset Data | `connectsecure_get_asset_data_asset_user_shares` | Retrieve asset user shares | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset Data | `connectsecure_get_asset_data_asset_user_shares_by_id` | Retrieve asset user share | id(必填) |
| Asset Data | `connectsecure_get_asset_data_asset_video_info` | Retrieve asset video info | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset Data | `connectsecure_get_asset_data_asset_video_info_by_id` | Retrieve asset video info | id(必填) |
| Asset Data | `connectsecure_get_asset_data_asset_windows_reboot_required` | Retrieve asset windows reboot required | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset Data | `connectsecure_get_asset_data_asset_windows_reboot_required_by_id` | Retrieve asset window reboot required | id(必填) |
| Asset Data | `connectsecure_get_asset_data_bios_info` | Retrieve bios info | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset Data | `connectsecure_get_asset_data_bios_info_by_id` | Retrieve bio info | id(必填) |
| Asset Data | `connectsecure_get_asset_data_browser_extensions` | Retrieve browser extensions | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset Data | `connectsecure_get_asset_data_browser_extensions_by_id` | Retrieve browser extension | id(必填) |
| Asset Data | `connectsecure_get_asset_data_ciphers_view` | Retrieve ciphers view | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset Data | `connectsecure_get_asset_data_ciphers_view_by_id` | Retrieve cipher view | id(必填) |
| Asset Data | `connectsecure_get_asset_data_windows_protection_status` | Retrieve windows protection status | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset Data | `connectsecure_get_asset_data_windows_protection_status_by_id` | Retrieve window protection status | id(必填) |
| Vulnerabilities | `connectsecure_get_vulnerabilities_application_vulnerabilities_by_os` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Vulnerabilities | `connectsecure_get_vulnerabilities_application_vulnerabilities_by_os_software_details` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Vulnerabilities | `connectsecure_get_vulnerabilities_application_vulnerabilities_by_os_software_details_suppressed` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Vulnerabilities | `connectsecure_get_vulnerabilities_application_vulnerabilities_by_product` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Vulnerabilities | `connectsecure_get_vulnerabilities_application_vulnerabilities_by_product_suppressed` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Vulnerabilities | `connectsecure_get_vulnerabilities_application_vulnerabilities_by_product_suppressed_tag` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Vulnerabilities | `connectsecure_get_vulnerabilities_application_vulnerabilities_by_product_tag` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Vulnerabilities | `connectsecure_get_vulnerabilities_application_vulnerabilities_net` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Vulnerabilities | `connectsecure_get_vulnerabilities_application_vulnerabilities_net_suppressed` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Vulnerabilities | `connectsecure_get_vulnerabilities_application_vulnerabilities_net_suppressed_tag` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Vulnerabilities | `connectsecure_get_vulnerabilities_application_vulnerabilities_net_tag` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Vulnerabilities | `connectsecure_get_vulnerabilities_application_vulnerabilities_suppressed` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Vulnerabilities | `connectsecure_get_vulnerabilities_application_vulnerabilities_suppressed_by_os` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Vulnerabilities | `connectsecure_get_vulnerabilities_application_vulnerabilities_suppressed_tag` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Vulnerabilities | `connectsecure_get_vulnerabilities_application_vulnerabilities_suppressed_tag_by_os` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Vulnerabilities | `connectsecure_get_vulnerabilities_application_vulnerabilities_tag` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Vulnerabilities | `connectsecure_get_vulnerabilities_application_vulnerabilities_tag_by_os` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Vulnerabilities | `connectsecure_get_vulnerabilities_report` | Retrieve records | cve(必填), skip(可选), limit(可选) |
| Vulnerabilities | `connectsecure_get_vulnerabilities_suppress_vulnerability` | Retrieve suppress vulnerability | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Vulnerabilities | `connectsecure_get_vulnerabilities_suppress_vulnerability_by_id` | Retrieve suppres vulnerability | id(必填) |
| Vulnerabilities | `connectsecure_get_vulnerabilities_suppress_vulnerability_problems` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Vulnerabilities | `connectsecure_get_vulnerabilities_suppress_vulnerability_solution` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_basic_info` | Retrieve ad basic info | company_id(必填), source(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_computers_view` | Retrieve ad computers view | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_domain_details` | Retrieve ad domain details | company_id(必填), source(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_gpos_details` | Retrieve ad gpos details | company_id(必填), domains_id(必填), source(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_gpos_view` | Retrieve ad gpos view | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_group_computers` | Retrieve ad group computers | company_id(必填), object_guid(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_group_users` | Retrieve ad group users | company_id(必填), object_guid(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_groups_view` | Retrieve ad groups view | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_ous_view` | Retrieve ad ous view | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_password_policies` | Retrieve ad password policies | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_roles` | Retrieve ad roles | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_roles_details` | Retrieve ad roles details | company_id(必填), object_guid(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_roles_member` | Retrieve ad roles member | company_id(必填), object_guid(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_user_licenses` | Retrieve ad user licenses | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_users_view` | Retrieve ad users view | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_azure_ad_logs` | Retrieve azure ad logs | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_azure_licenses` | Retrieve azure licenses | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_azure_secure_score` | Retrieve azure secure score | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_get_computer_details` | Retrieve get computer details | company_id(必填), object_guid(必填), source(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_get_groups_details` | Retrieve get groups details | company_id(必填), object_guid(必填), source(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_get_ous_details` | Retrieve get ous details | company_id(必填), object_guid(必填), source(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_get_user_details` | Retrieve get user details | company_id(必填), object_guid(必填), source(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Firewall | `connectsecure_get_firewall_firewall_groups` | Retrieve firewall groups | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Firewall | `connectsecure_get_firewall_firewall_groups_by_id` | Retrieve firewall group | id(必填) |
| Firewall | `connectsecure_get_firewall_firewall_interfaces` | Retrieve firewall interfaces | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Firewall | `connectsecure_get_firewall_firewall_interfaces_by_id` | Retrieve firewall interface | id(必填) |
| Firewall | `connectsecure_get_firewall_firewall_license` | Retrieve firewall license | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Firewall | `connectsecure_get_firewall_firewall_license_by_id` | Retrieve firewall license | id(必填) |
| Firewall | `connectsecure_get_firewall_firewall_rules` | Retrieve firewall rules | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Firewall | `connectsecure_get_firewall_firewall_rules_by_id` | Retrieve firewall rule | id(必填) |
| Firewall | `connectsecure_get_firewall_firewall_users` | Retrieve firewall users | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Firewall | `connectsecure_get_firewall_firewall_users_by_id` | Retrieve firewall user | id(必填) |
| Firewall | `connectsecure_get_firewall_firewall_zones` | Retrieve firewall zones | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Firewall | `connectsecure_get_firewall_firewall_zones_by_id` | Retrieve firewall zone | id(必填) |
| Compliance | `connectsecure_get_compliance_asset_compliance_details` | Retrieve records | asset_id(必填), platform(必填), compliance_type(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Compliance | `connectsecure_get_compliance_asset_compliance_report_data` | Retrieve records | asset_id(必填), company_id(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Compliance | `connectsecure_get_compliance_compliance_asset_info` | Retrieve records | compliance_status(必填), platform(必填), check_id(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Compliance | `connectsecure_get_compliance_compliance_check_asset_count` | Retrieve records | platform(必填), section(必填), compliance_type(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Compliance | `connectsecure_get_compliance_compliance_check_company_count` | Retrieve records | platform(必填), section(必填), compliance_type(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Compliance | `connectsecure_get_compliance_compliance_check_count` | Retrieve records | platform(必填), compliance_type(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Compliance | `connectsecure_get_compliance_compliance_check_count_by_section` | Retrieve records | platform(必填), compliance_status(必填), compliance_type(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Compliance | `connectsecure_get_compliance_compliance_internal_checks` | Retrieve records | compliance_type(必填), description(必填), platform(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Compliance | `connectsecure_get_compliance_compliance_maturity` | Retrieve records | platform(必填), compliance_type(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Compliance | `connectsecure_get_compliance_types` | Retrieve Compliance Types | 无 |
| Company | `connectsecure_get_company_adaudit` | Retrieve adaudit | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Company | `connectsecure_get_company_asset_windows_compatibility` | Retrieve asset windows compatibility | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Company | `connectsecure_get_company_companies` | Retrieve companies | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Company | `connectsecure_get_company_companies_by_id` | Retrieve company | id(必填) |
| Company | `connectsecure_get_company_company_stats` | Retrieve company stats | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Company | `connectsecure_get_company_company_stats_by_id` | Retrieve company stat | id(必填) |
| Company | `connectsecure_get_company_event_tickets` | Retrieve event tickets | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Company | `connectsecure_get_company_jobs_view` | Retrieve jobs view | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Company | `connectsecure_get_company_jobs_view_by_id` | Retrieve job view | id(必填) |
| Application Baseline | `connectsecure_get_application_baseline_app_baseline_plan_assets` | Retrieve app baseline plan assets | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Application Baseline | `connectsecure_get_application_baseline_app_baseline_plan_assets_by_id` | Retrieve app baseline plan asset | id(必填) |
| Application Baseline | `connectsecure_get_application_baseline_app_baseline_plan_company` | Retrieve app baseline plan company | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Application Baseline | `connectsecure_get_application_baseline_app_baseline_plan_company_by_id` | Retrieve app baseline plan company | id(必填) |
| Application Baseline | `connectsecure_get_application_baseline_app_baseline_plan_global` | Retrieve app baseline plan global | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Application Baseline | `connectsecure_get_application_baseline_app_baseline_plan_global_by_id` | Retrieve app baseline plan global | id(必填) |
| Application Baseline | `connectsecure_get_application_baseline_application_baseline_rules` | Retrieve application baseline rules | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Application Baseline | `connectsecure_get_application_baseline_application_baseline_rules_by_id` | Retrieve application baseline rule | id(必填) |
| Reports | `connectsecure_get_reports_cover_page` | Report Settings | 无 |
| Reports | `connectsecure_get_reports_download_default_template` | Report Settings | 无 |
| Reports | `connectsecure_get_reports_get_report_link` | Download report | job_id(必填), isGlobal(必填) |
| Reports | `connectsecure_get_reports_get_standard_report_settings` | Report Settings | reporttype(必填), isGlobal(必填) |
| Reports | `connectsecure_get_reports_report_jobs_view` | Retrieve report jobs view | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Reports | `connectsecure_get_reports_report_jobs_view_by_id` | Retrieve report job view | id(必填) |
| Reports | `connectsecure_get_reports_standard_reports` | List standard report | skip(可选), limit(可选), isGlobal(必填) |
| Integration | `connectsecure_get_integration_company_mappings` | Retrieve company mappings | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Integration | `connectsecure_get_integration_company_mappings_by_id` | Retrieve company mapping | id(必填) |
| Integration | `connectsecure_get_integration_integration_credentials` | Retrieve integration credentials | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Integration | `connectsecure_get_integration_integration_credentials_by_id` | Retrieve integration credential | id(必填) |
| Integration | `connectsecure_get_integration_integration_rules` | Retrieve integration rules | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Integration | `connectsecure_get_integration_integration_rules_by_id` | Retrieve integration rule | id(必填) |
| Credentials | `connectsecure_get_credentials_agent_credentials_mapping` | Retrieve agent credentials mapping | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Credentials | `connectsecure_get_credentials_agent_credentials_mapping_by_id` | Retrieve agent credential mapping | id(必填) |
| Credentials | `connectsecure_get_credentials_credentials` | Retrieve credentials | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Credentials | `connectsecure_get_credentials_credentials_by_id` | Retrieve credential | id(必填) |
| Discovery Settings | `connectsecure_get_discovery_settings_agent_discoverysettings_mapping` | Retrieve agent discoverysettings mapping | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Discovery Settings | `connectsecure_get_discovery_settings_agent_discoverysettings_mapping_by_id` | Retrieve agent discoverysetting mapping | id(必填) |
| Discovery Settings | `connectsecure_get_discovery_settings_discovery_settings` | Retrieve discovery settings | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Discovery Settings | `connectsecure_get_discovery_settings_discovery_settings_by_id` | Retrieve discovery setting | id(必填) |
| Attack Surface | `connectsecure_get_attack_surface_attack_surface_domain` | Retrieve attack surface domain | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Attack Surface | `connectsecure_get_attack_surface_attack_surface_domain_by_id` | Retrieve attack surface domain | id(必填) |
| Attack Surface | `connectsecure_get_attack_surface_attack_surface_results` | Retrieve attack surface results | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Attack Surface | `connectsecure_get_attack_surface_attack_surface_results_by_id` | Retrieve attack surface result | id(必填) |
| Tags | `connectsecure_get_tags_tag_rules` | Retrieve tag rules | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Tags | `connectsecure_get_tags_tag_rules_by_id` | Retrieve tag rule | id(必填) |
| Tags | `connectsecure_get_tags_tags` | Retrieve tags | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Tags | `connectsecure_get_tags_tags_by_id` | Retrieve tag | id(必填) |
| Ad Audit | `connectsecure_get_ad_audit_event_stats` | Retrieve event stats | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Ad Audit | `connectsecure_get_ad_audit_user_enabled_stats` | Retrieve user enabled stats | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Ad Audit | `connectsecure_get_ad_audit_user_event_stats` | Retrieve user event stats | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Ad Audit | `connectsecure_get_ad_audit_user_locked_stats` | Retrieve user locked stats | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Agent | `connectsecure_get_agent_agents` | Retrieve agents | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Agent | `connectsecure_get_agent_agents_by_id` | Retrieve agent | id(必填) |
| Agent | `connectsecure_get_agent_get_uninstall_secret` | Get uninstall secret token | company_id(必填) |
| Event Set | `connectsecure_get_event_set_event_set` | Retrieve event set | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Event Set | `connectsecure_get_event_set_event_set_by_id` | Retrieve event set | id(必填) |
| Ticket Template | `connectsecure_get_ticket_template_custom_ticketing_template` | Retrieve custom ticketing template | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Ticket Template | `connectsecure_get_ticket_template_custom_ticketing_template_by_id` | Retrieve custom ticketing template | id(必填) |
| Scheduler | `connectsecure_get_scheduler_scheduler` | Retrieve scheduler | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Scheduler | `connectsecure_get_scheduler_scheduler_by_id` | Retrieve scheduler | id(必填) |
| Backup Software | `connectsecure_get_backup_software_backup_software` | Retrieve backup software | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Backup Software | `connectsecure_get_backup_software_backup_software_by_id` | Retrieve backup software | id(必填) |
| EDR | `connectsecure_get_edr_edr` | Retrieve edr | condition(可选), skip(可选), limit(可选), order_by(可选) |
| EDR | `connectsecure_get_edr_edr_by_id` | Retrieve edr | id(必填) |
| PII | `connectsecure_get_pii_pii_scan_settings` | Retrieve pii scan settings | condition(可选), skip(可选), limit(可选), order_by(可选) |
| PII | `connectsecure_get_pii_pii_scan_settings_by_id` | Retrieve pii scan setting | id(必填) |
| External Scan | `connectsecure_get_external_scan_custom_profile` | Retrieve custom profile | condition(可选), skip(可选), limit(可选), order_by(可选) |
| External Scan | `connectsecure_get_external_scan_custom_profile_by_id` | Retrieve custom profile | id(必填) |
| Settings | `connectsecure_get_settings_custom_domains` | Retrieve custom domains | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Settings | `connectsecure_get_settings_custom_domains_by_id` | Retrieve custom domain | id(必填) |
| Compliance Assessment | `connectsecure_get_compliance_assessment_compliance_assessment` | Retrieve compliance assessment | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Compliance Assessment | `connectsecure_get_compliance_assessment_compliance_assessment_by_id` | Retrieve compliance assessment | id(必填) |
| Jobs | `connectsecure_get_jobs_job_details` | Retrieve job details | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Jobs | `connectsecure_get_jobs_job_details_view` | Retrieve job details view | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Patch Management | `connectsecure_get_patch_management_application_vulnerabilities` | Retrieve records | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Patch Management | `connectsecure_get_patch_management_application_vulnerabilities_os_patch` | Retrieve records | agent_type(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Users | `connectsecure_get_users_get_users` | Retrieve Users | condition(可选), skip(可选), limit(可选), order_by(可选) |

## 测试示例

```bash
# Health check
curl -s http://localhost:8080/health

# Call a tool via the MCP protocol (streamable HTTP) — requires an
# initialize handshake first per the MCP spec; abbreviated example below
# shows the tool-call request body only:
curl -s -X POST http://localhost:8080/mcp   -H "X-ConnectSecure-Access-Token: <jwt-access-token>"   -H "X-ConnectSecure-User-Id: <user-id>"   -H "X-ConnectSecure-Base-Url: https://pod1.connectsecure.com"   -H "Content-Type: application/json"   -H "Accept: application/json, text/event-stream"   -H "mcp-session-id: <session-id-from-initialize>"   -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "connectsecure_get_company_companies",
      "arguments": {}
    }
  }'
```

Expected: `200` with the companies list on a valid token; `401`/`403`
(surfaced by the tool as `Error: ConnectSecure API error 401/403: ...`) on an
invalid or expired token.

## API Reference

- Swagger UI: https://pod102.myconnectsecure.com/apidocs/ (spec:
  `https://pod102.myconnectsecure.com/apidocs/swagger.yaml`) — public, no
  login required. Each tenant's own pod hosts the identical spec.
- Overview / auth docs: see `/w/authorize` (tag `Auth`) in the spec above.

## Known Gaps

- **Read-only scope, by explicit user decision**: this MCP covers all 285
  `GET` (query) operations in the public spec. The ~78 `POST`/`PATCH`/`DELETE`
  write operations (create/update/delete company mappings, credentials,
  discovery settings, tags, scheduler jobs, etc.) are intentionally **not**
  implemented yet — can be added on request.
- **Two tool names were disambiguated** because their path's last segment
  collided with another endpoint in the same tag: `connectsecure_get_asset_remediate_records_companies`
  has a sibling in a different source path
  (`/r/get_data/remediate_records_companies`, suffixed `_get_data`), and
  `connectsecure_get_asset_notification_tickets_view` has a sibling at the
  bare (non-`/r/`) path (`/report_queries/...`, suffixed `_report_queries`).
- **`company_id`/`object_guid`/`asset_id` are not auto-resolved** — many
  Active Directory / Asset Data / Compliance tools require one of these IDs
  as input; call the corresponding list tool (e.g.
  `connectsecure_get_company_companies`, `connectsecure_get_asset_asset_view`)
  first to obtain it.
- Response field shapes are whatever the vendor's Swagger spec documents —
  not independently re-verified per endpoint beyond the schema-validity check
  (no bare arrays without `items`, confirmed with a script against
  `tools/list` output).
