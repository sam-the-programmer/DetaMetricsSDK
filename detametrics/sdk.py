import httpx

class DetaMetrics:
    def __init__(self, urlId: str) -> None:
        self.url = urlId + ".deta.app"

    def __repr__(self) -> str:
        return f"<DetaMetrics url={self.url}>"

    def __str__(self) -> str:
        return f"DetaMetrics(url={self.url})"

    def set(self, graph: str, metric: str, value: float) -> None:
        httpx.get(f"https://{self.url}/set/{graph}/{metric}/{value}")

    def clear(self, graph: str) -> None:
        httpx.get(f"https://{self.url}/clear")
