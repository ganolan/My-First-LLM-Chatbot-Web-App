# My First LLM Chatbot

A chatbot in a web page, built with [Cohere](https://cohere.com) and [Streamlit](https://streamlit.io).

Follow [How to Build and Deploy a Streamlit Chatbot](https://ganolan.github.io/concept-library/tutorials/build-and-deploy-a-streamlit-chatbot/) to fork it, run it on your Mac, and publish it on Streamlit Community Cloud. It needs Python and a Cohere key first: [How to Set Up Python and a Cohere Key](https://ganolan.github.io/concept-library/tutorials/set-up-python-and-a-cohere-key/).

## Run it on your Mac

In Terminal, in this folder:

```
pip3 install -r requirements.txt
python3 -m streamlit run chatbot.py
```

The chatbot opens in your browser. Press Control-C in Terminal to stop it.

> [!CAUTION]
> Never type your Cohere key into `chatbot.py` or any file you push to GitHub. Anyone who copies it can use Cohere as you. The app reads the key from `CO_API_KEY`: set it in Terminal on your Mac, and as a secret on Streamlit Community Cloud.

## Make it your own

- Change the system message in `chatbot.py`, and see how the replies change.
- Change the title and the first message.
- Read [Streamlit's basic concepts](https://docs.streamlit.io/get-started/fundamentals/main-concepts) to add more to the page.
