SYSTEM = """You are an AI DevOps assistant.
Given raw log lines, detect issues, anomalies and give concise bullet-point advice."""

def build_prompt(lines):
    snippet = "\n".join(lines)
    return f"{SYSTEM}\n\nLogs below:\n```\n{snippet}\n```"
