import httpx


class DetaMetrics:
    def __init__(self, urlId: str, apiKey: str) -> None:
        self.url = f"https://{urlId}.deta.app"
        self.__apiKey = apiKey
        self.__headers = {
            "User-Agent": "DetaMetrics",
            "X-Space-App-Key": self.__apiKey,
        }
        print(f"Using DetaMetrics Server at {self.url}")

    def __repr__(self) -> str:
        return f"<DetaMetrics url={self.url}>"

    def __str__(self) -> str:
        return f"DetaMetrics(url={self.url})"

    def set(self, graph: str, metric: str, value: float) -> None:
        httpx.get(f"{self.url}/set/{graph}/{metric}/{value}", headers=self.__headers)

    def clear(self) -> None:
        httpx.get(f"{self.url}/clear", headers=self.__headers)
