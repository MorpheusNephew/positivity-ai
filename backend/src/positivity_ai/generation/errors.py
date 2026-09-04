class GenerationException(Exception):
    status_code: int
    status: str
    message: str
