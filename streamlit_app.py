import os

import cohere
import streamlit as st

# ---------------------------------------------------------------
# Change these three lines to make the chatbot your own.
# ---------------------------------------------------------------

TITLE = "💬 My First Chatbot"
GREETING = "How can I help you?"
INSTRUCTIONS = "You are a friendly helper. Answer in two or three sentences."

# ---------------------------------------------------------------
# You do not need to change anything below this line yet.
# Streamlit runs this whole file again each time a message is sent.
# ---------------------------------------------------------------

st.title(TITLE)

# The key comes from CO_API_KEY: a secret on Streamlit Community Cloud,
# or a line in ~/.zshrc on your Mac. Never type the key into this file.
if "CO_API_KEY" not in os.environ:
    st.error("No Cohere key found. Add CO_API_KEY as a secret, then reboot the app.")
    st.stop()

co = cohere.ClientV2()

# The conversation so far, kept from one run to the next.
# The system message holds your instructions for the whole conversation.
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": INSTRUCTIONS},
        {"role": "assistant", "content": GREETING},
    ]

# Show every message except the system message.
for message in st.session_state.messages:
    if message["role"] != "system":
        st.chat_message(message["role"]).write(message["content"])

# When a message is sent: show it, send the whole conversation, show the reply.
prompt = st.chat_input("Type a message")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    reply = co.chat(model="command-a-03-2025", messages=st.session_state.messages)
    text = reply.message.content[0].text

    st.session_state.messages.append({"role": "assistant", "content": text})
    st.chat_message("assistant").write(text)
