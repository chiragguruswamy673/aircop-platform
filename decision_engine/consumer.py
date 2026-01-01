
import json
import os
from decision_engine.orchestrator import decide
from kafka import KafkaConsumer

def get_consumer():
    return KafkaConsumer(
        "system-events",
        bootstrap_servers=os.getenv("KAFKA_BROKER", "redpanda:9092"),
        auto_offset_reset="earliest",
        group_id="decision-engine-group",
        value_deserializer=lambda x: json.loads(x.decode("utf-8"))
    )

def main():
    if os.getenv("ENABLE_KAFKA", "false") != "true":
        print("🚫 Kafka disabled — Decision Engine idle")
        while True:
            pass  # keep container alive

    consumer = get_consumer()
    print("🧠 Decision Engine listening to Kafka...")

    for message in consumer:
        event = message.value
        decision = decide(event)
        print("🤖 AI DECISION:", decision)

if __name__ == "__main__":
    main()
