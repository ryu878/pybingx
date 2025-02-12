import time
import requests
import hmac
from hashlib import sha256
import json



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


    def get_account_profit_loss_flow(self, start_time: int = None, end_time: int = None, limit: int = 1000) -> dict:
        path = '/openApi/swap/v2/user/income'
        params = {
            "limit": limit
        }
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time
        return self._send_request("GET", path, params)

  
    def export_fund_flow(self, symbol: str, start_time: int = None, end_time: int = None, limit: int = 200, recv_window: int = None) -> bytes:
        path = '/openApi/swap/v2/user/income/export'
        params = {
            "symbol": symbol,
            "limit": limit
        }
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time
        if recv_window:
            params["recvWindow"] = recv_window
        return self._send_request("GET", path, params, return_binary=True)


    def get_trading_commission_rate(self, recv_window: int = None) -> dict:
        path = '/openApi/swap/v2/user/commissionRate'
        params = {}
        if recv_window:
            params["recvWindow"] = recv_window
        return self._send_request("GET", path, params)


    def place_order(
    self,
    symbol: str,
    side: str,
    position_side: str,
    order_type: str,
    quantity: float,
    price: float = None,
    time_in_force: str = None,
    stop_loss: dict = None,
    take_profit: dict = None,
    stop_guaranteed: bool = False,
    working_type: str = None,
    reduce_only: bool = False,
    price_protect: bool = False,
    callback_rate: float = None,
    recv_window: int = None
    ) -> dict:
        """
        Place an order on the BingX exchange.

        :param symbol: The trading pair symbol (e.g., "BTC-USDT").
        :param side: The order side ("BUY" or "SELL").
        :param position_side: The position side ("LONG" or "SHORT").
        :param order_type: The order type (e.g., "MARKET", "LIMIT").
        :param quantity: The quantity of the order.
        :param price: The price for limit orders (required for LIMIT orders).
        :param time_in_force: How long the order remains active (e.g., "GTC", "IOC").
        :param stop_loss: A dictionary containing stop-loss parameters.
        :param take_profit: A dictionary containing take-profit parameters.
        :param stop_guaranteed: Whether the stop-loss is guaranteed (default: False).
        :param working_type: The working type for stop orders ("MARK_PRICE" or "CONTRACT_PRICE").
        :param reduce_only: Whether the order is reduce-only (default: False).
        :param price_protect: Whether to enable price protection (default: False).
        :param callback_rate: The callback rate for trailing stop orders.
        :param recv_window: The receive window for the request (optional).
        :return: The response from the API.
        """
        path = '/openApi/swap/v2/trade/order'
        params = {
            "symbol": symbol,
            "side": side,
            "positionSide": position_side,
            "type": order_type,
            "quantity": quantity
        }

        # Add optional parameters
        if price:
            params["price"] = price
        if time_in_force:
            params["timeInForce"] = time_in_force
        if stop_loss:
            params["stopLoss"] = json.dumps(stop_loss)
        if take_profit:
            params["takeProfit"] = json.dumps(take_profit)
        if stop_guaranteed:
            params["stopGuaranteed"] = "true"
        if working_type:
            params["workingType"] = working_type
        if reduce_only:
            params["reduceOnly"] = "true"
        if price_protect:
            params["priceProtect"] = "true"
        if callback_rate:
            params["callbackRate"] = callback_rate
        if recv_window:
            params["recvWindow"] = recv_window

        return self._send_request("POST", path, params)

  
    def _send_request(self, method: str, path: str, params: dict, return_binary: bool = False):
        params_str = self._parse_params(params)
        signature = generate_signature(self.secret_key, params_str)
        url = f"{self.API_URL}{path}?{params_str}&signature={signature}"
        headers = {
            'X-BX-APIKEY': self.api_key,
        }
        if method == "POST":
            headers['Content-Type'] = 'application/json'
            response = requests.request(method, url, headers=headers, json=params)
        else:
            response = requests.request(method, url, headers=headers)
        if return_binary:
            return response.content  # Return binary content for file downloads
        return response.json()


    def _parse_params(self, params: dict) -> str:
        sorted_keys = sorted(params)
        params_str = "&".join([f"{key}={params[key]}" for key in sorted_keys])
        timestamp = f"timestamp={get_timestamp()}"
        return f"{params_str}&{timestamp}" if params_str else timestamp
