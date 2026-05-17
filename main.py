from fastapi import FastAPI, HTTPException
from app.summarizer import TextSummarizer
from app.schemas import SummarizeRequest, SummarizeResponse, ModelInfoResponse

app = FastAPI(
    title="Text Summarization API",
    description="A simple API for generating summaries from input text.",
    version="1.0.0"
)

AVAILABLE_MODELS = [
    "facebook/bart-large-cnn"
]

DEFAULT_MODEL = "facebook/bart-large-cnn"

summarizer = TextSummarizer(model_name=DEFAULT_MODEL)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Text Summarization API"}


@app.get("/models", response_model=ModelInfoResponse)
def get_models():
    return ModelInfoResponse(
        available_models=AVAILABLE_MODELS,
        default_model=DEFAULT_MODEL
    )


@app.post("/summarize", response_model=SummarizeResponse)
def summarize_text(request: SummarizeRequest):
    try:
        if not request.text.strip():
            raise HTTPException(status_code=400, detail="Input text cannot be empty.")

        summary = summarizer.summarize(
            text=request.text,
            max_summary_length=request.max_summary_length,
            min_summary_length=request.min_summary_length
        )

        return SummarizeResponse(
            original_text=request.text,
            summary=summary
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))