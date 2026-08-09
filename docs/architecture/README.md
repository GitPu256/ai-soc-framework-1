# Architecture Documentation

This folder contains system architecture documentation for the AI-Driven SOC Framework.


This section presents the system design for the AI Driven Security Operations Center (SOC) Framework. It explains the architecture, methodologies, algorithms, data flow, system components, and supporting design diagrams. The goal is to show how raw telemetry is transformed into prioritized, explainable, and governed SOC decisions.
3.1 System Architecture
The proposed system is a four layer AI Driven SOC Architecture that integrates ingestion, detection, explainability, and governance into a unified operational workflow. The architecture addresses three major SOC challenges: excessive alert volume, limited interpretability, and weak governance around AI assisted response.
The four layers include:
3.1.1 Data Ingestion and Normalization Layer
This layer receives raw telemetry from endpoints, cloud platforms, firewalls, identity systems, and threat intelligence feeds. It performs:
•	Schema validation
•	Deduplication
•	Timestamp alignment
•	Normalization
•	Privacy preserving controls (tokenization, minimization, encryption)
3.1.2 AI Based Threat Detection Layer
This layer applies:
•	QuickSort for deterministic triage
•	Binary Search for rapid severity lookup
•	XGBoost (placeholder) for structured event classification
•	LSTM (placeholder) for temporal sequence analysis
•	Anomaly scoring
•	MITRE ATT&CK mapping
Outputs include severity scores, confidence levels, and preliminary risk assessments.
3.1.3 Explainable AI Triage Layer
Explainability modules (SHAP and LIME placeholders) generate:
•	Feature importance insights
•	Confidence scores
•	Analyst readable summaries
This layer enhances transparency and supports analyst validation.
3.1.4 Governance and Response Layer
This layer enforces:
•	Human in the loop validation
•	Audit logging
•	Controlled SOAR playbook execution
•	Override justification
•	Compliance aligned response workflows
High risk alerts require explicit analyst approval before automated actions are executed.
As shown previously in Figure 1 the AI Driven SOC Architecture consists of four interconnected layers—Data Ingestion and Normalization, AI Based Threat Detection, Explainable AI Triage, and Governance and Response—each designed to transform raw telemetry into prioritized, transparent, and accountable security decisions.
3.2 Methodologies and Tools Used
The methodology combines deterministic algorithms, backend services, database storage, explainability placeholders, and governance controls to create a functional SOC prototype.
3.2.1 Algorithms and Core Logic
QuickSort Algorithm
Selected for its average case efficiency of O(n log n). Used to sort severity scores, timestamps, and other triage relevant attributes.
Binary Search Algorithm
Used for rapid lookup of severity values after sorting. Operates in O(log n) time, enabling fast retrieval even with large datasets.
Machine Learning Placeholders
Although full ML models were not implemented, placeholders demonstrate future integration:
•	XGBoost for structured event classification
•	LSTM for sequence based behavior analysis
•	Anomaly scoring
•	Confidence scoring
•	ATT&CK technique mapping
Explainability Tools
SHAP and LIME placeholders illustrate how feature level explanations would be generated.
Governance Tools
•	Approval gates
•	Audit logging
•	Incident review
•	Controlled SOAR execution
3.2.1.1 Detection and Triage Logic
The workflow follows a complete SOC pipeline:
1.	Collect telemetry
2.	Normalize events
3.	Extract features
4.	Score events using AI models
5.	Generate explanations
6.	Map alerts to MITRE ATT&CK
7.	Route alerts to analysts
8.	Require validation for high impact actions
9.	Execute governed response
10.	Store audit evidence
This ensures traceability from ingestion to final analyst decision.
3.2.2 Backend Framework (FastAPI)
FastAPI provides:
•	High performance RESTful endpoints
•	Automatic documentation (Swagger UI)
•	Seamless integration with Python algorithms
3.2.3 Database Storage (SQLite)
SQLite stores:
•	Severity values
•	Triage results
•	Audit logs
It supports rapid prototyping and persistent storage.
3.2.4 Software Configuration Management
•	Git for version control
•	Docker for environment consistency
3.3 Data Flow and System Components
The data flow begins when raw telemetry enters the ingestion layer from endpoint tools, cloud logs, identity systems, firewalls, network sensors, and threat intelligence sources.
3.3.1 Ingestion Module
•	Schema validation
•	Deduplication
•	Timestamp alignment
•	Parsing
•	Enrichment
•	Normalization
3.3.2 Feature Engineering Module
Extracts attributes such as:
•	Severity scores
•	Timestamps
•	Event types
•	Indicators of compromise
•	Geographic anomalies
•	Privilege use
•	Process behavior
3.3.3 Detection Module
Applies:
•	QuickSort
•	Binary Search
•	ML placeholders (XGBoost, LSTM)
Outputs include:
•	Risk scores
•	Confidence levels
•	Suspected attack categories
•	ATT&CK mappings
3.3.4 Explainability Module
Generates:
•	SHAP/LIME feature importance
•	Analyst readable summaries
3.3.5 Governance Module
Implements:
•	Approval gates
•	Audit logging
•	Controlled SOAR workflows
3.3.6 In-memory persistence module
Stores:
•	Severity values
•	Triage results
•	Audit logs
3.3.7 User Interface (UI)
Provides:
•	Log submission
•	Result visualization
•	Analyst decision interface
 Resource Justification Table
