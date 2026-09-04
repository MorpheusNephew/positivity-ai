"""The provider-neutral interface implemented by model adapters."""

from typing import Protocol

from positivity_ai.generation import GenerationRequest, GenerationResponse


class ModelAdapter(Protocol):
    """Describes an adapter capable of requesting a model generation."""

    def generate(self, request: GenerationRequest) -> GenerationResponse:
        """Generate a response for ``request`` or raise ``GenerationException`` on failure."""
        ...
