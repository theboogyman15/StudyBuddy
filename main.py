import ollama
from dotenv import load_dotenv
import os
import gradio as gr

load_dotenv(override=True)
model = os.getenv("MODEL_NAME")
system = os.getenv("SYSTEM_PROMPT")

def chat(message, history):
    formatted_history = [
        {"role": h["role"], "content": h["content"] if isinstance(h["content"], str) else h["content"][0]["text"]}
        for h in history
    ]
    all_messages = [{"role": "system", "content": system}] + formatted_history + [{"role": "user", "content": message}]
    response = ollama.chat(model=model, messages=all_messages)
    return response["message"]["content"]


gr.ChatInterface(
    fn=chat,
    title="Ollama Chat",
    description="Chat with Ollama"
).launch()