from .extractor import extract_usage
from .pricing import get_pricing
from .calculator import calculate_cost
from .formatter import format_output
from .logger import log_output
from .exceptions import CostTrackerError

def track(response, provider="openai"):
    try:
        # Extract usage
        usage_data=extract_usage(response, provider)

        input_tokens=usage_data["input_tokens"]
        output_tokens=usage_data["output_tokens"]
        model=usage_data["model"]

        # Get pricing
        pricing=get_pricing(model)

        # Calculate cost
        cost_data=calculate_cost(input_tokens, output_tokens, pricing)

        # Final data
        final_data={
            "model":model,
            "input_tokens":input_tokens,
            "output_tokens":output_tokens,
            "total_tokens": input_tokens+output_tokens,
            "total_cost": cost_data["total_cost"]
        }

        # Format output
        output=format_output(final_data)

        # Log output
        log_output(output)

        return final_data
    
    except CostTrackerError as e:
        log_output(f"[CostTracker Error] {str(e)}")
    except CostTrackerError as e:
        log_output(f"[Unexpected Error] {str(e)}")