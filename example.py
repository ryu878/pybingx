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