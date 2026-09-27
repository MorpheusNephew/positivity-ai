from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from positivity_ai.adapters.openai.adapter import OpenAIAdapter
from positivity_ai.generation.errors import GenerationException
from positivity_ai.generation.types import GenerationRequest, Message


@pytest.fixture
def generation_request() -> GenerationRequest:
    """Provide one provider-neutral request for adapter tests."""
    return GenerationRequest(
        provider="openai",
        model="gpt-4.1-mini",
        system_prompt="Respond with encouragement.",
        messages=[Message(role="user", content="I could use some encouragement.")],
    )


@pytest.fixture
def client() -> Mock:
    """Provide a fake client so tests never call the OpenAI API."""
    return Mock(provider="openai")


@pytest.fixture
def adapter(client: Mock) -> OpenAIAdapter:
    """Create an adapter with the fake client injected directly."""
    adapter = object.__new__(OpenAIAdapter)
    adapter.client = client
    return adapter


def test_generate_normalizes_openai_response(
    adapter: OpenAIAdapter, client: Mock, generation_request: GenerationRequest
) -> None:
    client.create_response.return_value = SimpleNamespace(
        output_text="You are making steady progress.",
        model="gpt-4.1-mini-2026-01-01",
        usage=SimpleNamespace(total_tokens=24),
    )

    response = adapter.generate(generation_request)

    assert response.provider == "openai"
    assert response.model == "gpt-4.1-mini-2026-01-01"
    assert response.message.role == "assistant"
    assert response.message.content == "You are making steady progress."
    assert response.total_tokens == 24
    client.create_response.assert_called_once_with(generation_request)


def test_generate_uses_requested_model_when_response_model_is_missing(
    adapter: OpenAIAdapter, client: Mock, generation_request: GenerationRequest
) -> None:
    client.create_response.return_value = SimpleNamespace(
        output_text="Keep going.",
        model=None,
        usage=SimpleNamespace(total_tokens=10),
    )

    response = adapter.generate(generation_request)

    assert response.model == generation_request.model


def test_generate_raises_when_openai_returns_no_text(
    adapter: OpenAIAdapter, client: Mock, generation_request: GenerationRequest
) -> None:
    client.create_response.return_value = SimpleNamespace(output_text=None)

    with pytest.raises(GenerationException, match="OpenAI returned no text output."):
        adapter.generate(generation_request)
