def cost_aware_decision(metrics: dict) -> dict:
    """
    Decide whether healing is worth the cost.
    """

    req_rate = metrics.get("request_rate", 0)
    restarts = metrics.get("restart_count", 0)

    if req_rate < 0.2 and restarts >= 3:
        return {
            "action": "IGNORE",
            "confidence": 0.78,
            "reason": "Low traffic and repeated restarts"
        }

    if restarts >= 5:
        return {
            "action": "DELAY",
            "confidence": 0.85,
            "reason": "Restart flapping detected"
        }

    return {
        "action": "RESTART",
        "confidence": 0.65,
        "reason": "Traffic justifies healing cost"
    }