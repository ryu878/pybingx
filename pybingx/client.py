import requests
from .utils import get_signature, parse_params


class BingXClient:
    API_URL = "https://open-api.bingx.com"

    def __init__(self, api_key: str, secret_key: str):
        self.api_key = api_key
        self.secret_key = secret_key

    def send_request(self, method: str, path: str, params: dict = None, payload: dict = None) -> dict:
        """Send an HTTP request to the BingX API."""
        if params is None:
            params = {}
        if payload is None:
            payload = {}

        params_str = parse_params(params)
        signature = get_signature(self.secret_key, params_str)
        url = f"{self.API_URL}{path}?{params_str}&signature={signature}"

        headers = {"X-BX-APIKEY": self.api_key}
        response = requests.request(method, url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()

    def get_contracts(self) -> dict:
        """Fetch contract details."""
        path = "/openApi/swap/v2/quote/contracts"
        return self.send_request("GET", path)

    def get_depth(self, symbol: str, limit: int = 5) -> dict:
        """Fetch depth information for a specific symbol."""
        path = "/openApi/swap/v2/quote/depth"
        params = {"symbol": symbol, "limit": str(limit)}
        return self.send_request("GET", path, params)

    def get_trades(self, symbol: str, limit: int = 10) -> dict:
        """Fetch recent trades for a specific symbol."""
        path = "/openApi/swap/v2/quote/trades"
        params = {"symbol": symbol, "limit": str(limit)}
        return self.send_request("GET", path, params)
