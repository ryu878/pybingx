import time
import requests
import hmac
from hashlib import sha256


class BingXClient:
    API_URL = "https://open-api.bingx.com"

    def __init__(self, api_key: str, secret_key: str):
        self.api_key = api_key
        self.secret_key = secret_key

    def _get_signature(self, payload: str) -> str:
        """Generate HMAC signature for authentication."""
        return hmac.new(self.secret_key.encode("utf-8"), payload.encode("utf-8"), sha256).hexdigest()

    def _build_url(self, path: str, params: dict) -> str:
        """Build the complete request URL with parameters and signature."""
        params_str = self._parse_params(params)
        signature = self._get_signature(params_str)
        return f"{self.API_URL}{path}?{params_str}&signature={signature}"

    def _parse_params(self, params: dict) -> str:
        """Convert dictionary to URL-encoded query string."""
        params["timestamp"] = str(int(time.time() * 1000))
        sorted_params = "&".join(f"{key}={params[key]}" for key in sorted(params))
        return sorted_params

    def send_request(self, method: str, path: str, params: dict = None, payload: dict = None) -> dict:
        """Send an HTTP request to the BingX API."""
        if params is None:
            params = {}
        if payload is None:
            payload = {}

        url = self._build_url(path, params)
        headers = {"X-BX-APIKEY": self.api_key}

        response = requests.request(method, url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()

    def get_contracts(self) -> dict:
        """Example API method to fetch contracts."""
        path = "/openApi/swap/v2/quote/contracts"
        return self.send_request("GET", path)
