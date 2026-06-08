# Predictive-Maintenance-IoT

## Contextual Predictive Maintenance

### Project Objective
Predict machine failures using IoT telemetry and machine learning techniques before breakdown occurs.

---

## Problem Statement

Industrial machines generate large amounts of sensor data. Unexpected equipment failures can cause production downtime and financial losses.

This project uses machine learning models to analyze IoT sensor telemetry and predict potential machine failures in advance.

---

## Dataset

Dataset Used:
AI4I 2020 Predictive Maintenance Dataset

Features:

- Air Temperature [K]
- Process Temperature [K]
- Rotational Speed [rpm]
- Torque [Nm]
- Tool Wear [min]

Target:

- Machine Failure (0 = No Failure, 1 = Failure)

---

## Team Members

| Member | Role |
|----------|----------|
| Member 1 | Data Engineer |
| Member 2 | ML Engineer |
| Member 3 | Context & Integration |
| Member 4 | Evaluation & Deployment Lead |

---

## Target KPI

- Macro F1 Score ≥ 0.85
- Accuracy ≥ 90%
- Precision ≥ 85%
- Recall ≥ 85%

---

## Project Structure

```text
predictive-maintenance-iot/
│
├── data/
├── notebooks/
├── src/
│   ├── preprocessing/
│   ├── training/
│   ├── evaluation/
│   └── deployment/
│
├── models/
├── reports/
├── tests/
│
├── README.md
├── requirements.txt
└── .gitignore

## Development Environment

- Python virtual environment configured
- Project folders initialized
- Dependencies installation in progress