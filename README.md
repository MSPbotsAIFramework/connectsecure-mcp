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

**19 read-only (`GET`) tools**, trimmed twice: first from an initial
285-tool full-API build down to 50 tools (to stay under Vertex AI/Gemini's
512-function-declaration ceiling across all loaded MCP servers), then
again on 2026-08-04 down to 19 tools per the "actual usage + minimal
same-category CRUD" scope decision applied across this program's MCP
fleet.

The 2026-08-04 trim confirmed **all 11 endpoints MSPbots' own production
integration actually calls** (via `web/int/sys/integration/api/list`
against integration id `2008424422784020481`):
`vulnerabilities_details`, `external_asset_vulnerabilities`,
`remediate_records`, `asset_critical_vulnerabilities`, `asset_view`,
`sw_problems_remediations_view` (all `asset`); `azure_secure_score`,
`ad_users_view`, `ad_password_policies` (all `active_directory`);
`companies`/`company` (`company`); `users` (`users`). Every one of those
is kept, plus a small amount of same-category padding for baseline
visibility:

- **`asset` (9 of the prior 18)**: the 6 actually-used tools above, plus
  `assets` (base list), `asset_stats`, `risk_score`.
- **`active_directory` (6 of the prior 22)**: the 3 actually-used tools
  above, plus `ad_basic_info`, `ad_domain_details`, `ad_groups_view`.
- **`company` (3 of the prior 9)**: `companies`, `companies_by_id`,
  `company_stats`.
- **`users` (1, unchanged)**: `get_users`.

**Cut entirely** on 2026-08-04 (available in the prior 50-tool build but
not exposed here): the other 16 `asset` tools (`asset_software`,
`asset_users`, `distinct_os`, `distinct_platform`,
`total_asset_count`, `vulnerabilities_count`, `problems_summary`,
`get_asset_remediation_plan`, `remediation_plan_global`), the other 16
`active_directory` tools (computers/GPOs/groups/OUs/roles detail views,
Azure AD logs/licenses, user licenses/details), and the other 6 `company`
tools (`adaudit`, `asset_windows_compatibility`, `event_tickets`,
`jobs_view` + `jobs_view_by_id`).

**Cut in the earlier 285→50 pass** (still not exposed here — see Known
Gaps for the full accounting): Asset Data (33, field-level machine
detail), Vulnerabilities category (22, overlapped with the vulnerability
summaries kept in Asset), Compliance (10), Reports (7), Firewall (12),
Application Baseline (8), Integration (6), Ad Audit, Agent, Attack
Surface, Tags, Credentials, Discovery Settings, Compliance Assessment,
Backup Software, EDR, Event Set, External Scan, Jobs, Patch Management,
PII, Scheduler, Settings, Ticket Template (2-4 each, mostly
administrative/config endpoints). Write operations (`POST`/`PATCH`/
`DELETE`, ~78 of them) were never in scope in either pass. If a removed
tool is needed later, the vendor's Swagger spec (linked below) still
documents it and it can be re-added the same way the kept tools were
generated.

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

| Category | Tool | Description | Params |
|---|---|---|---|
| active_directory | `connectsecure_get_active_directory_ad_basic_info` | Retrieve ad basic info. | company_id, source, condition?, skip?, limit?, order_by? |
| active_directory | `connectsecure_get_active_directory_ad_domain_details` | Retrieve ad domain details. | company_id, source, condition?, skip?, limit?, order_by? |
| active_directory | `connectsecure_get_active_directory_ad_groups_view` | Retrieve ad groups view. | condition?, skip?, limit?, order_by? |
| active_directory | `connectsecure_get_active_directory_ad_password_policies` | Retrieve ad password policies. | condition?, skip?, limit?, order_by? |
| active_directory | `connectsecure_get_active_directory_ad_users_view` | AD user account inventory for a client company (not ConnectSecure's own platform users — see `users_get_users`). | condition?, skip?, limit?, order_by? |
| active_directory | `connectsecure_get_active_directory_azure_secure_score` | Retrieve azure secure score. | condition?, skip?, limit?, order_by? |
| asset | `connectsecure_get_asset_asset_critical_vulnerabilities` | Vulnerability findings filtered to critical severity only (severity-scoped subset of `vulnerabilities_details`). | condition?, skip?, limit?, order_by? |
| asset | `connectsecure_get_asset_asset_stats` | Aggregate asset inventory counters, not individual asset records. | condition?, skip?, limit?, order_by? |
| asset | `connectsecure_get_asset_asset_view` | Per-asset inventory view from the core asset resource (primary asset listing). | condition?, skip?, limit?, order_by? |
| asset | `connectsecure_get_asset_assets` | Report-query asset list, same query group as `asset_stats` (alternative to `asset_view`). | condition?, skip?, limit?, order_by? |
| asset | `connectsecure_get_asset_external_asset_vulnerabilities` | Vulnerability findings scoped to externally-facing (internet-exposed) assets only. | condition?, skip?, limit?, order_by? |
| asset | `connectsecure_get_asset_remediate_records` | Remediation action records (fixes applied/recommended per finding), not raw findings. | condition?, skip?, limit?, order_by? |
| asset | `connectsecure_get_asset_risk_score` | Computed aggregate risk-score rating per asset/company. | condition?, skip?, limit?, order_by? |
| asset | `connectsecure_get_asset_sw_problems_remediations_view` | Software-specific problems (missing/outdated software) paired with remediation status. | condition?, skip?, limit?, order_by? |
| asset | `connectsecure_get_asset_vulnerabilities_details` | Full vulnerability findings across all assets/severities (base finding-level dataset). | condition?, skip?, limit?, order_by? |
| company | `connectsecure_get_company_companies` | Retrieve companies. | condition?, skip?, limit?, order_by? |
| company | `connectsecure_get_company_companies_by_id` | Retrieve company. | id |
| company | `connectsecure_get_company_company_stats` | Retrieve company stats. | condition?, skip?, limit?, order_by? |
| users | `connectsecure_get_users_get_users` | Retrieve Users. | condition?, skip?, limit?, order_by? |

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

- **Trimmed twice.** First from 285 to 50 tools, by explicit user decision,
  after the full 285-tool build tripped the platform's aggregate MCP
  function-declaration ceiling (Vertex AI/Gemini caps a single model call at
  512 function declarations across all loaded MCP servers) — see below for
  what that pass cut. Then again on 2026-08-04, from 50 to 19 tools, per
  the "actual usage + minimal same-category CRUD" scope decision applied
  across this program's MCP fleet — kept the 11 endpoints MSPbots' own
  production integration actually calls plus light same-category padding;
  cut the rest of what had been "full category" Active Directory/Company
  and the broader 18-tool Asset set down further. See **Scope** for the
  exact breakdown of both passes. Any removed tool can be re-added on
  request if a real use case needs it — the vendor's Swagger spec (linked
  below) still documents its exact shape.
- **285→50 pass cut entirely**: Asset Data, the standalone
  Vulnerabilities category, Compliance, Reports, Firewall, Application
  Baseline, Integration, and a long tail of small administrative/config
  categories (Ad Audit, Agent, Attack Surface, Tags, Credentials, Discovery
  Settings, Compliance Assessment, Backup Software, EDR, Event Set, External
  Scan, Jobs, Patch Management, PII, Scheduler, Settings, Ticket Template).
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
