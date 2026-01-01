from agents.reliability_agent import assess as risk_assess
from agents.impact_agent import assess as impact_assess
from agents.cost_agent import assess as cost_assess, cost_aware_decision
from agents.explainability_agent import explain


def collect_metrics(payload: dict) -> dict:
    """
    Mocked for now — later from Prometheus.
    """
    return {
        "request_rate": payload.get("request_rate", 0.3),
        "restart_count": payload.get("restart_count", 1)
    }


def decide(event: dict) -> dict:
    payload = event["payload"]

    # 1️⃣ Core assessments
    risk = risk_assess(payload)
    impact = impact_assess(payload)
    cost_status = cost_assess()

    # 2️⃣ Initial reliability-based intent
    if risk > 0.8 and impact == "HIGH":
        proposed_action = "RESTART_SERVICE"
    elif risk > 0.6 and cost_status == "WITHIN_BUDGET":
        proposed_action = "SCALE_UP"
    else:
        proposed_action = "MONITOR"

    # 3️⃣ Cost-aware veto (IMPORTANT)
    metrics = collect_metrics(payload)
    cost_decision = cost_aware_decision(metrics)

    if proposed_action == "RESTART_SERVICE" and cost_decision["action"] != "RESTART":
        final_action = cost_decision["action"]
        confidence = cost_decision["confidence"]
        reason = cost_decision["reason"]
    else:
        final_action = proposed_action
        confidence = 0.9
        reason = "Reliability and impact justify action"

    # 4️⃣ Final decision object
    decision = {
        "action": final_action,
        "risk_score": risk,
        "impact": impact,
        "cost": cost_status,
        "confidence": confidence,
        "reason": reason
    }

    # 5️⃣ Explainability layer
    decision["explanation"] = explain(decision)

    return decision
