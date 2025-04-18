# PyBingX

A Python client for the BingX cryptocurrency exchange API. This package allows developers to seamlessly interact with the BingX API to fetch market data, manage trades, and perform other account operations.

## Features

- Fetch market contract details
- Get order book depth information
- Retrieve recent trades
- Fetch historical klines (candlestick data)
- Fetch open interest statistics
- Get 24hr ticker price change
- Get asset information of user‘s Perpetual Account of USDC and USDT
- Retrieve information on users' positions of Perpetual Swap
- Easy-to-use and extend
- Built-in HMAC signature generation for secure API requests
- Export fund flow as Excel file (3 month)

## Installation

To install `pybingx`, first clone the repository 

```
git clone git@github.com:ryu878/pybingx.git
```
and install it locally:


```bash
pip install -e .
```

## Getting Started

### Importing the Client

```python
from pybingx import BingXClient
```

### Example Usage

```python
from pybingx import BingXClient

api_key = "your_api_key"
secret_key = "your_secret_key"

client = BingXClient(api_key, secret_key)

Market Data

# 1. USDT-M Perp Futures symbols. 
# Fetch contract details
contracts = client.get_contracts()
print("Contracts:", contracts)

# 2. Order Book. 
# Fetch depth information
depth_info = client.get_depth("SHIB-USDT", limit=5)
print("Depth Info:", depth_info)

# 3. Recent Trades List. 
# Fetch recent trades
trades_info = client.get_trades("BTC-USDT", limit=10)
print("Recent Trades:", trades_info)

# 4. Mark Price and Funding Rate. 
# Fetch premium index
premium_index = client.get_premium_index("BTC-USDT")
print("Premium Index:", premium_index)

# 5. Get Funding Rate History. 
# Fetch funding rate history with time range
start_time = 1672531200000  # Example timestamp in milliseconds
end_time = 1672617600000    # Example timestamp in milliseconds
funding_rate_history = client.get_funding_rate_history("BTC-USDT", start_time=start_time, end_time=end_time, limit=5)
print("Funding Rate History:", funding_rate_history)

# 6. Kline/Candlestick Data. 
# Fetch historical klines (candlestick data)
klines = client.get_klines("BTC-USDT", interval="1h", limit=1000, start_time=1672531200000)
print("Klines:", klines)

# 7. Open Interest Statistics. 
# Fetch open interest statistics
open_interest = client.get_open_interest("EOS-USDT")
print("Open Interest:", open_interest)

# 8. 24hr Ticker Price Change Statistics. 
# Fetch 24hr ticker price change for a specific symbol
ticker_price_change = client.get_24hr_ticker_price_change("SFP-USDT")
print("24hr Ticker Price Change (SFP-USDT):", ticker_price_change)

# Fetch 24hr ticker price change for all symbols
all_ticker_price_changes = client.get_24hr_ticker_price_change()
print("24hr Ticker Price Change (All Symbols):", all_ticker_price_changes)

# 9. Query historical transaction orders. 
# Fetch historical trades for a specific symbol
historical_trades = client.get_historical_trades("ETH-USDT", from_id="412551", limit=500)
print("Historical Trades:", historical_trades)

# 10. Symbol Order Book Ticker. 
# Fetch order book ticker for a specific symbol
order_book_ticker = client.get_symbol_order_book_ticker("BTC-USDT")
print("Order Book Ticker:", order_book_ticker)

# 11. Mark Price Kline/Candlestick Data. 
# Fetch mark price klines for a specific symbol and interval
mark_price_klines = client.get_mark_price_klines("KNC-USDT", interval="1h", limit=1000, start_time=1702717199998)
print("Mark Price Klines:", mark_price_klines)

# 12. Symbol Price Ticker. 
# Fetch price ticker for a specific symbol
price_ticker = client.get_symbol_price_ticker("TIA-USDT")
print("Symbol Price Ticker:", price_ticker)

# Fetch price tickers for all symbols
all_price_tickers = client.get_symbol_price_ticker()
print("All Symbol Price Tickers:", all_price_tickers)

Account Endpoints

# 1. Query account data
# Fetch user balance
user_balance = client.get_user_balance()
print("User Balance:", user_balance)

# 2. Query position data
# Fetch positions for a specific symbol
positions = client.get_positions(symbol="BNB-USDT")
print("Positions:", positions)

# Fetch positions for all symbols
all_positions = client.get_positions()
print("All Positions:", all_positions)

# 3. Get Account Profit and Loss Fund Flow
# Fetch profit and loss fund flow with a time range
profit_loss_flow = client.get_account_profit_loss_flow(start_time=1702713615001, end_time=1702731787011, limit=1000)
print("Profit and Loss Fund Flow:", profit_loss_flow)

# 4. Export fund flow
# Export fund flow data for a specific symbol
fund_flow_data = client.export_fund_flow(symbol="BTC-USDT", start_time=1702449874964, limit=200)

# Save the Excel file to disk
with open("fund_flow.xlsx", "wb") as file:
    file.write(fund_flow_data)
print("Fund flow data exported to fund_flow.xlsx")

# 5. Query Trading Commission Rate
# Fetch trading commission rate
commission_rate = client.get_trading_commission_rate(recv_window=5000)
print("Trading Commission Rate:", commission_rate)

Trades Endpoints
# 1. Test Order
# Test Order

take_profit = {
    "type": "TAKE_PROFIT_MARKET",
    "stopPrice": 31968.0,
    "price": 31968.0,
    "workingType": "MARK_PRICE"
}

response = client.test_order(
    symbol="BTC-USDT",
    side="BUY",
    position_side="LONG",
    order_type="MARKET",
    quantity=5,
    take_profit=take_profit
)
print("Test Order Response:", response)

# 2. Place order
# Place order
take_profit = {
    "type": "TAKE_PROFIT_MARKET",
    "stopPrice": 32000.0,
    "price": 32000.0,
    "workingType": "MARK_PRICE"
}

stop_loss = {
    "type": "STOP_MARKET",
    "stopPrice": 31000.0,
    "price": 31000.0,
    "workingType": "MARK_PRICE"
}

order_response = client.place_order(
    symbol="BTC-USDT",
    side="BUY",
    position_side="LONG",
    order_type="MARKET",
    quantity=0.01,
    take_profit=take_profit,
    stop_loss=stop_loss,
    stop_guaranteed=True,
    working_type="MARK_PRICE",
    reduce_only=False,
    price_protect=True
)
print("Order Response:", order_response)

# Place Limit Order with Reduce-Only
order_response = client.place_order(
    symbol="BTC-USDT",
    side="SELL",
    position_side="SHORT",
    order_type="LIMIT",
    quantity=0.01,
    price=33000.0,
    time_in_force="GTC",
    reduce_only=True
)
print("Order Response:", order_response)

# Trailing Stop Order
order_response = client.place_order(
    symbol="BTC-USDT",
    side="BUY",
    position_side="LONG",
    order_type="TRAILING_STOP_MARKET",
    quantity=0.01,
    callback_rate=1.0,  # 1% trailing stop
    working_type="MARK_PRICE"
)
print("Order Response:", order_response)

# Place Multiple Orders
orders = [
    {
        "symbol": "ETH-USDT",
        "type": "MARKET",
        "side": "BUY",
        "positionSide": "LONG",
        "quantity": 1
    },
    {
        "symbol": "BTC-USDT",
        "type": "MARKET",
        "side": "BUY",
        "positionSide": "LONG",
        "quantity": 0.001
    }
]

response = client.place_batch_orders(orders)
print("Batch Orders Response:", response)

# Close All Positions for a Specific Symbol
response = client.close_all_positions(symbol="BTC-USDT")
print("Close All Positions Response:", response)

# Cancel Order
Cancel an order that the current account is in the current entrusted state.

The cancellation api is limited to one second and can only cancel the same orderId or clientOrderId. Please do not resubmit

response = client.cancel_order(symbol="RNDR-USDT", order_id="1736011869418901234")
print("Cancel Order Response:", response)

# Cancel Multiple Orders
order_ids = [1735924831603391122, 1735924833239172233]
response = client.cancel_batch_orders(symbol="BTC-USDT", order_id_list=order_ids)
print("Cancel Batch Orders Response:", response)

# Cancel All Open Orders for a Specific Symbol
response = client.cancel_all_open_orders(symbol="ATOM-USDT")
print("Cancel All Open Orders Response:", response)

# Cancel All Open Limit Orders for a Specific Symbol
response = client.cancel_all_open_orders(symbol="ATOM-USDT", order_type="LIMIT")
print("Cancel All Open Limit Orders Response:", response)

# Query All Open Orders for a Specific Symbol:
response = client.get_all_open_orders(symbol="BTC-USDT")
print("All Open Orders:", response)

# Query All Open Limit Orders for a Specific Symbol:
response = client.get_all_open_orders(symbol="BTC-USDT", order_type="LIMIT")
print("All Open Limit Orders:", response)

# Query Pending Order Status
response = client.get_pending_order_status(symbol="OP-USDT", order_id="1736012449498123456")
print("Pending Order Status:", response)

# Query Order Details
response = client.get_order_details(symbol="OP-USDT", order_id="1736012449498123456")
print("Order Details:", response)

# Query Margin Type
response = client.get_margin_type(symbol="WOO-USDT")
print("Margin Type:", response)

# Change Margin Type
response = client.change_margin_type("MINA-USDT", "CROSSED", recv_window=60000)
print("Change Margin Type Response:", response)

# Query Leverage and Available Positions
leverage_and_positions = client.get_leverage_and_positions("BCH-USDT")
print("Leverage and Available Positions:", leverage_and_positions)

# Set Leverage
response = client.set_leverage("ETH-USDT", leverage=8, side="SHORT")
print("Set Leverage Response:", response)

# User's Force Orders
force_orders = client.get_force_orders("ATOM-USDT", start_time=1696291200000)
print("Force Orders:", force_orders)

# Query Order History
order_history = client.get_order_history("PYTH-USDT", start_time=1702688795000, end_time=1702731995000, limit=500)
print("Order History:", order_history)

# Modify Isolated Position Margin
response = client.modify_isolated_position_margin("BTC-USDT", margin_type=1, amount=3, position_side="LONG", recv_window=10000)
print("Modify Isolated Position Margin Response:", response)

```

