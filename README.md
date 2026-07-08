# AI-Driven SOC Framework
# AI-Driven Security Operations Center (SOC) Framework

An intelligent, layered, and explainable AI system designed to enhance threat detection, triage, and response in modern Security Operations Centers.

## Overview

This project presents a **four-layer AI-Driven SOC Framework** that combines machine learning, explainable AI (XAI), and human-in-the-loop governance to address key challenges in cybersecurity: high false positive rates, lack of model transparency, and analyst overload.

The architecture follows a modular design with clear separation of concerns across data ingestion, threat detection, explainable triage, and governed response.

## Architecture

The system is built on **four main layers**:

- **Layer 1: Data Ingestion & Normalization**
- **Layer 2: AI-Assisted Threat Detection** (XGBoost + LSTM)
- **Layer 3: Explainable AI Triage** (SHAP + LIME)
- **Layer 4: Human-in-the-Loop Governance**

**Key Technologies:**
- Behavioral analytics and sequence modeling
- MITRE ATT&CK mapping
- Explainable AI techniques
- SOAR integration
- NIST AI RMF aligned governance

## Repository Structure

```bash
├── src/
│   ├── layer1-ingestion/
│   ├── layer2-detection/
│   ├── layer3-xai/
│   └── layer4-hitl/
├── docs/
│   ├── architecture/
│   └── requirements/
├── models/           # Trained model artifacts
├── tests/            # Unit and integration tests
├── .github/workflows/ # CI/CD pipelines
└── README.md
