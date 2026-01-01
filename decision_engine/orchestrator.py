from agents.reliability_agent import assess as risk_assess
from agents.impact_agent import assess as impact_assess
from agents.cost_agent import assess as cost_assess
from agents.explainability_agent import explain
from agents.llm_agent import llm_reason
from metrics.prometheus_client import query


def collect_metrics(payload: dict) -> dict:
    return {
        "request_rate": query('rate(http_requests_total[1m])'),
        "restart_count": int(
            query('kube_pod_container_status_restarts_total{pod=~"aircop-gateway.*"}')
        )
    }


def decide(event: dict) -> dict:
    payload = event["payload"]

    # 1️⃣ Core signals
    risk = risk_assess(payload)
    impact = impact_assess(payload)
    cost_status = cost_assess()
    metrics = collect_metrics(payload)

    # 2️⃣ Build LLM context (THIS IS KEY)
    context = {
        "risk": risk,
        "impact": impact,
        "metrics": metrics,
        "cost": cost_status
    }

    # 3️⃣ LLM MAKES THE DECISION
    llm_decision = llm_reason(context)

    # 4️⃣ Final decision object
    decision = {
        "action": llm_decision["action"],
        "confidence": llm_decision["confidence"],
        "reason": llm_decision["reason"],
        "risk_score": risk,
        "impact": impact,
        "cost": cost_status,
        "metrics": metrics
    }

    # 5️⃣ Explainability layer
    decision["explanation"] = explain(decision)

    return decision


















