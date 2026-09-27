from unittest.mock import Mock

import pytest

import positivity_ai.clients.openai.client as openai_client_module
from positivity_ai.clients.openai.client import OpenAIClient
from positivity_ai.generation.errors import GenerationException
from positivity_ai.generation.types import GenerationRequest, Message


@pytest.fixture
def generation_request() -> GenerationRequest:
    return GenerationRequest(
        provider="openai",
        model="gpt-4.1-mini",
        system_prompt="Respond with encouragement.",
        messages=[Message(role="user", content="I could use some encouragement.")],
    )


def test_create_response_translates_shared_request(
    generation_request: GenerationRequest,
) -> None:
    sdk_client = Mock()
    sdk_response = Mock()
    sdk_client.responses.create.return_value = sdk_response
    client = OpenAIClient(sdk_client)

    response = client.create_response(generation_request)

    assert response is sdk_response
    sdk_client.responses.create.assert_called_once_with(
        input=generation_request.messages,
        model="gpt-4.1-mini",
        instructions="Respond with encouragement.",
    )


def test_create_response_normalizes_sdk_errors(
    monkeypatch: pytest.MonkeyPatch, generation_request: GenerationRequest
) -> None:
    class FakeSDKError(Exception):
        pass

    monkeypatch.setattr(openai_client_module, "APIConnectionError", FakeSDKError)
    sdk_client = Mock()
    sdk_client.responses.create.side_effect = FakeSDKError("connection failed")
    client = OpenAIClient(sdk_client)

    with pytest.raises(GenerationException, match="connection failed") as error:
        client.create_response(generation_request)

    assert isinstance(error.value.__cause__, FakeSDKError)
