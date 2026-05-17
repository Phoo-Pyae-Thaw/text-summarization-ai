from transformers import pipeline
from app.preprocessing import preprocess_text

class TextSummarizer:
    def __init__(self, model_name: str = "facebook/bart-large-cnn"):
        self.model_name = model_name
        self.summarizer = pipeline("summarization", model=model_name)

    def summarize(
        self,
        text: str,
        max_input_words: int = 500,
        max_summary_length: int = 130,
        min_summary_length: int = 30
    ) -> str:
        processed_text = preprocess_text(text, max_words=max_input_words)

        result = self.summarizer(
            processed_text,
            max_length=max_summary_length,
            min_length=min_summary_length,
            do_sample=False
        )

        return result[0]["summary_text"]

if __name__ == "__main__":
    summarizer = TextSummarizer()

    text = """
    Big data refers to the large volume of structured and unstructured data generated
every day. As artificial intelligence becomes more advanced, ethical concerns are
becoming more important. Issues such as data privacy, algorithm bias, and job
displacement need to be carefully managed. Governments and organizations must work
together to ensure AI is used responsibly and fairly. Organizations use big data analytics
to uncover hidden patterns, correlations, and insights that can improve decision-making.
With the help of technologies such as machine learning and data mining, companies can
gain a competitive advantage and better understand customer behavior.
    """

    summary = summarizer.summarize(text)

    print("Generated Summary:")
    print(summary)