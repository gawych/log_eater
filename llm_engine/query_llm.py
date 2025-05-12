import os
from dotenv import load_dotenv
from openai import OpenAI, AsyncOpenAI  # 1.x API

load_dotenv()

BASE_URL = os.getenv("OPENAI_BASE_URL", "http://localhost:11434/v1")
API_KEY  = os.getenv("OPENAI_API_KEY", "ollama")   # будь-який рядок для Ollama
MODEL    = os.getenv("LLM_MODEL",      "mistral")

client = OpenAI(
    base_url = BASE_URL,
    api_key  = API_KEY,
)

def ask_llm(prompt: str) -> str:
    """Return model answer (sync)."""
    rsp = client.chat.completions.create(
        model       = MODEL,
        messages    = [{"role": "user", "content": prompt}],
        temperature = 0.2,
        max_tokens  = 300,
    )
    return rsp.choices[0].message.content.strip()
