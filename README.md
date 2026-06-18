# 🚀 Predictive Maintenance IoT Project

## 🔧 Contextual Predictive Maintenance System

### 🎯 Project Objective

Predict machine failures using IoT telemetry data and Machine Learning techniques before breakdowns occur, enabling proactive maintenance and reducing operational downtime.

---

## 📖 Problem Statement

Industrial equipment continuously generates large volumes of sensor telemetry data. Unexpected machine failures can lead to:

* Production downtime
* Increased maintenance costs
* Reduced operational efficiency
* Significant financial losses

This project leverages Machine Learning algorithms to analyze IoT sensor data and predict potential machine failures before they occur, allowing preventive maintenance actions.

---

## 📊 Dataset Information

### Dataset

**AI4I 2020 Predictive Maintenance Dataset**

### Sensor Features

| Feature                 | Description                 |
| ----------------------- | --------------------------- |
| Air Temperature [K]     | Ambient air temperature     |
| Process Temperature [K] | Machine process temperature |
| Rotational Speed [rpm]  | Machine rotational speed    |
| Torque [Nm]             | Applied torque              |
| Tool Wear [min]         | Tool wear duration          |

### Target Variable

| Variable        | Description                 |
| --------------- | --------------------------- |
| Machine Failure | 0 = No Failure, 1 = Failure |

---

## 👥 Team Members

| Member   | Role                           | Name           |
| -------- | ------------------------------ | -------------- |
| Member 1 | Data Engineer                  | Tarun Saxena   |
| Member 2 | ML Engineer                    | Vaibhav Gautam |
| Member 3 | Context & Integration Engineer | Vaibhav Gautam |
| Member 4 | Evaluation & Deployment Lead   | Tarun Saxena   |

---

## 🎯 Target KPIs

| Metric         | Target |
| -------------- | ------ |
| Macro F1 Score | ≥ 0.85 |
| Accuracy       | ≥ 90%  |
| Precision      | ≥ 85%  |
| Recall         | ≥ 85%  |

---

## 🛠️ Development Environment

### Environment Setup

* Python Virtual Environment Configured
* GitHub Repository Initialized
* Project Structure Created
* Jupyter Notebook Environment Configured

### Project Structure

```text
predictive-maintenance-iot/
│
├── data/
├── notebooks/
├── src/
├── models/
├── docs/
├── README.md
c
└── requirements.txt
```

---

## 📦 Installed Dependencies

```text
pandas
numpy
lightgbm
imbalanced-learn
shap
matplotlib
seaborn
scikit-learn
```

---

## 🔄 Project Workflow

1. Data Collection & Validation
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Data Fusion & Context Integration
5. Model Training
6. Model Evaluation
7. Explainability using SHAP
8. Deployment Preparation

---

## 📈 Expected Outcome

Develop an intelligent predictive maintenance system capable of identifying machine failure risks in advance, enabling proactive maintenance and minimizing operational disruptions.

---

# 🚀 Predictive Maintenance IoT Project

# 🚀 Week 1 Progress Report

## Contextual Predictive Maintenance IoT

### 🎯 Sprint Goal

Set up the project environment, ingest and clean the AI4I dataset, perform exploratory data analysis (EDA), and engineer rolling window features for predictive maintenance modeling.

---

# 📅 Week 1 – Day 1

## Project Initialization & Repository Setup

### 👨‍💻 Tarun Saxena (Member 1 – Data Engineer)

✅ Created project directory structure:

* data/
* notebooks/
* src/
* models/

✅ Configured Python virtual environment

✅ Installed required dependencies:

* Pandas
* NumPy
* Scikit-Learn
* LightGBM
* SHAP
* Matplotlib
* Seaborn
* Imbalanced-Learn

---

### 🤖 Vaibhav Gautam (Member 2 – ML Engineer)

✅ Configured Jupyter Notebook environment

✅ Installed and configured nbstripout

✅ Created Week 1 EDA notebook structure

---

### 🔗 Vaibhav Gautam (Member 3 – Context & Integration Lead)

✅ Created Week 2 Fusion notebook skeleton

✅ Installed GeoPandas and supporting libraries

✅ Reviewed AI4I dataset documentation

---

### 🛡️ Tarun Saxena (Member 4 – Eval & Deploy Lead)

✅ Created GitHub repository

✅ Added .gitignore

✅ Created README.md

✅ Configured Kanban Board

✅ Created and assigned all project GitHub issues

---

# 📅 Week 1 – Day 2

## Dataset Acquisition & Initial Exploration

### 👨‍💻 Tarun Saxena (Member 1)

✅ Downloaded AI4I 2020 Predictive Maintenance Dataset

