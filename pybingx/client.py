import requests
import hmac
from hashlib import sha256
from pybingx.utils import generate_signature, get_timestamp

class BingXClient:
    def __init__(self, api_key, secret_key):
        self.api_url = "https://open-api.bingx.com"
        self.api_key = api_key
        self.secret_key = secret_key

    def _send_request(self, path, method="GET", params=None):
        if params is None:
            params = {}

        params["timestamp"] = get_timestamp()
        query_string = "&".join([f"{k}={v}" for k, v in sorted(params.items())])
        signature = generate_signature(self.secret_key, query_string)
        url = f"{self.api_url}{path}?{query_string}&signature={signature}"

        headers = {"X-BX-APIKEY": self.api_key}
        response = requests.request(method, url, headers=headers)

        return response.json()

    def get_contracts(self):
        return self._send_request("/openApi/swap/v2/quote/contracts")

    def get_depth(self, symbol, limit=5):
        return self._send_request("/openApi/swap/v2/quote/depth", params={"symbol": symbol, "limit": limit})

    def get_trades(self, symbol, limit=10):
        return self._send_request("/openApi/swap/v2/quote/trades", params={"symbol": symbol, "limit": limit})

    def get_premium_index(self, symbol):
        return self._send_request("/openApi/swap/v2/quote/premiumIndex", params={"symbol": symbol})
