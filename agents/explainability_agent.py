def explain(decision: dict) -> str:
    return (
        f"Action '{decision['action']}' chosen because "
        f"failure probability was {decision['risk_score']} "
        f"with user impact '{decision['impact']}' "
        f"and cost status '{decision['cost']}'."
    )
