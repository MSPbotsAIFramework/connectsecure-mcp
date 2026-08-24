from collections.abc import Callable

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

from .._json import dump_json_capped
from ..api_client import ConnectSecureClient, ConnectSecureError
from ._common import NO_TOKEN, ConditionParam, LimitParam, OrderByParam, SkipParam

_MAX_LIMIT = 200


def register(mcp: FastMCP, client_factory: Callable[[], ConnectSecureClient | None]) -> None:
    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def connectsecure_get_asset_asset_critical_vulnerabilities(
        condition: ConditionParam = None,
        skip: SkipParam = None,
        limit: LimitParam = None,
        order_by: OrderByParam = None,
    ) -> str:
        """Vulnerability findings filtered to critical severity only, across all assets.

        A severity-scoped subset of the full finding set — see
        connectsecure_get_asset_vulnerabilities_details for critical plus every
        other severity.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        if limit is not None:
            limit = min(limit, _MAX_LIMIT)
        params = {"condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/asset_critical_vulnerabilities", params=params)
            return dump_json_capped(result)
        except ConnectSecureError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def connectsecure_get_asset_asset_stats(
        condition: ConditionParam = None,
        skip: SkipParam = None,
        limit: LimitParam = None,
        order_by: OrderByParam = None,
    ) -> str:
        """Aggregate asset inventory counters (totals/breakdowns), not individual asset records.

        Summary numbers only; use connectsecure_get_asset_assets or
        connectsecure_get_asset_asset_view for the underlying per-asset rows.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        if limit is not None:
            limit = min(limit, _MAX_LIMIT)
        params = {"condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/asset_stats", params=params)
            return dump_json_capped(result)
        except ConnectSecureError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def connectsecure_get_asset_asset_view(
        condition: ConditionParam = None,
        skip: SkipParam = None,
        limit: LimitParam = None,
        order_by: OrderByParam = None,
    ) -> str:
        """Per-asset inventory view from ConnectSecure's core asset resource, one row per asset.

        Served from the dedicated asset resource rather than the report-query
        group the other asset_* tools use; treat it as the primary asset
        listing (see connectsecure_get_asset_assets for the report-query
        variant, and connectsecure_get_asset_asset_stats for counts only).
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        if limit is not None:
            limit = min(limit, _MAX_LIMIT)
        params = {"condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/asset/asset_view", params=params)
            return dump_json_capped(result)
        except ConnectSecureError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def connectsecure_get_asset_assets(
        condition: ConditionParam = None,
        skip: SkipParam = None,
        limit: LimitParam = None,
        order_by: OrderByParam = None,
    ) -> str:
        """Report-query asset list: one row per asset, same query group as asset_stats.

        Alongside the vulnerability/remediation report tools rather than the
        core asset resource; see connectsecure_get_asset_asset_view for that
        alternative asset listing.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        if limit is not None:
            limit = min(limit, _MAX_LIMIT)
        params = {"condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/assets", params=params)
            return dump_json_capped(result)
        except ConnectSecureError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def connectsecure_get_asset_external_asset_vulnerabilities(
        condition: ConditionParam = None,
        skip: SkipParam = None,
        limit: LimitParam = None,
        order_by: OrderByParam = None,
    ) -> str:
        """Vulnerability findings scoped to externally-facing (internet-exposed) assets only.

        The external-attack-surface subset; see
        connectsecure_get_asset_vulnerabilities_details for the full
        internal-plus-external finding set.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        if limit is not None:
            limit = min(limit, _MAX_LIMIT)
        params = {"condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/external_asset_vulnerabilities", params=params)
            return dump_json_capped(result)
        except ConnectSecureError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def connectsecure_get_asset_remediate_records(
        condition: ConditionParam = None,
        skip: SkipParam = None,
        limit: LimitParam = None,
        order_by: OrderByParam = None,
    ) -> str:
        """Remediation action records: fixes applied/recommended per finding, not raw findings.

        Tracks remediation status/history; use
        connectsecure_get_asset_vulnerabilities_details for the underlying
        vulnerability findings being remediated.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        if limit is not None:
            limit = min(limit, _MAX_LIMIT)
        params = {"condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/remediate_records", params=params)
            return dump_json_capped(result)
        except ConnectSecureError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def connectsecure_get_asset_risk_score(
        condition: ConditionParam = None,
        skip: SkipParam = None,
        limit: LimitParam = None,
        order_by: OrderByParam = None,
    ) -> str:
        """Computed aggregate risk-score rating per asset/company, not individual findings.

        A scoring/summary report — similar in role to asset_stats but
        risk-focused rather than inventory-count-focused.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        if limit is not None:
            limit = min(limit, _MAX_LIMIT)
        params = {"condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/risk_score", params=params)
            return dump_json_capped(result)
        except ConnectSecureError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def connectsecure_get_asset_sw_problems_remediations_view(
        condition: ConditionParam = None,
        skip: SkipParam = None,
        limit: LimitParam = None,
        order_by: OrderByParam = None,
    ) -> str:
        """Software-specific problems (missing/outdated software) paired with remediation status.

        Narrower than remediate_records: scoped to software problems
        specifically, with fix status joined into the same view.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        if limit is not None:
            limit = min(limit, _MAX_LIMIT)
        params = {"condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/sw_problems_remediations_view", params=params)
            return dump_json_capped(result)
        except ConnectSecureError as e:
            return e.to_envelope()

    @mcp.tool(annotations=ToolAnnotations(readOnlyHint=True))
    async def connectsecure_get_asset_vulnerabilities_details(
        condition: ConditionParam = None,
        skip: SkipParam = None,
        limit: LimitParam = None,
        order_by: OrderByParam = None,
    ) -> str:
        """Full vulnerability findings, all assets and severities: the base finding-level dataset.

        The other asset vulnerability tools are scoped subsets of this one:
        asset_critical_vulnerabilities filters to critical severity,
        external_asset_vulnerabilities filters to internet-exposed assets.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        if limit is not None:
            limit = min(limit, _MAX_LIMIT)
        params = {"condition": condition, "skip": skip, "limit": limit, "order_by": order_by}
        try:
            result = await client.get("/r/report_queries/vulnerabilities_details", params=params)
            return dump_json_capped(result)
        except ConnectSecureError as e:
            return e.to_envelope()
