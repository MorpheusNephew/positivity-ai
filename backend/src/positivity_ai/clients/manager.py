"""Construct provider-specific SDK client wrappers by implementation name."""

from collections.abc import Callable
from os import getenv
from typing import Literal

from google.genai import Client as GenAIClient
from openai import OpenAI
from positivity_ai.clients.google_genai.client import GoogleGenAIClient
from positivity_ai.clients.model_client import ModelClient
from positivity_ai.clients.openai.client import OpenAIClient

ClientName = Literal["google_genai", "openai"]
#: Identifiers for concrete client implementations, rather than UI providers.

_ClientFactory = Callable[[str | None], ModelClient]
#: Function signature for constructing a configured provider client wrapper.


class ClientManager:
    """Build the client wrapper requested by an adapter."""

    @staticmethod
    def get_client(client_name: ClientName, api_key: str | None = None) -> ModelClient:
        """Return a configured client wrapper for ``client_name``.

        When ``api_key`` is omitted, the selected factory reads its provider's
        API-key environment variable.
        """
        factory = _CLIENT_FACTORIES.get(client_name)

        if factory is None:
            raise ValueError(f"{client_name!r} is an unsupported client.")

        return factory(api_key)

    @staticmethod
    def _get_google_genai_client(
        api_key: str | None = None,
    ) -> GoogleGenAIClient:
        """Create a Google Gen AI wrapper using an explicit key or ``GEMINI_API_KEY``."""
        api_key = api_key if api_key else getenv("GEMINI_API_KEY")

        client = GenAIClient(api_key=api_key)

        return GoogleGenAIClient(client)

    @staticmethod
    def _get_openai_client(api_key: str | None = None) -> OpenAIClient:
        """Create an OpenAI wrapper using an explicit key or ``OPENAI_API_KEY``."""
        api_key = api_key if api_key else getenv("OPENAI_API_KEY")

        client = OpenAI(api_key=api_key)

        return OpenAIClient(client)


# Maps stable implementation names to the functions that construct their wrappers.
_CLIENT_FACTORIES: dict[ClientName, _ClientFactory] = {
    "google_genai": ClientManager._get_google_genai_client,
    "openai": ClientManager._get_openai_client,
}
