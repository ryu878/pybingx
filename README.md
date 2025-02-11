# PyBingX

A Python client for the BingX cryptocurrency exchange API. This package allows developers to seamlessly interact with the BingX API to fetch market data, manage trades, and perform other account operations.

## Features

- Fetch market contract details
- Get order book depth information
- Retrieve recent trades
- Fetch historical klines (candlestick data)
- Easy-to-use and extend
- Built-in HMAC signature generation for secure API requests

## Installation

To install `pybingx`, first clone the repository and install it locally:

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

# Fetch contract details
contracts = client.get_contracts()
print("Contracts:", contracts)

# Fetch depth information
depth_info = client.get_depth("SHIB-USDT", limit=5)
print("Depth Info:", depth_info)

# Fetch recent trades
trades_info = client.get_trades("BTC-USDT", limit=10)
print("Recent Trades:", trades_info)

# Fetch premium index
premium_index = client.get_premium_index("BTC-USDT")
print("Premium Index:", premium_index)

# Fetch funding rate history with time range
start_time = 1672531200000  # Example timestamp in milliseconds
end_time = 1672617600000    # Example timestamp in milliseconds
funding_rate_history = client.get_funding_rate_history("BTC-USDT", start_time=start_time, end_time=end_time, limit=5)
print("Funding Rate History:", funding_rate_history)

# Fetch historical klines (candlestick data)
klines = client.get_klines("BTC-USDT", interval="1h", limit=1000, start_time=1672531200000)
print("Klines:", klines)

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

