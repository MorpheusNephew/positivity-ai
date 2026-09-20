"""OpenAI implementation of the model adapter contract."""

from os import getenv
from typing import ClassVar

from openai import OpenAI
from positivity_ai.clients.model_client import ModelClient
from positivity_ai.generation import (
    GenerationRequest,
    GenerationResponse,
    AssistantMessage,
)

from positivity_ai.clients.openai import OpenAIClient


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
    client: ModelClient

    def __init__(self, api_key: str = None):
        """Create an adapter with an OpenAI SDK client."""

        api_key = api_key if api_key else getenv("OPENAI_API_KEY")

        client = OpenAI(api_key=api_key)

        self.client = OpenAIClient(client)

    def get_models_list(self) -> list[str]:
        """Return accessible OpenAI text-generation models supported by this app."""
        available_models = self.client.get_models_list()

        return [
            model for model in available_models if model in self.SUPPORTED_TEXT_MODELS
        ]

    def generate(self, request: GenerationRequest) -> GenerationResponse:
        """Send ``request`` to OpenAI and return a temporary normalized response."""

        response = self.client.create_response(request)

        print(response)

        return GenerationResponse(
            provider="OpenAI",
            model="some random model",
            message=AssistantMessage(content="Here's some magical stuff"),
            total_tokens=7,
        )
