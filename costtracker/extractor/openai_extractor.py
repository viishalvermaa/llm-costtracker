from .base import standardize_output

def extract_openai(response):
    """
    Extract usage from OpenAI-style response
    """

    usage=getattr(response, "usage", None)

    if not usage:
        return standardize_output(0,0,getattr(response, "model", "unknown"))
    
    input_tokens=getattr(usage, "prompt_tokens", 0)
    output_tokens=getattr(usage, "completion_tokens", 0)
    model=getattr(response, "model", "unknown")

    return standardize_output(input_tokens,output_tokens,model)