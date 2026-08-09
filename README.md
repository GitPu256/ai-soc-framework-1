<<<<<<< HEAD
# AI-Driven Security Operations Center (SOC) Framework

![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![GitHub](https://img.shields.io/github/v/release/PNjenga/ai-soc-framework)

**Capstone Project** | **AI-Powered SOC with Explainability & Governance**

---

## 📋 Overview

This project presents a **conceptual AI-driven Security Operations Center (SOC) framework** designed to address key challenges in modern cybersecurity:

- Alert fatigue and high false-positive rates
- Limited interpretability of AI decisions
- Lack of proper governance and human oversight

The framework integrates **Machine Learning (XGBoost + LSTM)**, **Explainable AI (SHAP + LIME)**, **MITRE ATT&CK** mapping, and **Human-in-the-Loop Governance**.

---

## ✨ Key Features

- **Four-Layer Architecture**: Ingestion → Detection → XAI Triage → Governed Response
- **Hybrid Detection**: XGBoost for structured data + LSTM for sequential behavior
- **Explainable AI**: SHAP and LIME for transparent decision-making
- **MITRE ATT&CK Integration**: Contextual threat intelligence
- **Responsible AI**: Human validation, audit logging, and override capabilities

---

## 📁 Project Structure

```bash
ai-soc-framework/
├── docs/                          # Documentation & Full Report
├── src/                           # Prototype Source Code
=======

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
>>>>>>> fork/main
│   ├── layer1-ingestion/
│   ├── layer2-detection/
│   ├── layer3-xai/
│   └── layer4-hitl/
<<<<<<< HEAD
├── images/                        # Architecture & Dashboard Diagrams
├── models/                        # ML Models
├── appendices/                    # Supporting Materials
├── reports/                       # Evaluation Outputs
└── tests/                         # Unit Tests
=======
├── docs/
│   ├── architecture/
│   └── requirements/
├── models/           # Trained model artifacts
├── tests/            # Unit and integration tests
├── .github/workflows/ # CI/CD pipelines
└── README.md
>>>>>>> fork/main
