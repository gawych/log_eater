from collector.loki_collector import LokiCollector
from preprocessor.filter        import flatten_streams
from llm_engine.prompt_builder  import build_prompt
from llm_engine.query_llm       import ask_llm

QUERY = '{job="minecraft"}'

if __name__ == "__main__":
    coll  = LokiCollector()
    raw   = coll.query_logs(QUERY, minutes=10)
    lines = flatten_streams(raw)

    if not lines:
        print("No log lines found.")
        exit()

    print(f"Collected {len(lines)} lines")

    prompt = build_prompt(lines)
    answer = ask_llm(prompt)
    print("\n=== LLM SUGGESTION ===\n", answer)
