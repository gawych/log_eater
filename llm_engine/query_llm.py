import os, openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key  = os.getenv("OPENAI_API_KEY", "ollama")
openai.api_base = os.getenv("OPENAI_BASE_URL", "http://localhost:11434/v1")
MODEL = os.getenv("LLM_MODEL", "mistral")

def ask_llm(prompt):
    rsp = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.2,
    )
    return rsp.choices[0].message.content.strip()
