def assess(payload: dict) -> str:
    if "memory" in payload.get("reason", "").lower():
        return "HIGH"
    return "LOW"