✅ Loaded dataset into Pandas DataFrame

✅ Inspected:

* Dataset Shape
* Column Names
* Data Types
* Sample Records

---

### 🤖 Vaibhav Gautam (Member 2)

✅ Visualized class distribution

✅ Calculated class imbalance ratio

✅ Added EDA observations and markdown explanations

---

### 🔗 Vaibhav Gautam (Member 3)

✅ Defined sensor column list

✅ Created sorting utility functions

✅ Developed rolling feature generator skeleton

---

### 🛡️ Tarun Saxena (Member 4)

✅ Created AGENTS.md

✅ Defined responsibilities for all four team roles

✅ Configured development branch workflow

---

# 📅 Week 1 – Day 3

## Data Quality Assessment & Feature Engineering

### 👨‍💻 Tarun Saxena (Member 1)

✅ Checked missing values

✅ Identified duplicate rows

✅ Verified dataset quality

✅ Documented findings

---

### 🤖 Vaibhav Gautam (Member 2)

✅ Generated correlation heatmap

✅ Analyzed numerical feature relationships

✅ Identified top failure predictors

---

### 🔗 Vaibhav Gautam (Member 3)

✅ Implemented rolling mean feature generation

✅ Applied rolling window calculations

✅ Verified output dimensions

---

### 🛡️ Tarun Saxena (Member 4)

✅ Added project governance rules

✅ Created project memory documentation

✅ Organized project reference files

---

# 📅 Week 1 – Day 4

## Feature Transformation & Advanced Engineering

### 👨‍💻 Tarun Saxena (Member 1)

✅ Encoded categorical Type feature

✅ Created Type_enc variable

✅ Verified encoding integrity

---

### 🤖 Vaibhav Gautam (Member 2)

✅ Generated sensor distribution plots

✅ Compared distributions across failure classes

✅ Saved visual analysis outputs

---

### 🔗 Vaibhav Gautam (Member 3)

✅ Implemented:

* Rolling Mean
* Rolling Standard Deviation
* Rolling Variance

✅ Applied transformations to all sensor columns

✅ Removed generated NaN rows

---

### 🛡️ Tarun Saxena (Member 4)

✅ Created team progress tracker

✅ Reviewed and merged pull requests

✅ Updated project documentation

---

# 📅 Week 1 – Day 5

## Pipeline Finalization & Sprint Closure

### 👨‍💻 Tarun Saxena (Member 1)

✅ Final dataset validation completed

✅ Developed data_loader.py

Functions Added:

* load_data()
* clean_data()

✅ Added documentation and docstrings

---

### 🤖 Vaibhav Gautam (Member 2)

✅ Finalized complete EDA notebook

✅ Consolidated all visualizations

✅ Added EDA summary findings

✅ Cleared notebook outputs

---

### 🔗 Vaibhav Gautam (Member 3)

✅ Completed feature_engineering.py

✅ Integrated rolling feature pipeline

✅ Tested end-to-end feature generation process

---

### 🛡️ Tarun Saxena (Member 4)

✅ Updated Kanban Board

✅ Closed completed Week 1 issues

✅ Added Week 1 project summary

✅ Reviewed repository structure

---

# 📊 Week 1 Sprint Summary

## Key Deliverables Completed

✅ Project Repository Setup

✅ Team Workflow Configuration

✅ AI4I Dataset Acquisition

✅ Data Quality Validation

✅ Exploratory Data Analysis

✅ Categorical Feature Encoding

✅ Rolling Mean Features

✅ Rolling Standard Deviation Features

✅ Rolling Variance Features

✅ Data Loading Pipeline

✅ Feature Engineering Pipeline

✅ Documentation & Governance Framework

---

## Team Contributions

| Team Member    | Roles                                  | Status      |
| -------------- | -------------------------------------- | ----------- |
| Tarun Saxena   | Data Engineer & Eval/Deploy Lead       | ✅ Completed |
| Vaibhav Gautam | ML Engineer & Context Integration Lead | ✅ Completed |

---

## Sprint Outcome

Successfully established the complete data processing and feature engineering foundation for the Contextual Predictive Maintenance project. The dataset was cleaned, analyzed, transformed, and prepared for contextual feature integration and machine learning experiments planned for Week 2.

**Sprint Status:** 🟢 Successfully Completed

**Next Sprint:** Week 2 – Contextual Data Fusion & Ablation Study
# 🚀 Week 2 Progress Report

## Contextual Predictive Maintenance IoT

---

# 📅 Week 2 – Day 1

## Contextual Data Simulation & Experiment Setup

### 👨‍💻 Tarun Saxena (Member 1 – Data Engineer)