## Project Structure

```
pybingx/
├── __init__.py
├── client.py
└── utils.py
setup.py
```

### File Descriptions

- `client.py`: Contains the `BingXClient` class responsible for making API requests.
- `utils.py`: Provides utility functions for signing requests and handling query parameters.
- `setup.py`: Package setup file for project installation.

## Available Methods

### `get_contracts()`
Retrieve contract details for available trading pairs.

### `get_depth(symbol: str, limit: int)`
Fetch order book depth information for the specified trading pair.

### `get_trades(symbol: str, limit: int)`
Retrieve the most recent trades for a given trading pair.

### `get_premium_index(symbol: str)`
Fetch the premium index for a specific trading pair.

### `get_funding_rate_history(symbol: str, start_time: int, end_time: int, limit: int)`
Retrieve the funding rate history for a specific trading pair within a time range.

- If both `start_time` and `end_time` are not sent, the API returns the latest data within the `limit`.
- The returned list is sorted by time from smallest to largest.
- If the amount of data between `start_time` and `end_time` exceeds the `limit`, the API returns the data from `start_time` up to the `limit`.

### `get_klines(symbol: str, interval: str, limit: int, start_time: int)`
Fetch historical klines (candlestick data) for a specific trading pair.

    symbol: The trading pair symbol (e.g., "BTC-USDT").

    interval: The interval of the klines (e.g., "1h", "4h", "1d").

    limit: The maximum number of klines to retrieve (default is 1000).

    start_time: The start time for the klines in milliseconds (optional).

