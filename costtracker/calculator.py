def calculate_cost(input_tokens:int, output_tokens:int, pricing:dict)->dict:
    input_cost=input_tokens*pricing["input"]
    output_cost=output_tokens*pricing["output"]
    total_cost=input_cost+output_cost

    return {
        "input_cost": input_cost,
        "output_cost": output_cost,
        "total_cost": total_cost
    }