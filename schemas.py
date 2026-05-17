from pydantic import BaseModel

class SummarizeRequest(BaseModel):
  text: str
  max_summary_length: int = 130
  min_summary_length: int = 30

class SummarizeResponse(BaseModel):
  original_text: str
  summary: str

class ModelInfoResponse(BaseModel):
  available_model: list[str]
  default_model: str