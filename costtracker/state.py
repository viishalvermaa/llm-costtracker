# Global state (shared across entire script execution)

TOTAL_COST=0.0
TOTAL_CALLS=0
CALL_LOGS=[]
BUDGET=None

def set_budget(value:float):
    """
    Set budget for the session
    """

    global BUDGET
    BUDGET=value

def get_budget():
    return BUDGET

def update_state(cost: float):
    """
    Update total cost and call count
    """

    global TOTAL_COST, TOTAL_CALLS, CALL_LOGS

    TOTAL_COST+=cost
    TOTAL_CALLS+=1
    CALL_LOGS.append(cost)

def get_state():
    """
    Get current tracking state
    """

    return {
        "total_cost": TOTAL_COST,
        "total_calls": TOTAL_CALLS,
        "calls": CALL_LOGS
    }

def reset_state():
    """
    Reset state before running a new script
    """

    global TOTAL_COST, TOTAL_CALLS, CALL_LOGS

    TOTAL_COST=0.0
    TOTAL_CALLS=0
    CALL_LOGS=[]