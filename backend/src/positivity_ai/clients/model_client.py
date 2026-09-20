"""Provider-specific client contract used by model adapters."""

from typing import Protocol

from positivity_ai.generation.types import GenerationRequest


class ModelClient(Protocol):
    """Defines the provider-specific operations required by model adapters."""

    @property
    def provider(self) -> str:
        """Return this provider's identifier for normalized responses."""
        ...

    def get_models_list(self) -> list[str]:
        """Return model IDs available from this provider."""
        ...

    def create_response(self, request: GenerationRequest):
        """Send a generation request to this provider and return its raw response."""
        ...
