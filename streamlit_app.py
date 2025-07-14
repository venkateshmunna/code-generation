import streamlit as st
import openai

# Set your OpenRouter API key here
openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"

st.title("Prompt to Code Generator")

prompt = st.text_area("Enter your prompt to generate code", height=150)

if st.button("Generate Code"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating code..."):
            try:
                response = openai.ChatCompletion.create(
                    model="openchat/openchat-3.5",  # You can change to other models too
                    messages=[
                        {"role": "user", "content": f"Write code for: {prompt}"}
                    ],
                    temperature=0.3
                )
                code = response['choices'][0]['message']['content']
                st.code(code, language="python")
                st.download_button("Download Code", code, file_name="generated_code.py")
                st.success("Code generated successfully!")
            except Exception as e:
                st.error(f"Error: {e}")
