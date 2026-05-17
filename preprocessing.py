import re

def clean_text(text: str) -> str:
    if not text:
        return ""
    
    text = text.lower()
    text = re.sub(r'(^|\.\s+)([a-z])', lambda m: m.group(1) + m.group(2).upper(), text)

    text = re.sub(r"[\n\r\t]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def truncate_text(text: str, max_words: int = 500) -> str:
    words = text.split()
    if len(words) <= max_words:
        return text
    return " ".join(words[:max_words])

def preprocess_text(text: str, max_words: int = 500) -> str:
    text = clean_text(text)
    text = truncate_text(text, max_words=max_words)
    return text

if __name__ == "__main__":
    sample_text = "aI Is GrOwInG FaSt.\nIt HELPS in Education, HEALTHCARE, and business."
    processed = preprocess_text(sample_text, max_words=20)
    print(processed)