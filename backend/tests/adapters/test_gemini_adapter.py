from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from positivity_ai.adapters.gemini.adapter import GeminiAdapter
from positivity_ai.generation.errors import GenerationException
from positivity_ai.generation.types import GenerationRequest, Message


@pytest.fixture
def generation_request() -> GenerationRequest:
    return GenerationRequest(
        provider="gemini",
        model="gemini-2.5-flash",
        system_prompt="Respond with encouragement.",
        messages=[Message(role="user", content="I could use some encouragement.")],
    )


@pytest.fixture
def client() -> Mock:
    return Mock(provider="google")


@pytest.fixture
def adapter(client: Mock) -> GeminiAdapter:
    adapter = object.__new__(GeminiAdapter)
    adapter.client = client
    return adapter


def test_generate_normalizes_gemini_response(
    adapter: GeminiAdapter, client: Mock, generation_request: GenerationRequest
) -> None:
    client.create_response.return_value = SimpleNamespace(
        output_text="You are building valuable skills.",
        model="gemini-2.5-flash-001",
        usage=SimpleNamespace(total_tokens=19),
    )

    response = adapter.generate(generation_request)

    assert response.provider == "google"
    assert response.model == "gemini-2.5-flash-001"
    assert response.message.content == "You are building valuable skills."
    assert response.total_tokens == 19
    client.create_response.assert_called_once_with(generation_request)


def test_generate_uses_requested_model_when_gemini_response_model_is_missing(
    adapter: GeminiAdapter, client: Mock, generation_request: GenerationRequest
) -> None:
    client.create_response.return_value = SimpleNamespace(
        output_text="Keep experimenting.",
        model=None,
        usage=SimpleNamespace(total_tokens=11),
    )

    response = adapter.generate(generation_request)

    assert response.model == generation_request.model


def test_generate_raises_when_gemini_returns_no_text(
    adapter: GeminiAdapter, client: Mock, generation_request: GenerationRequest
) -> None:
    client.create_response.return_value = SimpleNamespace(output_text=None)

    with pytest.raises(GenerationException, match="Gemini returned no text output."):
        adapter.generate(generation_request)
