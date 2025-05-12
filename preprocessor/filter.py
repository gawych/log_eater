import re
EXCLUDE = [re.compile(r'INFO')]

def flatten_streams(raw):
    flat = []
    for stream in raw.get("data", {}).get("result", []):
        for ts, line in stream["values"]:
            if any(p.search(line) for p in EXCLUDE):
                continue
            flat.append(line)
    # беремо останні 300 рядків, щоб LLM не захлинувся
    return flat[-300:]
