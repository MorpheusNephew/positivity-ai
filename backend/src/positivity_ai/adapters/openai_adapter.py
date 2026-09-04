"""OpenAI implementation of the model adapter contract."""

from positivity_ai.generation import GenerationRequest, GenerationResponse


class OpenAIAdapter:
    """Adapter responsible for translating generation requests to OpenAI calls."""

    def generate(self, request: GenerationRequest) -> GenerationResponse:
        """Generate an OpenAI response for ``request``.

        This method is intentionally unimplemented while the OpenAI integration is
        being built.
        """
        pass
