from .exceptions import UnsupportedModelError

# Prices per token (converted from per 1k tokens)
MODEL_PRICING={
    "gemini-2.5-flash-lite": {
        "input": 0.00035 / 1000,
        "output": 0.00105 / 1000
    },
    "gpt-4":{
        "input":0.03/1000,
        "output":0.06/1000
    },
    "gpt-3.5-turbo":{
        "input":0.001/1000,
        "output":0.002/1000
    }
}

def get_pricing(model:str)->dict:
    if model not in MODEL_PRICING:
        raise UnsupportedModelError(f"Pricing not found for model: {model}")
    
    return MODEL_PRICING[model]