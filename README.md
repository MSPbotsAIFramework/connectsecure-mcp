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

**50 read-only (`GET`) tools**, trimmed down from an initial 285-tool build
that covered ConnectSecure's entire public query API. The full build hit the
platform's aggregate MCP function-declaration ceiling (Vertex AI/Gemini caps
a single model call at 512 function declarations across *all* loaded MCP
servers), so scope was cut to the tools with real signal:

- **All 11 endpoints MSPbots' own production integration actually calls**
  (confirmed via `web/int/sys/integration/api/list` against integration id
  `2008424422784020481`), spread across Asset/Company/Users/Active Directory.
- **Active Directory (22 tools, full category)** — kept in full since AD
  posture (users, password policies, basic info, Azure secure score, etc.) is
  a primary use case for this server.
- **Company (9, full category)** and **Users (1)** — small, kept in full.
- **Asset (18 curated core/summary tools)** — trimmed from 110: kept
  list/summary-level queries (`assets`, `asset_view`, `asset_stats`,
  `distinct_os`, `distinct_platform`, `total_asset_count`, `risk_score`,
  `vulnerabilities_details`, `vulnerabilities_count`,
  `asset_critical_vulnerabilities`, `external_asset_vulnerabilities`,
  `remediate_records`, `sw_problems_remediations_view`, `problems_summary`,
  `asset_software`, `asset_users`, `get_asset_remediation_plan`,
  `remediation_plan_global`); dropped narrow drill-down variants
  (`_by_id`, `_suppressed`, `_tag`, per-company/per-day breakdowns, etc.).

**Cut entirely** (available in ConnectSecure's API but not exposed here —
see Known Gaps): Asset Data (33, field-level machine detail), Vulnerabilities
category (22, overlapped with the vulnerability summaries kept in Asset),
Compliance (10), Reports (7), Firewall (12), Application Baseline (8),
Integration (6), Ad Audit, Agent, Attack Surface, Tags, Credentials,
Discovery Settings, Compliance Assessment, Backup Software, EDR, Event Set,
External Scan, Jobs, Patch Management, PII, Scheduler, Settings, Ticket
Template (2-4 each, mostly administrative/config endpoints). Write operations
(`POST`/`PATCH`/`DELETE`, ~78 of them) were never in scope — see **Known Gaps**.

## Authentication

ConnectSecure is multi-tenant: every tenant is provisioned on its own pod
hostname (e.g. `https://pod1.connectsecure.com`), and auth is a JWT access
token obtained out-of-band via:

```
POST {base_url}/w/authorize
Client-Auth-Token: base64(tenant_name + "+" + client_id + ":" + client_secret)
```

