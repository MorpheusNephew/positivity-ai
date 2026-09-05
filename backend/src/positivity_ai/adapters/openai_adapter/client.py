"""Thin wrapper around the OpenAI Python SDK."""

from openai import OpenAI

from positivity_ai.generation import GenerationRequest


class OpenAIClient:
    """Executes OpenAI SDK calls used by ``OpenAIAdapter``."""

    #: Configured OpenAI SDK client.
    client: OpenAI

    def __init__(self):
        """Create an OpenAI SDK client using the configured environment credentials."""
        self.client = OpenAI()

    def get_models_list(self) -> list[str]:
        """Return model IDs visible to the configured OpenAI credential."""
        list_of_models = self.client.models.list()

        list_of_models = [model.id for model in list_of_models]

        return list_of_models

    def create_response(self, request: GenerationRequest) -> None:
        """Placeholder for translating ``request`` into an OpenAI response call.

        The request is not yet translated into SDK parameters.
        """
        self.client.responses.create()
        pass
