# 📝 Text Summarization AI
A full-stack AI application that generates summaries from long text using NLP.

## 🚀 Features
- Summarize long articles instantly
- Adjustable summary length (min/max)
- Clean web interface using Streamlit
- FastAPI backend for scalable API

## 🛠 Tech Stack
- FastAPI (Backend)
- Streamlit (Frontend)
- HuggingFace Transformers (BART model)
- Python

## 📂 Project Structure
app/
 ├── main.py
 ├── preprocessing.py
 ├── schemas.py
 ├── summarizer.py
streamlit_app.py

## ▶️ How to Run

### 1. Clone repo
git clone https://github.com/your-username/text-summarization-ai.git

### 2. Create environment
python -m venv venv
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run backend
uvicorn app.main:app --reload

### 5. Run frontend
streamlit run streamlit_app.py
