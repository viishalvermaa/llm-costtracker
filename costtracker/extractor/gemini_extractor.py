from .base import standardize_output

def extract_gemini(response):
    """
    Extract usage from Gemini response
    """
    try:
        model=getattr(response, "model_version", "unknown")

        usage=getattr(response, "usage_metadata", None)

        if usage:
            input_tokens=getattr(usage, "prompt_token_count", 0)
            output_tokens=getattr(usage, "candidates_token_count", 0)
        
        else:
            input_tokens=0
            output_tokens=0

        return standardize_output(input_tokens, output_tokens, model)
    
    except Exception:
        return standardize_output(0,0,"unknown")