### `get_open_interest(symbol: str)`
Fetch open interest statistics for a specific trading pair.

    symbol: The trading pair symbol (e.g., "EOS-USDT").

### `get_24hr_ticker_price_change(symbol: str = None)`
Fetch 24-hour ticker price change statistics for a specific trading pair or all pairs if no symbol is provided.
    
    symbol: The trading pair symbol (e.g., "SFP-USDT"). If not provided, returns data for all trading pairs.

### `get_historical_trades(symbol: str, from_id: str = None, limit: int = 500, recv_window: int = None)`
Fetch historical transaction orders for a specific trading pair.

    symbol: The trading pair symbol (e.g., "ETH-USDT").
    from_id: The trade ID to start fetching historical trades from (optional).
    limit: The maximum number of trades to retrieve (default is 500).
    recv_window: The receive window for the request (optional).

### `get_symbol_order_book_ticker(symbol: str)`
Fetch the order book ticker for a specific trading pair.

    symbol: The trading pair symbol (e.g., "BTC-USDT").

### `get_mark_price_klines(symbol: str, interval: str, limit: int = 1000, start_time: int = None)`
Fetch mark price kline/candlestick data for a specific trading pair and interval.

    symbol: The trading pair symbol (e.g., "KNC-USDT").
    interval: The interval of the klines (e.g., "1h", "4h", "1d").
    limit: The maximum number of klines to retrieve (default is 1000).
    start_time: The start time for the klines in milliseconds (optional, e.g. 1702717199998).

