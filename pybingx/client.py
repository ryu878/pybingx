import time
import requests
import hmac
from hashlib import sha256



def generate_signature(secret_key, payload):
    return hmac.new(secret_key.encode("utf-8"), payload.encode("utf-8"), sha256).hexdigest()

 
def get_timestamp():
    return str(int(time.time() * 1000))

class BingXClient:
    API_URL = "https://open-api.bingx.com"


    def __init__(self, api_key: str, secret_key: str):
        self.api_key = api_key
        self.secret_key = secret_key


    def get_contracts(self):
        path = '/openApi/swap/v2/quote/contracts'
        return self._send_request("GET", path, {})


    def get_depth(self, symbol: str, limit: int = 5):
        path = '/openApi/swap/v2/quote/depth'
        params = {
            "symbol": symbol,
            "limit": limit
        }
        return self._send_request("GET", path, params)


    def get_trades(self, symbol: str, limit: int = 10):
        path = '/openApi/swap/v2/quote/trades'
        params = {
            "symbol": symbol,
            "limit": limit
        }
        return self._send_request("GET", path, params)


    def get_premium_index(self, symbol: str):
        path = '/openApi/swap/v2/quote/premiumIndex'
        params = {
            "symbol": symbol
        }
        return self._send_request("GET", path, params)


    def get_funding_rate(self, symbol: str, limit: int = 2):
        path = '/openApi/swap/v2/quote/fundingRate'
        params = {
            "symbol": symbol,
            "limit": limit
        }
        return self._send_request("GET", path, params)


    def _send_request(self, method: str, path: str, params: dict):
        params_str = self._parse_params(params)
        signature = self._get_sign(params_str)
        url = f"{self.API_URL}{path}?{params_str}&signature={signature}"
        headers = {
            'X-BX-APIKEY': self.api_key,
        }
        response = requests.request(method, url, headers=headers)
        return response.json()


    def _get_sign(self, payload: str) -> str:
        return hmac.new(self.secret_key.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()


    def _parse_params(self, params: dict) -> str:
        sorted_keys = sorted(params)
        params_str = "&".join([f"{key}={params[key]}" for key in sorted_keys])
        timestamp = f"timestamp={int(time.time() * 1000)}"
        return f"{params_str}&{timestamp}" if params_str else timestamp


    def get_klines(self, symbol: str, interval: str, limit: int = 1000, start_time: int = None) -> dict:
        path = '/openApi/swap/v3/quote/klines'
        params = {"symbol": symbol, "interval": interval, "limit": limit}
        if start_time:
            params["startTime"] = start_time
        return self._send_request("GET", path, params)


    def get_open_interest(self, symbol: str) -> dict:
        path = '/openApi/swap/v2/quote/openInterest'
        params = {
            "symbol": symbol
        }
        return self._send_request("GET", path, params)
    

    def get_24hr_ticker_price_change(self, symbol: str = None) -> dict:
        path = '/openApi/swap/v2/quote/ticker'
        params = {}
        if symbol:
            params["symbol"] = symbol
        return self._send_request("GET", path, params)

 
    def get_historical_trades(self, symbol: str, from_id: str = None, limit: int = 500, recv_window: int = None) -> dict:
        path = '/openApi/swap/v1/market/historicalTrades'
        params = {
            "symbol": symbol,
            "limit": limit
        }
        if from_id:
            params["fromId"] = from_id
        if recv_window:
            params["recvWindow"] = recv_window
        return self._send_request("GET", path, params)


    def get_symbol_order_book_ticker(self, symbol: str) -> dict:
        path = '/openApi/swap/v2/quote/bookTicker'
        params = {
            "symbol": symbol
        }
        return self._send_request("GET", path, params)
    

    def get_mark_price_klines(self, symbol: str, interval: str, limit: int = 1000, start_time: int = None) -> dict:
        path = '/openApi/swap/v1/market/markPriceKlines'
        params = {
            "symbol": symbol,
            "interval": interval,
            "limit": limit
        }
        if start_time:
            params["startTime"] = start_time
        return self._send_request("GET", path, params)


    def get_symbol_price_ticker(self, symbol: str = None) -> dict:
        path = '/openApi/swap/v1/ticker/price'
        params = {}
        if symbol:
            params["symbol"] = symbol
        return self._send_request("GET", path, params)
    
    
    def get_user_balance(self) -> dict:
        path = '/openApi/swap/v3/user/balance'
        params = {}
        return self._send_request("GET", path, params)

  
    def get_positions(self, symbol: str = None, recv_window: int = None) -> dict:
        path = '/openApi/swap/v2/user/positions'
        params = {}
        if symbol:
            params["symbol"] = symbol
        if recv_window:
            params["recvWindow"] = recv_window
        return self._send_request("GET", path, params)
    
    
    def _send_request(self, method: str, path: str, params: dict):
        params_str = self._parse_params(params)
        signature = generate_signature(self.secret_key, params_str)
        url = f"{self.API_URL}{path}?{params_str}&signature={signature}"
        headers = {
            'X-BX-APIKEY': self.api_key,
        }
        response = requests.request(method, url, headers=headers)
        return response.json()


    def _parse_params(self, params: dict) -> str:
        sorted_keys = sorted(params)
        params_str = "&".join([f"{key}={params[key]}" for key in sorted_keys])
        timestamp = f"timestamp={get_timestamp()}"
        return f"{params_str}&{timestamp}" if params_str else timestamp
