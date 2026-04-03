from .pricing_loader import fetch_remote_pricing

def get_pricing(model:str):
    """
    Get pricing for a given model from remote source
    """

    pricing_data=fetch_remote_pricing()

    if not pricing_data:
        raise ValueError("Pricing service unavailable")
    if model not in pricing_data:
        raise ValueError(f"Pricing not found for model: {model}")
    
    return pricing_data[model]
    