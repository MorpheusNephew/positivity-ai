"""Thin wrapper around the Google Gen AI Python SDK."""

from google.genai import Client as GenAIClient
from google.genai.errors import APIError

from positivity_ai.generation.errors import GenerationException
from positivity_ai.generation.types import GenerationRequest


class GoogleGenAIClient:
    """Executes Google Gen AI SDK calls used by ``GeminiAdapter``."""

    #: Configured Google Gen AI SDK client.
    client: GenAIClient

    def __init__(self, client: GenAIClient):
        """Wrap an initialized Google Gen AI SDK client."""

        self.client = client

    @property
    def provider(self) -> str:
        """Return Google's identifier for normalized responses."""
        return "google"

    def get_models_list(self) -> list[str]:
        """Return model IDs visible to the configured Google credential."""
        list_of_models = self.client.models.list()

        # Google returns resource names such as ``models/gemini-3.1-flash-lite``;
        # adapters use the shorter identifier accepted by generation requests.
        return [model.name.split("/")[1] for model in list_of_models]

    def create_response(self, request: GenerationRequest):
        """Translate ``request`` into a Gemini Interactions API call."""
        input_steps = [
            {
                "type": "user_input" if message.role == "user" else "model_output",
                "content": [{"type": "text", "text": message.content}],
            }
            for message in request.messages
        ]

        try:
            return self.client.interactions.create(
                input=input_steps,
                model=request.model,
                system_instruction=request.system_prompt,
                store=False,
            )
        except APIError as error:
            # Keep the SDK traceback available while exposing an app-level error.
            raise GenerationException(str(error)) from error
