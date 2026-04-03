from .extractor import extract_usage
from .pricing import get_pricing
from .calculator import calculate_cost
from .formatter import format_output
from .logger import log_output
from .exceptions import CostTrackerError
from .state import update_state
from .config import load_config
from .utils.provider_detector import detect_provider

def track(response, provider=None):
    """
    Track cost of a response.
    Provider can be passed explicitly or resolved via config/default
    """

    try:
        config=load_config()

        # explicit provider
        if provider:
            final_provider=provider
        
        # auto-detect first
        else:
            detected=detect_provider(response)

            if detected:
                final_provider=detected

            # fallback to config(future release)
            elif config.get("provider"):
                final_provider=config.get("provider")
            
            else:
                log_output("⚠️ Could not detect provider. Skipping cost tracking.")
                return None


        # Extract usage
        try:
            usage_data=extract_usage(response, final_provider)
        except Exception:
            log_output("⚠️ Failed to extract usage data. Skipping.")
            return None

        input_tokens=usage_data.get("input_tokens", 0)
        output_tokens=usage_data.get("output_tokens", 0)
        model=usage_data.get("model", "unknown")

        if model == "unknown":
            log_output("⚠️ Model not detected. Skipping cost calculation.")

            update_state(0)

            return {
                "model":model,
                "input_tokens":input_tokens,
                "output_tokens":output_tokens,
                "total_tokens": input_tokens+output_tokens,
                "total_cost": 0
            }


        # Get pricing
        try:
            pricing=get_pricing(model)
        except Exception:
            log_output(f"⚠️ Pricing not found for model: {model}. Skipping cost.")

            update_state(0)

            return {
                "model":model,
                "input_tokens":input_tokens,
                "output_tokens":output_tokens,
                "total_tokens": input_tokens+output_tokens,
                "total_cost": 0
            }


        # Calculate cost
        try:
            cost_data=calculate_cost(input_tokens, output_tokens, pricing)
            total_cost=cost_data.get("total_cost", 0)
        except Exception:
            log_output("⚠️ Cost calculation failed.  Setting cost to 0.")
            total_cost=0
        

        update_state(total_cost)

        # Final data
        final_data={
            "model":model,
            "input_tokens":input_tokens,
            "output_tokens":output_tokens,
            "total_tokens": input_tokens+output_tokens,
            "total_cost": total_cost
        }

        # Format output
        try:
            output=format_output(final_data)
        except Exception:
            log_output(f"Tracked: {final_data}")

        # Log output
        # log_output(output)

        return final_data
    
    except Exception as e:
        log_output(f"[Unexpected Error] {str(e)}")
        return None