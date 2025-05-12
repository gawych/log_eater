EXCLUDE_PATTERNS = [re.compile(r'INFO'), re.compile(r'Debug')]
def flatten_streams(raw):
    flat=[]
    for s in raw.get("data",{}).get("result",[]):
        lbl = s["stream"]
        for ts,line in s["values"]:
            if any(p.search(line) for p in EXCLUDE_PATTERNS):
                continue
            flat.append({"ts":ts,"labels":lbl,"line":line})
    return flat[-500:]
