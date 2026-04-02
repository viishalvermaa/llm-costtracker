from .exceptions import InvalidResponseError

def extract_usage(response, provider="openai")->dict:
    try:
        if provider=="openai":
            usage=getattr(response,"usage", None)

            if not usage:
                raise InvalidResponseError("No usage data found in response")
            
            return {
                "input_tokens":getattr(usage, "prompt_tokens", 0),
                "output_tokens": getattr(usage, "completion_tokens", 0),
                "model": getattr(response, "model", "unknown")
            }
        
        raise InvalidResponseError(f"Unsupported Provider: {provider}")
    
    except Exception as e:
        raise InvalidResponseError(f"Failed to extract usage: {str(e)}")
    
    