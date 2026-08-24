from typing import Annotated

from pydantic import Field

from .._json import error_envelope

NO_TOKEN = error_envelope(
    "not_configured",
    "No ConnectSecure credentials. Send the X-ConnectSecure-Access-Token, "
    "X-ConnectSecure-User-Id, and X-ConnectSecure-Base-Url headers.",
    False,
)

# Shared param annotations for the condition/skip/limit/order_by quartet that
# nearly every list-style report tool exposes. Centralized here so the wording
# (and any future correction, e.g. if the real `condition` grammar is ever
# confirmed) only needs to change in one place.
#
# `condition` note: this codebase forwards the value verbatim to ConnectSecure
# (see api_client.ConnectSecureClient.get / _clean_params) with no parsing,
# validation, or construction of its own, and no example of the expression
# grammar (SQL-like clause? key=value? another DSL?) exists anywhere in this
# repo's code, comments, README, or tests. The description below says that
# plainly instead of guessing a syntax.
ConditionParam = Annotated[
    str | None,
    Field(
        description=(
            "Vendor-defined filter expression, forwarded as-is to ConnectSecure's report-query "
            "endpoint. This service does not parse, validate, or construct it, and no confirmed "
            "example of its grammar (SQL-like clause, key=value, or another DSL) exists in this "
            "codebase or its docs — treat the exact syntax as unverified and check ConnectSecure's "
            "own API/Swagger reference before relying on a specific format."
        )
    ),
]
SkipParam = Annotated[
    int | None,
    Field(description="Zero-based offset: number of matching records to skip before the returned page, for pagination."),
]
LimitParam = Annotated[
    int | None,
    Field(description="Max records to return in this call. Capped at 200 server-side regardless of the value passed."),
]
OrderByParam = Annotated[
    str | None,
    Field(description="Field name to sort results by, passed through as-is to the upstream report query."),
]
