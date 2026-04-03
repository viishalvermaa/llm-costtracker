import click
import runpy

from .state import reset_state, get_state, set_budget, get_budget
from .logger import set_log_file, log_output
from .config import load_config

@click.group()
def cli():
    """
    costtracker CLI tool
    """
    pass

@cli.command()
@click.argument("script")
@click.option("--budget", type=float, default=None, help="Set budget limit")
@click.option("--log-file", type=str, default=None, help="Logs output to file")
@click.option("--provider", type=str, default=None, help="Sets the provider to calculate cost")
def run(script, budget, log_file, provider):
    """
    Run a Python script with cost tracking enabled.
    """

    # Load config file
    config=load_config()

    # Merge values (priority: CLI > config > default)
    final_budget=budget if budget is not None else config.get("budget")
    final_log_file=log_file if log_file is not None else config.get("log_file")
    final_provider=provider if provider is not None else config.get("provider")

    # Reset previous state
    reset_state()

    # Apply config
    if final_budget is not None:
        set_budget(final_budget)

    if final_log_file:
        set_log_file(final_log_file)

    # Set budget if provided
    if budget is not None:
        set_budget(budget)

    # Set log file
    if log_file:
        set_log_file(log_file)

    # Inform user
    log_output(f"\nRunning {script}\n")

    # Execute script
    runpy.run_path(script, run_name="__main__")

    # Get final state
    state=get_state()

    # Print per-call breakdown
    log_output("\n------------------------------------")
    for i, cost in enumerate(state["calls"], start=1):
        log_output(f"Call {i} -> ${cost:.6f}")

    # Print summary
    log_output("\n------------------------------------")
    log_output(f"Total Calls: {state['total_calls']}")
    log_output(f"Total Cost: ${state['total_cost']:.6f}")
    log_output("------------------------------------\n")

    # Budget check
    budget_value=get_budget()
    if budget_value is not None and state['total_cost'] > budget_value:
        log_output(f"\n⚠️ Budget exceeded! Limit: ${budget_value:.6f} | Current: ${state['total_cost']:.6f}")
        log_output("------------------------------------\n")