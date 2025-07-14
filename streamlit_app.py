import streamlit as st
import requests

# Set Hugging Face Inference API endpoint and key
API_URL = "https://api-inference.huggingface.co/models/bigcode/starcoder"
headers = {
    "Authorization": f"Bearer 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"
}

def query(prompt):
    payload = {"inputs": prompt}
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        result = response.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        elif isinstance(result, dict) and "error" in result:
            return f"Error from model: {result['error']}"
        else:
            return "Unknown response format."
    except Exception as e:
        return f"Request failed: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="Prompt-to-Code Generator", layout="centered")
st.title("💻 Prompt to Code Generator (Hugging Face API)")

prompt = st.text_area("Enter your prompt to generate code:", height=150)

if st.button("Generate Code"):
    if not prompt.strip():
        st.warning("Please enter a prompt first.")
    else:
        with st.spinner("Generating code..."):
            output = query(prompt)
            if output.startswith("Error") or output.startswith("Request failed"):
                st.error(output)
            else:
                st.code(output, language="python")
                st.download_button("Download Code", output, file_name="generated_code.py")
