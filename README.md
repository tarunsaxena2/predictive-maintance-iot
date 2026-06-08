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

| Member | Role | Name |
|----------|----------|-------------------|
| Member 1 | Data Engineer |Tarun Saxena |
| Member 2 | ML Engineer |Vaibhav Gautam |
| Member 3 | Context & Integration |Vaibhav Gautam |
| Member 4 | Evaluation & Deployment Lead | Tarun Saxena |

---

## Target KPI

- Macro F1 Score ≥ 0.85
- Accuracy ≥ 90%
- Precision ≥ 85%
- Recall ≥ 85%

---

## Development Environment

- Python virtual environment configured
- Project folders initialized
- Dependencies installation in progress

## Installed Dependencies

- pandas
- numpy
- lightgbm
- imbalanced-learn
- shap
- matplotlib
- seaborn
- scikit-learn

# Week 1 – Day 1 Progress Report
## Predictive Maintenance IoT Project

### Member 1 – Data Engineer (Tarun Saxena)

#### Tasks Completed
- Created project folder structure:
  - data/
  - notebooks/
  - src/
  - models/
- Set up Python virtual environment.
- Installed required dependencies:
  - pandas
  - numpy
  - lightgbm
  - imbalanced-learn
  - shap
  - matplotlib
  - seaborn
  - scikit-learn
- Verified environment setup and package installation.
- Committed changes to GitHub repository.

**Commit Message**
```bash
feat: initialize project folder structure and virtual environment (fixes #1)


## Member 2 – ML Engineer (Vaibhav Gautam)

### Tasks Completed

- Set up Jupyter Notebook development environment.
- Verified Jupyter Notebook installation and functionality.
- Installed and configured **nbstripout** for notebook output cleaning.
- Enabled nbstripout as a Git pre-commit hook.
- Created the notebook file:
  - `week1_eda.ipynb`
- Added initial notebook structure including:
  - Project Title
  - Introduction Section
  - Dataset Overview Section
  - Exploratory Data Analysis (EDA) Section
  - Observations Section
- Prepared notebook template for future data exploration activities.
- Verified notebook execution and repository integration.
- Committed all setup files and notebook skeleton to GitHub.

### Deliverables

- Jupyter Notebook environment configured.
- nbstripout hook installed and activated.
- `week1_eda.ipynb` notebook created with required headers and structure.
- Initial EDA workspace ready for Week 1 analysis tasks.

### Commit Message

```bash
feat: setup jupyter environment and nbstripout hook (fixes #1)


## Member 3 – Context & Integration Engineer (Vaibhav Gautam)

### Tasks Completed

- Set up Jupyter Notebook environment for project development.
- Created notebook skeleton:
  - `week2_fusion.ipynb`
- Added initial notebook sections:
  - Project Overview
  - Data Sources
  - Data Fusion Strategy
  - Feature Integration
  - Results & Observations
- Installed GeoPandas and supporting geospatial libraries.
- Verified successful installation of all required packages.
- Reviewed AI4I Predictive Maintenance Dataset documentation.
- Studied dataset structure, features, target variables, and failure categories.
- Identified key attributes for future integration and feature engineering tasks.
- Prepared notebook framework for Week 2 data fusion activities.
- Committed notebook skeleton and environment setup files to GitHub.

### Deliverables

- Jupyter Notebook environment configured.
- `week2_fusion.ipynb` notebook skeleton created.
- GeoPandas and required dependencies installed.
- AI4I dataset documentation reviewed and understood.
- Integration workflow prepared for upcoming project phases.

### Commit Message

```bash
feat: setup week2 notebook skeleton and review dataset docs (fixes #1)



## Member 4 – Evaluation & Deployment Lead (Tarun Saxena)

### Tasks Completed

- Created GitHub repository:
  - `predictive-maintenance-iot`
- Configured repository settings and initialized project workspace.
- Added `.gitignore` file using Python template.
- Included exclusions for:
  - data/
  - models/
  - virtual environment files
  - cache and temporary files
- Created `README.md` containing:
  - Project title
  - Project description
  - Objectives
  - Team roles
  - Technology stack
- Set up GitHub Kanban Board for project management.
- Created workflow columns:
  - To Do
  - In Progress
  - In Review
  - Done
- Created all project GitHub Issues according to the project task plan.
- Added appropriate labels to issues for organization and tracking.
- Assigned issues to respective team members based on responsibilities.
- Verified issue tracking and board integration.
- Committed all repository initialization and project management setup files.

### Deliverables

- GitHub repository successfully created and configured.
- README documentation added.
- .gitignore configured for Python project development.
- Kanban board established for project tracking.
- All project issues created, labeled, and assigned.
- Team workflow structure prepared for future development activities.

### Commit Message

```bash
feat: initialize github repo with gitignore, README, Kanban board and all issues (fixes #1)

### Project stucture
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