### `get_symbol_price_ticker(symbol: str = None)`
Fetch the price ticker for a specific trading pair or all pairs if no symbol is provided.

    symbol: The trading pair symbol (e.g., "TIA-USDT"). If not provided, returns price tickers for all trading pairs.

### `get_user_balance()`
Fetch the user's balance.

### `get_positions(symbol: str = None, recv_window: int = None)`
Fetch position data for a specific trading pair or all pairs if no symbol is provided.

    symbol: The trading pair symbol (e.g., "BNB-USDT"). If not provided, returns positions for all trading pairs.
    recv_window: The receive window for the request (optional).

### `get_account_profit_loss_flow(start_time: int = None, end_time: int = None, limit: int = 1000)`
Fetch the profit and loss fund flow for the perpetual contract under the current account.

    start_time: The start time for the query in milliseconds (optional).
    end_time: The end time for the query in milliseconds (optional).
    limit: The maximum number of records to retrieve (default is 1000).

### `export_fund_flow(symbol: str, start_time: int = None, end_time: int = None, limit: int = 200, recv_window: int = None)`
Export the fund flow data as an Excel file, keeping only the last 3 months of data.

    symbol: The trading pair symbol (e.g., "BTC-USDT").
    start_time: The start time for the query in milliseconds (optional).
    end_time: The end time for the query in milliseconds (optional).
    limit: The maximum number of records to retrieve (default is 200).
    recv_window: The receive window for the request (optional).

### `get_trading_commission_rate(recv_window: int = None)`
Fetch the trading commission rate for the current user.

    recv_window: The receive window for the request (optional).

### `place_order(symbol: str, side: str, position_side: str, order_type: str, quantity: float, price: float = None, time_in_force: str = None, stop_loss: dict = None, take_profit: dict = None, stop_guaranteed: bool = False, working_type: str = None, reduce_only: bool = False, price_protect: bool = False, callback_rate: float = None, recv_window: int = None)`
Place an order on the BingX exchange.

Trading Rules:

