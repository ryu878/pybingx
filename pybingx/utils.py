import time
import hmac
from hashlib import sha256

def get_signature(secret_key: str, payload: str) -> str:
    """Generate HMAC signature."""
    return hmac.new(secret_key.encode("utf-8"), payload.encode("utf-8"), sha256).hexdigest()

def parse_params(params: dict) -> str:
    """Convert dictionary to a URL-encoded query string."""
    params["timestamp"] = str(int(time.time() * 1000))
    return "&".join(f"{key}={params[key]}" for key in sorted(params))
