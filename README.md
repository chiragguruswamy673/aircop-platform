# AIRCOP – Autonomous Intelligent Resilience & Cost-Optimized Platform

AIRCOP is an autonomous, AI-driven self-healing platform built on Kubernetes that detects failures, reasons about impact and cost, and takes explainable remediation actions using an LLM-based decision engine.

---

## 🚀 Key Capabilities

- 🔁 **Self-Healing Microservices**
  - Automatic recovery from application and pod-level failures
- 🧠 **LLM-Based Decision Intelligence**
  - Replaces rule-based automation with explainable AI reasoning
- 💰 **Cost-Aware Healing**
  - Prevents over-healing during low traffic or flapping scenarios
- 📊 **Full Observability**
  - Prometheus metrics + Grafana dashboards
- 🧪 **Chaos Engineering**
  - Controlled failure injection with visual proof of recovery

---

## 🏗️ Architecture Overview

Client
|
v
Gateway Service (FastAPI)
|
| Health / Failure Events
v
Kafka (Redpanda)
|
v
Decision Engine
├─ Reliability Agent
├─ Impact Agent
├─ Cost Signal Collector
└─ LLM Reasoning Agent
|
v
Explainable Decision
|
v
Kubernetes Action (Restart / Monitor / Ignore)

yaml
Copy code

---

## 🧠 Decision Intelligence Flow

1. Gateway detects failure or degradation
2. Event is published to Kafka
3. Decision Engine collects:
   - Risk score
   - Impact level
   - Cost signals
   - Live Prometheus metrics
4. LLM agent reasons over structured context
5. Explainable decision is produced
6. Kubernetes executes the action

---

## 🤖 LLM-Based Reasoning (Core Innovation)

Instead of static rules, AIRCOP uses an LLM-style reasoning agent that returns **structured decisions**:

```json
{
  "action": "RESTART | IGNORE | MONITOR",
  "confidence": 0.0–1.0,
  "reason": "Explainable justification"
}
```
This ensures:

- Deterministic execution
- Auditability
- Safe AI usage in infrastructure decisions

## 📊 Observability
Metrics
- http_requests_total
- Pod restart counts
- Request rate trends
- Dashboards
- Traffic dips during failure
- Automatic recovery after healing
- Restart visualization

## 🧪 Chaos Engineering Validation
- Pod termination testing
- Application-level failure injection
- AI-triggered recovery
- Visual verification via Grafana

## 🛠️ Tech Stack
- Backend: Python, FastAPI
- Messaging: Kafka (Redpanda)
- AI Reasoning: LLM-style agent (pluggable)
- Orchestration: Kubernetes (Minikube)
- Observability: Prometheus, Grafana
- Containerization: Docker

## 📌 Why This Project Is Different
Most self-healing systems:
- Restart blindly
- Ignore cost
- Lack explainability
AIRCOP:
- Reasons before acting
- Balances reliability and cost
- Explains every decision

## 🔮 Future Enhancements
- Real LLM integration (OpenAI / Azure / Local)
- Confidence-based safety guardrails
- Cost modeling per cloud provider
- Grafana decision annotations
