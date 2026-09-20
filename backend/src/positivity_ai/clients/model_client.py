from typing import Protocol

from positivity_ai.generation.types import GenerationRequest


class ModelClient(Protocol):

    def get_models_list(self) -> list[str]: ...

    def create_response(self, request: GenerationRequest): ...
