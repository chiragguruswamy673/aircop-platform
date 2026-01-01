from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response
from event_bus.kafka_producer import publish_event
import random
import os

app = FastAPI(title="AIRCOP Gateway")

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests"
)

@app.middleware("http")
async def metrics_middleware(request, call_next):
    REQUEST_COUNT.inc()
    response = await call_next(request)
    return response

@app.get("/")
def root():
    return {"message": "AIRCOP Platform Running"}

@app.get("/health")
def health():
    if random.random() > 0.75:
        failure = {"status": "FAIL", "reason": "Memory spike detected"}

        if os.getenv("ENABLE_KAFKA", "false") == "true":
            publish_event("HEALTH_FAILURE", failure)

        return failure

    return {"status": "OK"}


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
