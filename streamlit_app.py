import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"


st.set_page_config(page_title="Text Summarization AI", page_icon="📝")
st.title("📝 Text Summarization AI")
st.write("Enter a long text below and generate a summary using the FastAPI backend.")


text_input = st.text_area(
    "Enter your text",
    height=250,
    placeholder="Paste a long article or paragraph here..."
)

max_summary_length = st.slider(
    "Maximum Summary Length",
    min_value=30,
    max_value=200,
    value=130
)

min_summary_length = st.slider(
    "Minimum Summary Length",
    min_value=10,
    max_value=100,
    value=30
)


if st.button("Generate Summary"):
    if not text_input.strip():
        st.warning("Please enter some text before generating a summary.")
    else:
        payload = {
            "text": text_input,
            "max_summary_length": max_summary_length,
            "min_summary_length": min_summary_length
        }

        try:
            response = requests.post(f"{API_URL}/summarize", json=payload)

            if response.status_code == 200:
                result = response.json()

                st.subheader("Summary Result")
                st.success("Summary generated successfully.")

                st.write("**Original Text:**")
                st.write(result["original_text"])

                st.write("**Generated Summary:**")
                st.write(result["summary"])
            else:
                st.error(f"API Error: {response.status_code}")
                st.write(response.json())

        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the FastAPI backend. Please make sure the API server is running.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")