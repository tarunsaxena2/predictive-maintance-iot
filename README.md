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
# 📘 WEEK 1 — Combined Sprint Summary

### **Sprint Goal:** *IoT Telemetry Ingestion & Signal Processing*

During Week 1, the team successfully established the complete project foundation for the Predictive Maintenance System. The repository, development environment, project structure, Git workflow, Kanban board, GitHub Issues, and documentation were fully configured to support collaborative development.

The AI4I 2020 Predictive Maintenance dataset was downloaded, inspected, and validated. Comprehensive Exploratory Data Analysis (EDA) was performed, including class imbalance analysis, correlation analysis, sensor distribution visualization, and dataset quality checks for missing values and duplicate records. The categorical **Type** feature was encoded into **Type_enc**, resulting in a clean and model-ready dataset.

On the feature engineering side, rolling window statistics were implemented for all sensor variables. Rolling **Mean**, **Standard Deviation**, and **Variance** features were generated using a configurable window size, then integrated into a reusable feature engineering pipeline for future model training.

Project governance was also completed through documentation updates, AGENTS role definitions, Antigravity project rules, brain memory files, progress tracking, pull request reviews, and Kanban management. By the end of the sprint, all Week 1 GitHub Issues were completed, notebooks were cleaned, documentation was finalized, and the project was prepared for advanced feature fusion and machine learning experiments in Week 2.

### **Week 1 Deliverables**

* ✅ Project repository and collaborative development workflow established.
* ✅ AI4I dataset downloaded, cleaned, validated, and prepared.
* ✅ Complete Exploratory Data Analysis (EDA) with visualizations and insights.
* ✅ Class imbalance, correlation, and sensor distribution analysis completed.
* ✅ Missing values, duplicate records, and categorical encoding handled.
* ✅ Rolling Mean, Standard Deviation, and Variance features engineered.
* ✅ Modular data loading and feature engineering pipelines implemented.
* ✅ Team documentation, Kanban board, progress tracker, and README updated.
* ✅ All Week 1 tasks successfully completed, reviewed, and merged.

### **Outcome**

Week 1 concluded with a clean, well-documented, and reproducible data processing pipeline. The project now includes a validated dataset, engineered rolling statistical features, and a collaborative development framework, providing a strong foundation for contextual data fusion, feature enhancement, and predictive model development in the upcoming sprint.


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

# 📊 Week 2 – Day 5 Progress Report (Finalization)

---

# 👨‍💻 Member 1 – Tarun Saxena (Data Engineer)

### ✅ Assigned Task

* Finalized `ablation_study.ipynb`
* Cleared notebook outputs
* Added title, section headers, and conclusion
* Saved final `ext_features` list in `src/feature_sets.py`
* Pushed clean notebook to repository

### ✅ Work Completed

* Organized the ablation study notebook with proper documentation.
* Added a final conclusion summarizing the impact of external features.
* Updated the final feature list used across the project.
* Removed unnecessary notebook outputs before committing.
* Successfully pushed all finalized changes to GitHub.

---

# 👨‍💻 Member 2 – Vaibhav Gautam (ML Engineer)

### ✅ Assigned Task

* Finalized all Week 2 visualization plots
* Saved plots as PNG files in `outputs/`
* Cleared visualization notebook outputs
* Wrote Week 2 EDA summary
* Pushed clean notebook

### ✅ Work Completed

* Generated all required visualization charts.
* Exported plots into the `outputs/` directory.
* Cleaned notebook outputs for submission.
* Prepared a concise EDA summary highlighting feature trends and data insights.
* Successfully pushed finalized visualization work.

---

# 👨‍💻 Member 3 – Vaibhav Gautam (Context & Integration)

### ✅ Assigned Task

* Finalized `week2_fusion.ipynb`
* Completed end-to-end feature integration pipeline
* Cleared notebook outputs
* Added summary section
* Updated `feature_engineering.py`
* Pushed final notebook

### ✅ Work Completed

* Completed the Week 2 feature fusion pipeline.
* Integrated preprocessing and engineered features into the workflow.
* Updated the final version of `feature_engineering.py`.
* Added a project summary section for better documentation.
* Removed notebook outputs and committed the clean version.

