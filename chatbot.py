import os

import cohere
import streamlit as st

# My First Chatbot: a Cohere chatbot in a Streamlit web page.
# Streamlit runs this whole file again every time the user sends a message.

st.title("💬 My First Chatbot")

# The key comes from CO_API_KEY: set in Terminal on your Mac, and as a secret
# on Streamlit Community Cloud. Never type the key into this file.
if "CO_API_KEY" not in os.environ:
    st.error("No Cohere key found. Set CO_API_KEY, then run the app again.")
    st.stop()

co = cohere.ClientV2()

# The conversation so far. session_state keeps it from one run to the next.
# The system message holds the instructions for the whole conversation.
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a friendly helper. Answer in two or three sentences."},
        {"role": "assistant", "content": "How can I help you?"},
    ]

# Show every message except the system message.
for message in st.session_state.messages:
    if message["role"] != "system":
        st.chat_message(message["role"]).write(message["content"])

# When the user sends a message: add it, send the whole conversation, and add the reply.
prompt = st.chat_input("Type a message")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    reply = co.chat(model="command-a-03-2025", messages=st.session_state.messages)
    text = reply.message.content[0].text

    st.session_state.messages.append({"role": "assistant", "content": text})
    st.chat_message("assistant").write(text)
