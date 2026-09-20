"""Thin wrapper around the OpenAI Python SDK."""

from openai import (
    OpenAI,
    APIConnectionError,
    APITimeoutError,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    InternalServerError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    UnprocessableEntityError,
)
from os import getenv

from positivity_ai.generation import GenerationRequest, GenerationException


class OpenAIClient:
    """Executes OpenAI SDK calls used by ``OpenAIAdapter``."""

    #: Configured OpenAI SDK client.
    client: OpenAI

    def __init__(self, client: OpenAI):
        """Wrap an initialized OpenAI SDK client."""

        self.client = client

    def get_models_list(self) -> list[str]:
        """Return model IDs visible to the configured OpenAI credential."""
        list_of_models = self.client.models.list()

        list_of_models = [model.id for model in list_of_models]

        return list_of_models

    def create_response(self, request: GenerationRequest):
        """Translate ``request`` into an OpenAI Responses API call."""
        try:

            return self.client.responses.create(
                input=request.messages,
                model=request.model,
                instructions=request.system_prompt,
            )

        except (
            APIConnectionError,
            APITimeoutError,
            AuthenticationError,
            BadRequestError,
            ConflictError,
            InternalServerError,
            NotFoundError,
            PermissionDeniedError,
            RateLimitError,
            UnprocessableEntityError,
        ) as error:
            raise GenerationException(str(error)) from error
