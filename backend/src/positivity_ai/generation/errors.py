"""Exceptions raised when a provider cannot complete a generation."""


class GenerationException(Exception):
    """A normalized technical failure returned by a model provider."""

    #: HTTP status code returned by the provider, when one is available.
    status_code: int
    #: Provider-defined status or error code.
    status: str
    #: Human-readable description of the provider failure.
    message: str