✅ Loaded cleaned dataset with rolling features

✅ Defined `base_features` containing internal telemetry features and `Type_enc`

✅ Created `feature_sets.py` for ablation study feature management

**Outcome:** Internal-only feature set prepared for baseline model evaluation.

---

### 🤖 Vaibhav Gautam (Member 2 – ML Engineer)

✅ Generated box plots for sensor distributions across failure categories

✅ Compared sensor behavior for:

* TWF
* HDF
* PWF
* OSF
* RNF

✅ Identified sensor patterns associated with specific failure types

**Outcome:** Better understanding of failure-specific sensor characteristics.

---

### 🔗 Vaibhav Gautam (Member 3 – Context & Integration Lead)

✅ Simulated external contextual variables:

* Ambient Temperature (`ambient_temp_C`)
* Factory Load (`factory_load_pct`)

✅ Applied reproducibility using `random_state=42`

**Outcome:** External environmental context dataset prepared.

---

### 🛡️ Tarun Saxena (Member 4 – Evaluation & Deployment Lead)

✅ Created `results_comparison.md`

✅ Added sections:

* Ablation Study Results
* Model Comparison Table
* Week 3 Metrics

**Outcome:** Evaluation framework established for upcoming experiments.

---

### 📊 Day 1 Status

| Member                    | Status      |
| ------------------------- | ----------- |
| Tarun Saxena (Member 1)   | ✅ Completed |
| Vaibhav Gautam (Member 2) | ✅ Completed |
| Vaibhav Gautam (Member 3) | ✅ Completed |
| Tarun Saxena (Member 4)   | ✅ Completed |

---

# 📅 Week 2 – Day 2

## Contextual Fusion & Baseline Evaluation

### 👨‍💻 Tarun Saxena (Member 1 – Data Engineer)

✅ Trained RandomForestClassifier using 5-Fold Stratified Cross Validation

✅ Evaluated model using Macro F1 Score

✅ Documented baseline experiment:

> Without External Features

**Outcome:** Internal-only benchmark model successfully established.

---

### 🤖 Vaibhav Gautam (Member 2 – ML Engineer)

✅ Generated scatter plots:

* Ambient Temperature vs Machine Failure
* Factory Load vs Machine Failure

✅ Calculated Point-Biserial Correlation coefficients

✅ Documented feature-target relationships

**Outcome:** Quantified predictive relevance of contextual variables.

---

### 🔗 Vaibhav Gautam (Member 3 – Context & Integration Lead)

✅ Simulated humidity signal

```python
humidity_pct = np.random.normal(loc=60, scale=10)
```

✅ Merged:

* Ambient Temperature
* Factory Load
* Humidity

with IoT telemetry dataset

✅ Verified merge dimensions and consistency

**Outcome:** Unified contextual dataset successfully created.

---

### 🛡️ Tarun Saxena (Member 4 – Evaluation & Deployment Lead)

✅ Reviewed contextual fusion notebook

✅ Verified:

* Correct index alignment
* No row loss
* Merge integrity maintained
* Dataset consistency preserved

✅ Added GitHub PR review comments

**Outcome:** Contextual data fusion validated and approved.

---

### 📊 Day 2 Status

| Member                    | Status      |
| ------------------------- | ----------- |
| Tarun Saxena (Member 1)   | ✅ Completed |
| Vaibhav Gautam (Member 2) | ✅ Completed |
| Vaibhav Gautam (Member 3) | ✅ Completed |
| Tarun Saxena (Member 4)   | ✅ Completed |

---
# 📅 Week 2 — Day 3 Progress Report (Wednesday)

## 🚀 Predictive Maintenance IoT Project

---

## 👨‍💻 Member 1 — Tarun Saxena (Data Engineer)

### ✅ Task Completed

* Defined **`ext_features`** list by combining:

  * Base sensor features
  * `ambient_temp_C`
  * `factory_load_pct`
  * `humidity_pct`
* Trained **Random Forest Classifier** using the extended feature set.
* Applied **5-Fold Cross Validation** to ensure robust model evaluation.
* Calculated and recorded **Macro F1 Score** for the **"With External Features"** experiment.
* Compared performance against baseline feature configuration for feature fusion assessment.


### 🎯 Status

**Completed Successfully**

---

## 👨‍💻 Member 2 — Vaibhav Gautam (ML Engineer)

### ✅ Task Completed

* Generated **Seaborn Pair Plot** using:

  * Top 4 important features
  * `Machine failure` target variable
* Created **Cross-Feature Correlation Heatmap** between:

  * External context variables
  * All machine sensor columns
