import requests
import os

PROM_URL = os.getenv("PROMETHEUS_URL", "http://prometheus:9090")


def query(promql: str) -> float:
    resp = requests.get(
        f"{PROM_URL}/api/v1/query",
        params={"query": promql},
        timeout=3
    )
    resp.raise_for_status()
    data = resp.json()["data"]["result"]
    if not data:
        return 0.0
    return float(data[0]["value"][1])
