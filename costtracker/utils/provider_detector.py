def detect_provider(response):
    """
    Detect provider based on response structure
    """

    # Gemini
    if hasattr(response, "model_version"):
        return "gemini"

    # OpenAI
    if hasattr(response, "usage"):
        return "openai"
    
    # Unknown provider
    return None