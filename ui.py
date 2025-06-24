import streamlit as st
import requests

st.set_page_config(page_title="TerminalAI", page_icon="🖥️")
st.title("🖥️ TerminalAI")
st.caption("Convert natural language to terminal commands")

prompt = st.text_input("What do you want to do?", "")

if st.button("Generate Command"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Thinking..."):
            response = requests.post("http://localhost:8000/generate", json={"prompt": prompt})
            result = response.json()["command"]
            st.code(result, language="bash")
