from pybingx.client import BingXClient

api_key = "your_api_key"
secret_key = "your_secret_key"

client = BingXClient(api_key, secret_key)
contracts = client.get_contracts()
print(contracts)
