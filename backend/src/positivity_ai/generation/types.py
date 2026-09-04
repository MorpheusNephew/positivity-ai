"""Provider-neutral data exchanged during a model generation."""

from typing import Literal

from pydantic import BaseModel, Field


class Message(BaseModel):
    """One user or assistant turn in a provider-neutral conversation."""

    role: Literal["user", "assistant"] = Field(
        description="Role of the participant that produced the message."
    )
    content: str = Field(description="Text content produced by the participant.")


class AssistantMessage(Message):
    """A message produced by the model in response to a generation request."""

    role: Literal["assistant"] = Field(
        default="assistant",
        description="Role of the generated message; defaults to the assistant.",
    )


class GenerationRequest(BaseModel):
    """The input required to ask a specific provider model for a generation."""

    provider: str = Field(
        description="Identifier of the provider that should serve the request."
    )
    model: str = Field(description="Identifier of the provider model to request.")
    system_prompt: str = Field(
        description="Instructions that guide the model's behavior."
    )
    messages: list[Message] = Field(
        description="Ordered user and assistant messages supplied as conversation context."
    )


class GenerationResponse(BaseModel):
    """A provider-neutral result returned after a successful model generation."""

    provider: str = Field(
        description="Identifier of the provider that served the response."
    )
    model: str = Field(description="Identifier of the model that served the response.")
    message: AssistantMessage = Field(
        description="New assistant message generated for the request."
    )
    total_tokens: int = Field(
        description="Total input and output tokens reported by the provider for the request."
    )