Trading Rules: https://bingx.com/en/tradeInfo/perpetual/trading-rules/BTC-USDT/

About price accuracy and quantity accuracy reference interface: https://open-api.bingx.com/openApi/swap/v2/quote/contracts

If the accuracy exceeds the range of the current period, the current API order will still be successful, but it will be truncated. For example, the price requirement is: 0.0001, if the order is 0.123456, it will be successfully submitted with 0.1234.

    symbol: The trading pair symbol (e.g., "BTC-USDT").
    side: The order side ("BUY" or "SELL").
    position_side: The position side ("LONG" or "SHORT").
    order_type: The order type (e.g., "MARKET", "LIMIT", "TRAILING_STOP_MARKET").
    quantity: The quantity of the order.
    price: The price for limit orders (required for LIMIT orders).
    time_in_force: How long the order remains active (e.g., "GTC", "IOC").
    stop_loss: A dictionary containing stop-loss parameters.
    take_profit: A dictionary containing take-profit parameters.
    stop_guaranteed: Whether the stop-loss is guaranteed (default: False).
    working_type: The working type for stop orders ("MARK_PRICE" or "CONTRACT_PRICE").
    reduce_only: Whether the order is reduce-only (default: False).
    price_protect: Whether to enable price protection (default: False).
    callback_rate: The callback rate for trailing stop orders.
    recv_window: The receive window for the request (optional).

### `place_batch_orders(orders: list, recv_window: int = None)`
Place multiple orders in a single request.

    orders: A list of order dictionaries. Each dictionary should contain:
    symbol: The trading pair symbol (e.g., "ETH-USDT").
    type: The order type (e.g., "MARKET", "LIMIT").
    side: The order side ("BUY" or "SELL").
    positionSide: The position side ("LONG" or "SHORT").
    quantity: The quantity of the order.
    recv_window: The receive window for the request (optional).


### `close_all_positions(symbol: str, recv_window: int = None)`
Close all positions for a specific trading pair using a market order.

One-click liquidation of all positions under the current account. Note that one-click liquidation is triggered by a market order.

    symbol: The trading pair symbol (e.g., "BTC-USDT").
    recv_window: The receive window for the request (optional).

### `cancel_order(symbol: str, order_id: str, recv_window: int = None)`
Cancel an order that is currently in the "entrusted" state.

    symbol: The trading pair symbol (e.g., "RNDR-USDT").
    order_id: The ID of the order to cancel.
    recv_window: The receive window for the request (optional).

### `cancel_batch_orders(symbol: str, order_id_list: list, recv_window: int = None)`
Cancel multiple orders in a single request. 

Batch cancellation of some of the orders whose current account is in the current entrusted state.

    symbol: The trading pair symbol (e.g., "BTC-USDT").
    order_id_list: A list of order IDs to cancel.
    recv_window: The receive window for the request (optional).

### `cancel_all_open_orders(symbol: str, order_type: str = None, recv_window: int = None)`
Cancel all open orders for a specific trading pair.

    symbol: The trading pair symbol (e.g., "ATOM-USDT").
    order_type: The order type to cancel (e.g., "LIMIT"). If None, cancels all order types.
    recv_window: The receive window for the request (optional).

### `get_all_open_orders(symbol: str, order_type: str = None, recv_window: int = None)`
Query all open orders for a specific trading pair.

    symbol: The trading pair symbol (e.g., "BTC-USDT").
    order_type: The order type to filter by (e.g., "LIMIT"). If None, returns all order types.
    recv_window: The receive window for the request (optional).

### `get_pending_order_status(symbol: str, order_id: str, recv_window: int = None)`
Query the status of a specific pending order.

    symbol: The trading pair symbol (e.g., "OP-USDT").
    order_id: The ID of the order to query.
    recv_window: The receive window for the request (optional).

