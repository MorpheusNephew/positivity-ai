from unittest.mock import Mock

import pytest

import positivity_ai.clients.manager as client_manager_module
from positivity_ai.clients.manager import ClientManager


@pytest.mark.parametrize(
    ("factory_name", "sdk_constructor_name", "wrapper_name", "environment_variable"),
    [
        ("_get_openai_client", "OpenAI", "OpenAIClient", "OPENAI_API_KEY"),
        ("_get_google_genai_client", "GenAIClient", "GoogleGenAIClient", "GEMINI_API_KEY"),
    ],
)
def test_client_factories_use_provider_environment_keys(
    monkeypatch: pytest.MonkeyPatch,
    factory_name: str,
    sdk_constructor_name: str,
    wrapper_name: str,
    environment_variable: str,
) -> None:
    monkeypatch.setenv(environment_variable, "environment-key")
    sdk_client = Mock()
    sdk_constructor = Mock(return_value=sdk_client)
    wrapper = Mock()
    monkeypatch.setattr(client_manager_module, sdk_constructor_name, sdk_constructor)
    monkeypatch.setattr(client_manager_module, wrapper_name, wrapper)

    result = getattr(ClientManager, factory_name)()

    sdk_constructor.assert_called_once_with(api_key="environment-key")
    wrapper.assert_called_once_with(sdk_client)
    assert result is wrapper.return_value


def test_client_factory_prefers_explicit_api_key(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "environment-key")
    sdk_constructor = Mock()
    monkeypatch.setattr(client_manager_module, "OpenAI", sdk_constructor)
    monkeypatch.setattr(client_manager_module, "OpenAIClient", Mock())

    ClientManager._get_openai_client("explicit-key")

    sdk_constructor.assert_called_once_with(api_key="explicit-key")


def test_get_client_dispatches_to_registered_factory(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    factory = Mock(return_value=Mock())
    monkeypatch.setitem(client_manager_module._CLIENT_FACTORIES, "openai", factory)

    result = ClientManager.get_client("openai", "api-key")

    factory.assert_called_once_with("api-key")
    assert result is factory.return_value


def test_get_client_rejects_unsupported_client() -> None:
    with pytest.raises(ValueError, match="'unsupported' is an unsupported client"):
        ClientManager.get_client("unsupported")