(Note the literal `+` between `tenant_name` and `client_id` — confirmed against
both ConnectSecure's own Swagger description and MSPbots' real implementation
in `autointegration`'s `ConnectSecureAuth.java`; easy to miss since the
Swagger text renders it ambiguously as "tenant+client_id".)

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
| Active Directory | `connectsecure_get_active_directory_ad_basic_info` | Retrieve ad basic info. | company_id(必填), source(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_computers_view` | Retrieve ad computers view. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_domain_details` | Retrieve ad domain details. | company_id(必填), source(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_gpos_details` | Retrieve ad gpos details. | company_id(必填), domains_id(必填), source(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_gpos_view` | Retrieve ad gpos view. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_group_computers` | Retrieve ad group computers. | company_id(必填), object_guid(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_group_users` | Retrieve ad group users. | company_id(必填), object_guid(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_groups_view` | Retrieve ad groups view. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_ous_view` | Retrieve ad ous view. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_password_policies` | Retrieve ad password policies. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_roles` | Retrieve ad roles. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_roles_details` | Retrieve ad roles details. | company_id(必填), object_guid(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_roles_member` | Retrieve ad roles member. | company_id(必填), object_guid(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_user_licenses` | Retrieve ad user licenses. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_ad_users_view` | Retrieve ad users view. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_azure_ad_logs` | Retrieve azure ad logs. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_azure_licenses` | Retrieve azure licenses. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_azure_secure_score` | Retrieve azure secure score. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_get_computer_details` | Retrieve get computer details. | company_id(必填), object_guid(必填), source(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_get_groups_details` | Retrieve get groups details. | company_id(必填), object_guid(必填), source(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_get_ous_details` | Retrieve get ous details. | company_id(必填), object_guid(必填), source(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Active Directory | `connectsecure_get_active_directory_get_user_details` | Retrieve get user details. | company_id(必填), object_guid(必填), source(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_asset_critical_vulnerabilities` | Retrieve records. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_asset_software` | Retrieve records. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_asset_stats` | Retrieve asset stats. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_asset_users` | Retrieve asset users. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_asset_view` | Retrieve asset view. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_assets` | Retrieve assets. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_distinct_os` | Retrieve records. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_distinct_platform` | Retrieve records. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_external_asset_vulnerabilities` | Retrieve records. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_get_asset_remediation_plan` | Retrieve records. | having(必填), condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_problems_summary` | Retrieve records. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_remediate_records` | Retrieve records. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_remediation_plan_global` | Retrieve records. |  |
| Asset | `connectsecure_get_asset_risk_score` | Retrieve records. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_sw_problems_remediations_view` | Retrieve records. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_total_asset_count` | Retrieve records. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_vulnerabilities_count` | Retrieve records. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Asset | `connectsecure_get_asset_vulnerabilities_details` | Retrieve records. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Company | `connectsecure_get_company_adaudit` | Retrieve adaudit. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Company | `connectsecure_get_company_asset_windows_compatibility` | Retrieve asset windows compatibility. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Company | `connectsecure_get_company_companies` | Retrieve companies. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Company | `connectsecure_get_company_companies_by_id` | Retrieve company. | id(必填) |
| Company | `connectsecure_get_company_company_stats` | Retrieve company stats. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Company | `connectsecure_get_company_company_stats_by_id` | Retrieve company stat. | id(必填) |
| Company | `connectsecure_get_company_event_tickets` | Retrieve event tickets. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Company | `connectsecure_get_company_jobs_view` | Retrieve jobs view. | condition(可选), skip(可选), limit(可选), order_by(可选) |
| Company | `connectsecure_get_company_jobs_view_by_id` | Retrieve job view. | id(必填) |
| Users | `connectsecure_get_users_get_users` | Retrieve Users. | condition(可选), skip(可选), limit(可选), order_by(可选) |

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

**Live self-test against a real account: passed.** Using a real
`access_token`/`user_id`/pod for tenant `mspbots` (pod `pod107`), called
through the running MCP server end-to-end:

- `connectsecure_get_users_get_users` → returned 11 real user records.
- `connectsecure_get_company_companies` → returned the real company
  (`id: 11939`, `mspbots.ai`, `internal_scan: false`).
- `connectsecure_get_active_directory_ad_basic_info`,
  `connectsecure_get_active_directory_ad_users_view`,
  `connectsecure_get_asset_assets`, `connectsecure_get_asset_vulnerabilities_details`
  → all returned `{"status": true, "total": 0}` (genuine empty result, not
  an error). Cross-checked against the two non-empty calls above: since the
  same auth/parsing path returns real data for users/companies, the zero
  counts for AD/asset/vulnerability endpoints reflect this test tenant
  having `internal_scan: false` (no on-prem scan agent deployed) — nothing
  has been scanned yet — not a broken pipeline or masked auth failure.
- **`Client-Auth-Token` format correction**: the initial `/w/authorize`
  attempt (base64 of `tenant_name` + `client_id` + `:` + `client_secret`,
  no separator between `tenant_name` and `client_id`) got a real `403` from
  ConnectSecure. This was first (wrongly) suspected to mean the provided
  `client_secret` was still MSPbots-internal ciphertext (it base64-decodes
  to a `gAAAAA...`-prefixed string, the signature of a Python
  `cryptography.fernet` token). That hypothesis was disproved by checking
  the real implementation in MSPbots' `autointegration` repo
  (`client/src/main/java/mspbots/integration/client/core/auth/impl/ConnectSecureAuth.java`):
  the actual formula inserts a literal `+` between `tenant_name` and
  `client_id` — `base64(tenant_name + "+" + client_id + ":" + client_secret)`
  — and uses `client_secret` completely as-is, with no decryption step
  anywhere in that codebase. Rebuilding the token with the literal `+`
  included, using the exact same (unmodified) `client_secret` value, got a
  real `200` from `/w/authorize` with a valid `access_token`. So the
  `client_secret` was fine all along; the bug was purely in the test
  script's string concatenation, not in ConnectSecure, MSPbots' credential
  storage, or this MCP server (which never performs the `/w/authorize`
  exchange itself — see Authentication).

## API Reference

- Swagger UI: https://pod102.myconnectsecure.com/apidocs/ (spec:
  `https://pod102.myconnectsecure.com/apidocs/swagger.yaml`) — public, no
  login required. Each tenant's own pod hosts the identical spec.
- Overview / auth docs: see `/w/authorize` (tag `Auth`) in the spec above.

## Known Gaps

- **Trimmed from 285 to 50 tools, by explicit user decision**, after the
  full 285-tool build tripped the platform's aggregate MCP
  function-declaration ceiling (Vertex AI/Gemini caps a single model call at
  512 function declarations across all loaded MCP servers). Kept: the 11
  endpoints MSPbots' own production integration actually calls, the full
  Active Directory/Company/Users categories, and 18 curated Asset
  list/summary tools. Cut entirely: Asset Data, the standalone
  Vulnerabilities category, Compliance, Reports, Firewall, Application
  Baseline, Integration, and a long tail of small administrative/config
  categories (Ad Audit, Agent, Attack Surface, Tags, Credentials, Discovery
  Settings, Compliance Assessment, Backup Software, EDR, Event Set, External
  Scan, Jobs, Patch Management, PII, Scheduler, Settings, Ticket Template) —
  see **Scope** for the full breakdown. Any of these can be re-added on
  request if a real use case needs them.
- **Read-only scope, by explicit user decision** (unchanged from the
  original build): the ~78 `POST`/`PATCH`/`DELETE` write operations
  (create/update/delete company mappings, credentials, discovery settings,
  tags, scheduler jobs, etc.) were never implemented — can be added on
  request.
- **`company_id`/`object_guid`/`asset_id` are not auto-resolved** — many
  Active Directory / Asset Data / Compliance tools require one of these IDs
  as input; call the corresponding list tool (e.g.
  `connectsecure_get_company_companies`, `connectsecure_get_asset_asset_view`)
  first to obtain it.
- Response field shapes are whatever the vendor's Swagger spec documents —
  not independently re-verified per endpoint beyond the schema-validity check
  (no bare arrays without `items`, confirmed with a script against
  `tools/list` output).
