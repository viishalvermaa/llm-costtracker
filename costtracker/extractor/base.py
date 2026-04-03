from typing import Dict

def standardize_output(input_tokens:int, output_tokens:int, model:str) -> Dict:
    """
    Ensure all extractors return a consistent format
    """

    return {
        "input_tokens":input_tokens,
        "output_tokens":output_tokens,
        "model":model
    }