import json
import urllib.request

PRICING_URL = "https://raw.githubusercontent.com/viishalvermaa/costtrack-pricing-remote/refs/heads/main/pricing.json"

_cached_pricing = None

def fetch_remote_pricing():
    """
    Fetch price from remote source with caching
    """

    global _cached_pricing

    # Return cached if available
    if _cached_pricing is not None:
        return _cached_pricing
    
    try:
        with urllib.request.urlopen(PRICING_URL) as response:
            data=response.read()
            _cached_pricing=json.loads(data)
            return _cached_pricing
    except Exception:
        return {}