---

# 👨‍💻 Member 4 – Tarun Saxena (Evaluation & Deploy Lead)

### ✅ Assigned Task

* Updated Kanban Board
* Moved all Week 2 issues to **Done**
* Updated README with Week 2 summary
* Reviewed and merged all Week 2 Pull Requests

### ✅ Work Completed

* Successfully completed Kanban board management.
* Updated README with:

  * External feature integration summary
  * Ablation study findings
  * Week 2 achievements
* Reviewed all pull requests submitted during Week 2.
* Merged approved PRs into the project branch.
* Verified repository status and ensured Week 2 deliverables were complete.
  ---

  # 📊 WEEK 2 SUMMARY — Contextual Data Fusion & Feature Engineering

## 🎯 Sprint Goal

The primary objective of Week 2 was to enhance the predictive maintenance system by integrating simulated external environmental context with the existing IoT sensor dataset. The team aimed to engineer new contextual features, compare model performance before and after data fusion through an ablation study, and validate that external information improves machine failure prediction.

---

## 📌 Week 2 Overview

During Week 2, the project evolved from relying solely on internal IoT sensor data to incorporating external contextual information. Three realistic environmental variables—**Ambient Temperature**, **Factory Load Percentage**, and **Humidity Percentage**—were simulated using reproducible statistical distributions and merged with the cleaned IoT dataset. The data fusion process was carefully validated to ensure that all records remained aligned and no information was lost.

A structured feature engineering pipeline was developed to support both the baseline and extended feature sets. The baseline model used only internal IoT rolling features, while the extended model combined these features with the newly created environmental variables. Both models were trained using the same Random Forest algorithm and evaluated through **5-Fold Stratified Cross Validation**, ensuring a fair and reliable comparison.

An extensive ablation study was conducted to measure the contribution of external contextual features. Key evaluation metrics, including **Macro F1 Score**, **Precision**, and **Recall**, were compared between the baseline and extended models. The percentage improvement in Macro F1 was calculated, demonstrating the positive impact of contextual data on predictive performance.

To better understand the dataset, multiple exploratory visualizations were generated, including sensor distribution box plots, scatter plots, pair plots, correlation heatmaps, and ranked feature correlation charts. These visual analyses highlighted relationships between IoT sensor readings, environmental conditions, and machine failures, providing valuable insights into feature importance.

The feature engineering workflow was modularized by implementing a reusable `merge_external_context()` function, allowing external signals to be added efficiently to future datasets. Comprehensive validation checks confirmed proper timestamp alignment, merge integrity, and consistency of all engineered features.

Finally, all notebooks were cleaned and documented with clear titles, section headers, conclusions, and summaries. Project documentation, including the README, results comparison report, and Kanban board, was updated to reflect the successful completion of the sprint. All Week 2 pull requests were reviewed, merged, and the repository was prepared for the next development phase.

---

# 🏆 Key Achievements

* Successfully simulated realistic external environmental features.
* Integrated contextual data with the IoT dataset through a validated fusion pipeline.
* Created reusable feature engineering modules for future experiments.
* Conducted a complete ablation study comparing baseline and extended feature sets.
* Demonstrated improved predictive performance using contextual information.
* Generated comprehensive visualizations and feature correlation analyses.
* Validated dataset integrity, timestamp alignment, and merge correctness.
* Finalized notebooks, documentation, README updates, Kanban board, and repository cleanup.

---

# 🚀 Conclusion

Week 2 successfully established a complete **Contextual Data Fusion and Feature Engineering pipeline** for the predictive maintenance project. By combining IoT sensor data with simulated environmental context and validating its impact through an ablation study, the team demonstrated that contextual features provide additional predictive value and strengthen machine failure detection. This sprint laid a robust foundation for **Week 3**, where the project will focus on advanced model optimization, hyperparameter tuning, and deployment-ready machine learning workflows.

---

## Team Contributions

| Team Member    | Roles                                  | Status      |
| -------------- | -------------------------------------- | ----------- |
| Tarun Saxena   | Data Engineer & Eval/Deploy Lead       | ✅ Completed |
| Vaibhav Gautam | ML Engineer & Context Integration Lead | ✅ Completed |

