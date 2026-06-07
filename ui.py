import streamlit as st
import requests

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="RAG Chatbot", layout="centered")

st.title("🤖 RAG Chatbot")
st.caption("Ask questions based on your documents")

API_URL = "http://127.0.0.1:8000/ask"

# -----------------------------
# Initialize chat history
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Display chat messages
# -----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# Chat input
# -----------------------------
prompt = st.chat_input("Ask your question...")

if prompt:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call FastAPI backend
    try:
        response = requests.post(
            API_URL,
            json={"question": prompt},
            timeout=300
        )

        if response.status_code == 200:
            data = response.json()
            answer = data.get("answer", "No answer returned.")

            # ✅ GPT-style clean reply (NO sources, NO confidence)
            reply = answer.strip()

        else:
            reply = f"❌ Backend error (status code: {response.status_code})"

    except Exception as e:
        reply = f"❌ Could not connect to backend.\n\n**Error:** `{e}`"

    # Show assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
    with st.chat_message("assistant"):
        st.markdown(reply)