Resource	Purpose	Justification
Public or simulated security datasets	Model testing and workflow simulation	Allows evaluation without exposing proprietary or personally identifiable data.
Machine learning models	Threat classification and anomaly detection	Supports detection of patterns that static rules may miss.
Explainability methods	Analyst-facing interpretation	Improves transparency, trust, and alert triage quality.
MITRE ATT&CK mapping	Threat context and reporting	Provides standardized language for techniques, tactics, and coverage gaps.
Governance and audit controls	Accountable response	Preserves human oversight and supports compliance review.
Table 3.1. Resources used in the SOC prototype and their justification.

Project Risk Register
Risk	Impact	Mitigation	Timeline
False positives and alert fatigue	Critical alerts may be buried among low value findings, slowing early testing and distorting baseline triage metrics.	Establish baseline thresholds in Week 1, apply confidence bands, and refine prioritization rules in Week 2 before model integration.	Weeks
 1–2
Black box model decisions	Analysts may hesitate to act if the system cannot justify why a prediction was made, reducing trust during detection and explainability development.	Integrate SHAP/LIME outputs in Week 3, add plain language summaries in Week 4, and require decision logs for high risk alerts by Week 6.	Weeks 
3–6
Adversarial manipulation	Attackers could alter inputs or behavior patterns to evade detection during model development and validation.	Add adversarial test cases in Week 4, enforce strict input validation in Week 5, and introduce anomaly pattern review checkpoints in Week 6.	Weeks
 3–6
Concept drift	Threat behavior and baseline activity may change before prototype evaluation is complete, reducing model reliability.	Track drift indicators at each review checkpoint, adjust thresholds in Week 8, and plan retraining triggers for Week 10.	Weeks 
7–10
Automation bias	Users may accept recommendations too quickly if governance checkpoints are unclear, increasing operational risk.	Implement mandatory analyst approval in Week 7, add override justification fields in Week 8, and conduct supervisor review simulations in Weeks 9–10.	Weeks 
7–10
Table 3.2. Risks, impacts, and mitigation strategies across the project timeline.


3.4 Design Diagrams (DFD, UML, ER Diagram)
This section describes the design diagrams supporting the SOC framework.
3.4.1 Data Flow Diagram (DFD)
Shows telemetry flow from ingestion → normalization → feature extraction → detection → explainability → governance → audit logging.
 Data Flow Diagram
 <img width="975" height="650" alt="image" src="https://github.com/user-attachments/assets/d92cd1c6-c9d7-4571-a8f5-824e6273e619" />

Figure 4. Data flow diagram showing end to end SOC processing pipeline.
3.4.2 UML Use Case Diagram
Defines interactions among:
•	SOC Analyst
•	Incident Responder
•	SOC Manager/CISO
•	Compliance Reviewer
•	AI Detection Engine
•	Explainability Service
•	SOAR Platform
UML Use Case Diagram
 <img width="975" height="650" alt="image" src="https://github.com/user-attachments/assets/3ba15103-e837-40e1-8cbc-22520fe1c828" />

Figure 5. Use case diagram showing interactions between SOC stakeholders and system components.
3.4.3 Entity Relationship Diagram (ERD)
Defines core entities:
•	Event
•	Alert
•	ModelPrediction
•	Explanation
•	AnalystDecision
•	Incident
•	ResponseAction
•	AuditLog
•	User
•	Asset
•	ATT&CKTechnique
Entity Relationship Diagram
 <img width="1050" height="524" alt="image" src="https://github.com/user-attachments/assets/a4bfe302-3397-46f5-adb5-86ec32df3100" />

Figure 6: ER diagram showing traceability from raw telemetry to final response and audit evidence

