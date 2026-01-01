def llm_reason(context: dict) -> dict:
    """
    This function simulates an LLM.
    It RETURNS a JSON-like Python dict.
    """

    risk = context["risk"]
    impact = context["impact"]
    req_rate = context["metrics"]["request_rate"]
    restarts = context["metrics"]["restart_count"]

    # ---- LLM-style reasoning ----
    if risk > 0.8 and impact == "HIGH" and req_rate > 0.5:
        return {
            "action": "RESTART",
            "confidence": 0.9,
            "reason": "High risk with active user traffic justifies restart"
        }

    if req_rate < 0.2 and restarts >= 3:
        return {
            "action": "IGNORE",
            "confidence": 0.8,
            "reason": "Low traffic and repeated restarts indicate over-healing"
        }

    return {
        "action": "MONITOR",
        "confidence": 0.6,
        "reason": "Insufficient evidence for intervention"
    }
