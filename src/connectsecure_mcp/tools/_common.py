from .._json import error_envelope

NO_TOKEN = error_envelope(
    "not_configured",
    "No ConnectSecure credentials. Send the X-ConnectSecure-Access-Token, "
    "X-ConnectSecure-User-Id, and X-ConnectSecure-Base-Url headers.",
    False,
)
