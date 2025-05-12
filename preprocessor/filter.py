import re

# Логічніше лишити тільки DEBUG/TRACE, а INFO поки залишити
EXCLUDE = [re.compile(r'DEBUG', re.I), re.compile(r'TRACE', re.I)]

def flatten_streams(raw):
    flat = []
    for stream in raw.get("data", {}).get("result", []):
        for _, line in stream["values"]:
            if any(p.search(line) for p in EXCLUDE):
                continue
            flat.append(line)
    return flat[-300:]
