import sys
from pathlib import Path
import streamlit as st

# Tambahkan folder backend ke python path
sys.path.append(str(Path(__file__).resolve().parent.parent / "backend"))

from gemini_service import ask_gemini

st.set_page_config(
    page_title="KostPrakhas AI",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 KostPrakhas AI")
st.caption("Customer Service Chatbot menggunakan Google Gemini")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Tanyakan tentang KostPrakhas...")

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    response = ask_gemini(prompt)

    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })
