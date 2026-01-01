from agents.reliability_agent import assess as risk_assess
from agents.impact_agent import assess as impact_assess
from agents.cost_agent import assess as cost_assess
from agents.explainability_agent import explain

def decide(event: dict) -> dict:
    payload = event["payload"]

    risk = risk_assess(payload)
    impact = impact_assess(payload)
    cost = cost_assess()

    if risk > 0.8 and impact == "HIGH":
        action = "RESTART_SERVICE"
    elif risk > 0.6 and cost == "WITHIN_BUDGET":
        action = "SCALE_UP"
    else:
        action = "MONITOR"

    decision = {
        "action": action,
        "risk_score": risk,
        "impact": impact,
        "cost": cost
    }

    decision["explanation"] = explain(decision)
    return decision
