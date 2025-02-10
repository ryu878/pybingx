# PyBingX

A Python client for the BingX cryptocurrency exchange API. This package allows developers to seamlessly interact with the BingX API to fetch market data, manage trades, and perform other account operations.

## Features

- Fetch market contract details
- Get order book depth information
- Retrieve recent trades
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

## Contributing

Feel free to submit issues or pull requests if you'd like to improve this package.

## License

This project is licensed under the MIT License.

