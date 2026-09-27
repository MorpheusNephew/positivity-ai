import pytest

from positivity_ai.adapters.gemini.adapter import GeminiAdapter
from positivity_ai.adapters.manager import AdapterManager
from positivity_ai.adapters.openai.adapter import OpenAIAdapter


def test_get_available_providers_returns_registered_provider_names() -> None:
    assert AdapterManager.get_available_providers() == ["openai", "gemini"]


@pytest.mark.parametrize(
    ("provider", "expected_adapter"),
    [("openai", OpenAIAdapter), ("gemini", GeminiAdapter)],
)
def test_get_adapter_class_returns_registered_adapter(
    provider: str, expected_adapter: type
) -> None:
    assert AdapterManager.get_adapter_class(provider) is expected_adapter


def test_get_adapter_class_rejects_unsupported_provider() -> None:
    with pytest.raises(ValueError, match="ollama is an unsupported provider"):
        AdapterManager.get_adapter_class("ollama")