* Saved all visualizations inside the **`outputs/`** directory.
* Prepared visual analysis artifacts to support feature fusion insights.



### 🎯 Status

**Completed Successfully**

---

## 👨‍💻 Member 3 — Vaibhav Gautam (Context & Integration)

### ✅ Task Completed

* Implemented **`merge_external_context(df)`** function in `feature_engineering.py`.
* Added comprehensive function **docstring** describing:

  * Purpose
  * Inputs
  * Outputs
* Integrated all simulated external signals:

  * `ambient_temp_C`
  * `factory_load_pct`
  * `humidity_pct`
* Tested functionality to verify successful feature merging.
* Displayed **before and after column counts** to validate integration.



### 🎯 Status

**Completed Successfully**

---

## 👨‍💻 Member 4 — Tarun Saxena (Eval & Deploy Lead)

### ✅ Task Completed

* Created a structured **Dataset Summary Table** in `week2_fusion.ipynb`.
* Documented the complete feature fusion workflow, including:

  * Original feature count
  * Rolling features added
  * External features added
  * Total engineered features
  * Final dataset shape
* Improved notebook readability and project documentation.
* Enabled quick verification of feature engineering and fusion pipeline outputs.



### 🎯 Status

**Completed Successfully**

---

# 📊 Day 3 Summary

| Member         | Role                  | Status      |
| -------------- | --------------------- | ----------- |
| Tarun Saxena   | Data Engineer         | ✅ Completed |
| Vaibhav Gautam | ML Engineer           | ✅ Completed |
| Vaibhav Gautam | Context & Integration | ✅ Completed |
| Tarun Saxena   | Eval & Deploy Lead    | ✅ Completed |

---
# 📅 Week 2 – Day 4 (Thursday) Progress Report

> **Project:** Predictive Maintenance using IoT & External Context Data  
> **Sprint:** Week 2 – Evaluation & Validation

---

## 👥 Team Contributions

| Member | Role | Status |
|---------|------|--------|
| **Tarun Saxena** | Data Engineer | ✅ Completed |
| **Vaibhav Gautam** | ML Engineer | ✅ Completed |
| **Vaibhav Gautam** | Context & Integration | ✅ Completed |
| **Tarun Saxena** | Eval & Deploy Lead | ✅ Completed |

---



## 🔹 Member 1 — Data Engineer (# 👨‍💻 Tarun Saxena)

### ✅ Completed Tasks
- Calculated the **Macro F1 Improvement Percentage** using:

```text
((External F1 - Baseline F1) / Baseline F1) × 100
```

- Compared baseline and enhanced models.
- Created a detailed evaluation table containing:
  - Feature Set
  - Macro F1
  - Precision
  - Recall
- Updated **ablation_study.ipynb** with complete calculations and documentation.



---


## 🔹 Member 2 — ML Engineer (# 👨‍💻 Vaibhav Gautam)

### ✅ Completed Tasks
- Generated the final **Top 10 Feature Correlation** bar chart.
- Included:
  - Internal sensor features
  - External contextual features
- Ranked features by **absolute correlation** with **Machine Failure**.
- Annotated each bar with correlation values for better interpretability.


---

## 🔹 Member 3 — Context & Integration (# 👨‍💻 Vaibhav Gautam)

### ✅ Completed Tasks
- Verified timestamp synchronization across all merged datasets.
- Validated rolling statistical features and external contextual data alignment.
- Displayed the first five rows of the merged DataFrame for verification.
- Added integrity and validation checks to ensure reliable data fusion before evaluation.



---



### Achievements
- 📈 Performance improvement quantified through Macro F1 comparison.
- 📊 Feature importance visualized using correlation analysis.
- 🔄 Data fusion validated through timestamp integrity checks.
- 📝 Ablation study findings documented for final reporting.
- 🚀 Repository updated with evaluation notebooks, documentation, and validation outputs.

---

# 🎯 Sprint Status

| Task | Status |
|------|--------|
| Model Evaluation | ✅ Completed |
| F1 Improvement Analysis | ✅ Completed |
| Feature Correlation Study | ✅ Completed |
| Data Validation | ✅ Completed |
| Ablation Study Documentation | ✅ Completed |
| Repository Update | ✅ Completed |

---

## 🔹 Member 4 — Eval & Deploy Lead (# 👨‍💻 Tarun Saxena)

### ✅ Completed Tasks
- Compiled the complete Week 2 Ablation Study findings.
- Wrote a **200-word evaluation summary** in **results_comparison.md**.
- Explained:
  - What experiments were performed
  - Performance improvements observed
  - Why external contextual features improved prediction quality
- Finalized documentation for reporting and deployment.

   
---

