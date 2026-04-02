def format_output(data:dict)->str:
    return (
        f"\nModel: {data['model']}\n"
        f"Tokens: {data['total_tokens']} "
        f"(input: {data['input_tokens']}, output: {data['output_tokens']})\n"
        f"Cost: ${data['total_cost']:.6f}\n"
    )