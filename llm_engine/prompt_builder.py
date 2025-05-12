SYSTEM_PROMPT = """
You are DevOps Log Analyst AI.
Identify anomalies, errors, or suspicious patterns.
Suggest probable root causes and next steps.
Respond in concise bullet points.
"""

def build_prompt(lines):
    snippet = "\n".join(l["line"][:400] for l in lines)
    return SYSTEM_PROMPT + "\n\nLogs:\n" + snippet