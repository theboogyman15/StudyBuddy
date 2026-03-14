import ollama
from dotenv import load_dotenv 
import os
import gradio as gr

load_dotenv() 
model = os.getenv("MODEL_NAME")
System = os.getenv("SYSTEM_PROMPT")
