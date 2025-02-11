import hmac
import time
from hashlib import sha256

def generate_signature(secret_key, payload):
    return hmac.new(secret_key.encode("utf-8"), payload.encode("utf-8"), sha256).hexdigest()

def get_timestamp():
    return str(int(time.time() * 1000))