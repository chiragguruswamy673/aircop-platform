import redis
import json

r = redis.Redis(host="redis", port=6379, decode_responses=True)

def publish_event(event_type: str, payload: dict):
    event = {
        "type": event_type,
        "payload": payload
    }
    r.publish("system_events", json.dumps(event))
