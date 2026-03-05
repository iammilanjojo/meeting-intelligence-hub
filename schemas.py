from pydantic import BaseModel

class TranscriptResponse(BaseModel):
    message: str
    filename: str