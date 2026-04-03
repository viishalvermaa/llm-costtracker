from .openai_extractor import extract_openai
from .gemini_extractor import extract_gemini

def extract_usage(response, provider:str):
    """
    Router extraction based on provider
    """

    if provider=="openai":
        return extract_openai(response)
    elif provider=="gemini":
        return extract_gemini(response)
    
    else:
        raise ValueError(f"Unsupported provider: {provider}")