### `get_order_details(symbol: str, order_id: str, recv_window: int = None)`
Query the details of a specific order.

    symbol: The trading pair symbol (e.g., "OP-USDT").
    order_id: The ID of the order to query.
    recv_window: The receive window for the request (optional).

### `get_margin_type(symbol: str, recv_window: int = None)`
Query the margin type (isolated or cross) for a specific trading pair.

    symbol: The trading pair symbol (e.g., "WOO-USDT").
    recv_window: The receive window for the request (optional).

### `change_margin_type(symbol: str, margin_type: str, recv_window: int = None)`
Change the user's margin mode on the specified symbol contract: isolated margin or cross margin.

    symbol: The trading pair symbol (e.g., "MINA-USDT").
    margin_type: The margin type to set ("ISOLATED" or "CROSSED").
    recv_window: The receive window for the request (optional).

### `get_leverage_and_positions(symbol: str, recv_window: int = None)`
Query the opening leverage and available positions of the user in the specified symbol contract.

    symbol: The trading pair symbol (e.g., "BCH-USDT").
    recv_window: The receive window for the request (optional).

### `set_leverage(symbol: str, leverage: int, side: str, recv_window: int = None)`
Adjust the user's opening leverage in the specified symbol contract.

    symbol: The trading pair symbol (e.g., "ETH-USDT").
    leverage: The leverage value to set (e.g., 8).
    side: The position side ("LONG" or "SHORT").
    recv_window: The receive window for the request (optional).

### `get_force_orders(symbol: str, start_time: int = None, end_time: int = None, recv_window: int = None)`
Query the user's forced liquidation orders.

    symbol: The trading pair symbol (e.g., "ATOM-USDT").
    start_time: The start time for the query in milliseconds (optional).
    end_time: The end time for the query in milliseconds (optional).
    recv_window: The receive window for the request (optional).

### `get_order_history(symbol: str, start_time: int = None, end_time: int = None, limit: int = 500, recv_window: int = None)`
Query the user's historical orders (order status is completed or canceled).

Key steps for using the API:
- The maximum query time range shall not exceed 7 days.
- Query data within the last 7 days by default.
- Return order list sorted by updateTime from smallest to largest.

    symbol: The trading pair symbol (e.g., "PYTH-USDT").
    start_time: The start time for the query in milliseconds (optional).
    end_time: The end time for the query in milliseconds (optional).
    limit: The maximum number of orders to retrieve (default is 500).
    recv_window: The receive window for the request (optional).

### `modify_isolated_position_margin(symbol: str, margin_type: int, amount: float, position_side: str, recv_window: int = None)`
Adjust the isolated margin funds for the positions in the isolated position mode.

    symbol: The trading pair symbol (e.g., "BTC-USDT").
    margin_type: The type of margin adjustment (1: Add margin, 2: Reduce margin).
    amount: The amount of margin to adjust.
    position_side: The position side ("LONG" or "SHORT").
    recv_window: The receive window for the request (optional).


## Contributing

Feel free to submit issues or pull requests if you'd like to improve this package.

## Disclaimer
This project is for informational and educational purposes only. You should not use this information or any other material as legal, tax, investment, financial or other advice. Nothing contained here is a recommendation, endorsement or offer by me to buy or sell any securities or other financial instruments. If you intend to use real money, use it at your own risk. Under no circumstances will I be responsible or liable for any claims, damages, losses, expenses, costs or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.

## Contacts
I develop trading bots of any complexity, dashboards and indicators for crypto exchanges, forex and stocks.
To contact me:

Discord: https://discord.gg/zSw58e9Uvf

😎 Register on BingX and get a **20% discount** on fees: https://bingx.com/invite/HAJ8YQQAG/

## VPS for bots and scripts
I prefer using DigitalOcean.
  
[![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%202.svg)](https://www.digitalocean.com/?refcode=3d7f6e57bc04&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)
  
To get $200 in credit over 60 days use my ref link: https://m.do.co/c/3d7f6e57bc04

