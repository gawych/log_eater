from collector.loki_collector import LokiCollector

if __name__ == "__main__":
    collector = LokiCollector()
    logs = collector.query_logs('{job="minecraft"}', limit=10)
    print(logs)
