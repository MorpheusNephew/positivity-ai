"""Gemini implementation of the model adapter contract."""

from os import getenv
from typing import ClassVar

from google.genai import Client as GenAIClient

from positivity_ai.clients.google_genai import GoogleGenAIClient
from positivity_ai.clients.model_client import ModelClient
from positivity_ai.generation.types import (
    AssistantMessage,
    GenerationRequest,
    GenerationResponse,
)


class GeminiAdapter:
    """Adapts provider-neutral generation requests for the Gemini API."""

    SUPPORTED_TEXT_MODELS: ClassVar[frozenset[str]] = frozenset(
        {
            # Gemini 3 model IDs
            "gemini-3.8-flash",
            "gemini-3.7-flash",
            "gemini-3.6-flash",
            "gemini-3.5-flash",
            "gemini-3.5-flash-lite",
            "gemini-3.1-pro-preview",
            "gemini-3.1-flash-lite",
            "gemini-3-flash-preview",
            # Gemini 2.5 model IDs
            "gemini-2.5-pro",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            # Gemini 2 model IDs
            "gemini-2.0-flash",
            "gemini-2.0-flash-lite",
            # Gemma open-weight model IDs
            "gemma-2-2b-it",
            "gemma-2-9b-it",
            "gemma-2-27b-it",
            "codegemma-7b-it",
        }
    )

    #: Client used to send provider-specific requests to Gemini.
    client: ModelClient

    def __init__(self, api_key: str = None):
        """Create an adapter with a Google Gen AI SDK client."""
        api_key = api_key if api_key else getenv("GEMINI_API_KEY")

        client = GenAIClient(api_key=api_key)

        self.client = GoogleGenAIClient(client)

    def get_models_list(self) -> list[str]:
        """Return text-generation model IDs eligible for use with this adapter."""
        available_models = self.client.get_models_list()

        return [
            model for model in available_models if model in self.SUPPORTED_TEXT_MODELS
        ]

    def generate(self, request: GenerationRequest) -> GenerationResponse:
        """Send ``request`` to Gemini and return a temporary normalized response."""

        response = self.client.create_response(request)

        print(response)

        return GenerationResponse(
            provider=self.client.provider,
            model="some random model",
            message=AssistantMessage(content="Here's some magical stuff"),
            total_tokens=7,
        )
