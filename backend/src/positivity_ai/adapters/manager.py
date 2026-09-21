"""Select registered adapter classes by provider identifier."""

from positivity_ai.adapters.gemini.adapter import GeminiAdapter
from positivity_ai.adapters.model_adapter import ModelAdapter
from positivity_ai.adapters.openai.adapter import OpenAIAdapter


class AdapterManager:
    """Maps provider identifiers to adapter classes for later construction."""

    #: Provider identifiers mapped to adapter classes for caller-managed construction.
    _adapter_classes = {"openai": OpenAIAdapter, "gemini": GeminiAdapter}

    @staticmethod
    def get_available_providers() -> list[str]:
        """Return a new list of provider identifiers available for selection."""
        return list(AdapterManager._adapter_classes)

    @staticmethod
    def get_adapter_class(provider: str) -> type[ModelAdapter]:
        """Return the adapter class registered for ``provider``."""
        adapter_class = AdapterManager._adapter_classes.get(provider)

        if adapter_class is not None:
            return adapter_class

        raise ValueError(f"{provider} is an unsupported provider")
