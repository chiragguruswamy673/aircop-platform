def assess(payload: dict) -> float:
    reason = payload.get("reason", "").lower()

    if "memory" in reason:
        return 0.85
    if "cpu" in reason:
        return 0.75

    return 0.3
