import requests
import yaml
import time

class LokiCollector:
    def __init__(self, config_file="config.yaml"):
        with open(config_file, "r") as f:
            self.config = yaml.safe_load(f)
        self.loki_url = self.config["loki"]["url"]

    def query_logs(self, query, minutes=5, limit=500):
        now_ns   = int(time.time()*1e9)
        start_ns = now_ns - minutes*60*1_000_000_000
        params = {"query": query, "limit": limit,
                "start": start_ns, "end": now_ns}
        r = requests.get(f"{self.loki_url}/loki/api/v1/query_range", params=params)
        r.raise_for_status()
        return r.json()

if __name__ == "__main__":
    collector = LokiCollector()
    result = collector.query_logs('{job="varlogs"}', limit=10)
    print(result)
