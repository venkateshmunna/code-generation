
import streamlit as st
import requests

st.title("Free Prompt-to-Code Generator 🔓")

prompt = st.text_area("Enter your prompt to generate code", height=150)

API_URL = "https://api-inference.huggingface.co/models/Salesforce/codegen-350M-mono"
headers = {"Authorization": ""}  # No token for public inference

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

if st.button("Generate Code"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating..."):
            result = query({"inputs": prompt})
            try:
                code = result[0]['generated_text']
                st.code(code, language="python")
                st.download_button("Download Code", code, file_name="generated_code.py")
            except Exception as e:
                st.error("Error: Could not generate code. Please try again.")
