"""Provider-neutral data exchanged during a model generation."""

from pydantic import BaseModel, Field


class GenerationRequest(BaseModel):
    """The input required to ask a specific provider model for a generation."""

    provider: str = Field(
        description="Identifier of the provider that should serve the request."
    )
    model: str = Field(description="Identifier of the provider model to request.")
    system_prompt: str = Field(
        description="Instructions that guide the model's behavior."
    )
    user_prompt: str = Field(description="The end user's message to the model.")


class GenerationResponse(BaseModel):
    """A provider-neutral result returned after a successful model generation."""

    provider: str = Field(
        description="Identifier of the provider that served the response."
    )
    model: str = Field(description="Identifier of the model that served the response.")
    text: str = Field(description="Generated response text.")
    total_tokens: int = Field(
        description="Total input and output tokens reported by the provider for the request."
    )
