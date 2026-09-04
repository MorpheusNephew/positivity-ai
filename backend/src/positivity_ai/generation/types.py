from pydantic import BaseModel


class GenerationRequest(BaseModel):
    system_prompt: str
    user_prompt: str
    model: str


class GenerationResponse(BaseModel):
    pass
