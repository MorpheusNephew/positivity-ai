from typing import Protocol

from positivity_ai.generation import GenerationRequest, GenerationResponse


class ModelAdapter(Protocol):
    def generate(self, request: GenerationRequest) -> GenerationResponse: ...
