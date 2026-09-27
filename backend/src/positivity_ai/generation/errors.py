"""Exceptions raised when a provider cannot complete a generation."""


class GenerationException(Exception):
    """A normalized technical failure returned by a model provider."""

    def __init__(self, message):
        super().__init__(message)
