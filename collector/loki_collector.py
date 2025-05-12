import requests
import yaml

class LokiCollector:
    def __init__(self, config_file="config.yaml"):
        with open(config_file, "r") as f:
            self.config = yaml.safe_load(f)
        self.loki_url = self.config["loki"]["url"]

    def query_logs(self, query, limit=100):
        params = {
            "query": query,
            "limit": limit
        }
        response = requests.get(f"{self.loki_url}/loki/api/v1/query", params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to query Loki: {response.status_code} {response.text}")

if __name__ == "__main__":
    collector = LokiCollector()
    result = collector.query_logs('{job="varlogs"}', limit=10)
    print(result)
