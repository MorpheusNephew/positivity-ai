"""OpenAI implementation of the model adapter contract."""

from typing import ClassVar

from positivity_ai.generation import (
    GenerationRequest,
    GenerationResponse,
    AssistantMessage,
)

from .client import OpenAIClient


class OpenAIAdapter:
    """Adapter responsible for translating generation requests to OpenAI calls."""

    #: Canonical OpenAI model IDs that Positivity AI supports for text generation.
    SUPPORTED_TEXT_MODELS: ClassVar[frozenset[str]] = frozenset(
        {
            "gpt-4.1",
            "gpt-4.1-mini",
            "gpt-4.1-nano",
            "gpt-4o",
            "gpt-4o-mini",
            "gpt-5.4",
            "gpt-5.4-mini",
            "gpt-5.4-nano",
            "gpt-5.5",
            "gpt-5.5-pro",
            "gpt-5.6-luna",
            "gpt-5.6-sol",
            "gpt-5.6-terra",
        }
    )

    #: Client used to send provider-specific requests to OpenAI.
    openai_client: OpenAIClient

    def __init__(self):
        """Create an adapter with an OpenAI SDK client."""
        self.openai_client = OpenAIClient()

    def get_models_list(self) -> list[str]:
        """Return accessible OpenAI text-generation models supported by this app."""
        available_models = self.openai_client.get_models_list()

        return [
            model for model in available_models if model in self.SUPPORTED_TEXT_MODELS
        ]

    def generate(self, request: GenerationRequest) -> GenerationResponse:
        """Return a temporary response while the OpenAI integration is being built.

        The response validates the provider-neutral adapter contract but does not
        yet send ``request`` to OpenAI.
        """

        return GenerationResponse(
            provider="OpenAI",
            model="some random model",
            message=AssistantMessage(content="Here's some magical stuff"),
            total_tokens=7,
        )
