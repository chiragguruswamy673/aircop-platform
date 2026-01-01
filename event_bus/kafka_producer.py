from kafka import KafkaProducer
import json
import os

_producer = None

def get_producer():
    global _producer
    if _producer is None:
        _producer = KafkaProducer(
            bootstrap_servers=os.getenv("KAFKA_BROKER", "redpanda:9092"),
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )
    return _producer

def publish_event(event_type: str, payload: dict):
    producer = get_producer()
    event = {
        "type": event_type,
        "payload": payload
    }
    producer.send("system-events", event)
    producer.flush()
