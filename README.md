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

# Week 1 

## Predictive Maintenance IoT Project

**Day 1 Progress Report**

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
Status:✅ Completed


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

Status:✅ Completed


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

Status:✅ Completed


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
- Status:✅ Completed

**Day 2 Progress Report**

**Member 1 – Data Engineer (Tarun Saxena)**

--#Tasks Completed

* Downloaded the **AI4I 2020 Predictive Maintenance Dataset**.
* Stored the dataset in the project data directory for analysis.
* Created a Python data loading script using **Pandas**.
* Loaded the dataset into a Pandas DataFrame.
* Performed initial dataset inspection and validation.

--Dataset Inspection Results

* Dataset Shape: **10,000 rows × 14 columns**
* Verified successful dataset loading.
* Inspected all column names.
* Checked data types of all features.
* Displayed and reviewed the first 5 rows of the dataset.
* Confirmed the presence of the target variable **Machine Failure**.

--Key Features Identified

* Product ID
* Type
* Air Temperature [K]
* Process Temperature [K]
* Rotational Speed [rpm]
* Torque [Nm]
* Tool Wear [min]
* Machine Failure
* TWF, HDF, PWF, OSF, RNF failure indicators

--Tools & Technologies Used

* Python
* Pandas
* VS Code
* Git & GitHub



--Outcome

The AI4I 2020 Predictive Maintenance dataset was successfully downloaded, loaded, and inspected. The dataset structure, feature names, data types, and sample records were verified, confirming that the data is ready for data quality assessment and exploratory data analysis in the next phase.

Status:✅ Completed

**Member 2 – ML Engineer (Vaibhav Gautam)**
# Tasks Completed
* Opened `week1_eda.ipynb` notebook for exploratory data analysis
* Loaded AI4I 2020 Predictive Maintenance dataset (10,000 rows, 14 columns)
* Plotted class distribution using Seaborn countplot
* Calculated class frequencies:
  * No Failure (0): 9,661 samples — 96.61%
  * Failure (1): 339 samples — 3.39%
* Computed class imbalance ratio: **28.5:1**
* Added markdown commentary explaining:
  * What class imbalance is
  * Why it is a challenge for predictive maintenance
  * How it biases models toward majority class
  * Future solution: SMOTE will be used in Week 3
* Fixed and cleaned notebook — removed error cell
* Cleared all notebook outputs before committing
* Committed and pushed to GitHub branch `dev/vaibhav-gautam`

# Deliverables
* `notebooks/week1_eda.ipynb`
  * Class distribution countplot
  * Imbalance ratio calculation (28.5:1)
  * Markdown explanation of class imbalance problem

# Outcome
Successfully completed Day 2 EDA tasks. Dataset imbalance clearly identified and documented. Foundation ready for correlation heatmap analysis on Day 3.
Status:✅ Completed

**Member 3 – Context & Integration (Vaibhav Gautam)**
# Tasks Completed
* Created `src/feature_engineering.py` from scratch
* Defined centralized `SENSOR_COLUMNS` list:
  * Air temperature [K]
  * Process temperature [K]
  * Rotational speed [rpm]
  * Torque [Nm]
  * Tool wear [min]
* Implemented `sort_and_reset()` function:
  * Sorts DataFrame by index
  * Resets index after sorting
  * Ensures chronological ordering for time-series processing
* Written `rolling_feature_generator()` skeleton:
  * Accepts DataFrame and window size parameter
  * Framework ready for rolling mean, std, variance implementation
  * Will be fully implemented on Day 3
* Added proper docstrings and inline comments
* Committed and pushed to GitHub branch `dev/vaibhav-gautam`

# Deliverables
* `src/feature_engineering.py`
  * Sensor column definitions
  * `sort_and_reset()` utility function
  * Rolling feature generator skeleton
  * Full documentation and comments


# Outcome
Successfully established foundational feature engineering framework. Sensor columns standardized and sorting utility implemented. Rolling feature pipeline skeleton ready for full implementation on Day 3.
Status:✅ Completed

**Member 4 – Evaluation & Deployment Lead (Tarun Saxena)**

--Tasks Completed

Reviewed and synchronized the project repository.
Created AGENTS.md file with detailed role definitions for all four team members.
Documented responsibilities, assigned issues, deliverables, and workflow for each project role.
Added project governance and GitHub contribution guidelines.
Updated repository documentation to support team collaboration and project tracking.
Committed and pushed AGENTS documentation to the repository.
File Added
AGENTS.md


--Outcome

Team structure and responsibilities are clearly defined.
Project documentation has been improved.
Collaboration and task ownership are now documented for the entire project team.
Status:✅ Completed

**Day 3 Progress**

**Mamber 1 : Data Engineer(Tarun Saxena)**
Tasks Completed:

*Loaded and validated the AI4I Predictive Maintenance dataset.
* Verified dataset structure, dimensions, and column information.
* Performed missing value analysis across all dataset features.
* Conducted duplicate row detection and validation.
* Documented data quality findings and observations.
* Prepared final validation summary for the dataset.

Outcome:

* No missing values found in the dataset.
* No duplicate records detected.
* Dataset structure successfully verified.
* Dataset confirmed ready for preprocessing and feature engineering.

Status:✅ Completed

**Member 2 – ML Engineer (Vaibhav Gautam)**

# Tasks Completed
* Opened `week1_eda.ipynb` notebook for exploratory data analysis
* Loaded AI4I 2020 Predictive Maintenance dataset (10,000 rows, 14 columns)
* Plotted class distribution using Seaborn countplot
* Calculated class frequencies:
  * No Failure (0): 9,661 samples — 96.61%
  * Failure (1): 339 samples — 3.39%
* Computed class imbalance ratio: **28.5:1**
* Added markdown commentary explaining:
  * What class imbalance is
  * Why it is a challenge for predictive maintenance
  * How it biases models toward majority class
  * Future solution: SMOTE will be used in Week 3
* Fixed and cleaned notebook — removed error cell
* Cleared all notebook outputs before committing
* Committed and pushed to GitHub branch `dev/vaibhav-gautam`

# Deliverables
* `notebooks/week1_eda.ipynb`
  * Class distribution countplot
  * Imbalance ratio calculation (28.5:1)
  * Markdown explanation of class imbalance problem


# Outcome
Successfully completed Day 2 EDA tasks. Dataset imbalance clearly identified and documented. Foundation ready for correlation heatmap analysis on Day 3.
Status:✅ Completed

**Member 3 – Context & Integration (Vaibhav Gautam)**
# Tasks Completed
* Created `src/feature_engineering.py` from scratch
* Defined centralized `SENSOR_COLUMNS` list:
  * Air temperature [K]
  * Process temperature [K]
  * Rotational speed [rpm]
  * Torque [Nm]
  * Tool wear [min]
* Implemented `sort_and_reset()` function:
  * Sorts DataFrame by index
  * Resets index after sorting
  * Ensures chronological ordering for time-series processing
* Written `rolling_feature_generator()` skeleton:
  * Accepts DataFrame and window size parameter
  * Framework ready for rolling mean, std, variance implementation
  * Will be fully implemented on Day 3
* Added proper docstrings and inline comments
* Committed and pushed to GitHub branch `dev/vaibhav-gautam`

# Deliverables
* `src/feature_engineering.py`
  * Sensor column definitions
  * `sort_and_reset()` utility function
  * Rolling feature generator skeleton
  * Full documentation and comments

# Outcome
Successfully established foundational feature engineering framework. Sensor columns standardized and sorting utility implemented. Rolling feature pipeline skeleton ready for full implementation on Day 3.

Status:✅ Completed


**Mamber 4 : Evaluation & Deployment Lead(Tarun Saxena)**

Tasks Completed:

* Created project rules and governance documentation.
* Added project context memory documentation.
* Added dataset information memory and reference files.
* Expanded project context with sprint objectives.
* Documented dataset metadata and failure type information.
* Organized repository documentation for team collaboration.

Outcome:

* Project governance framework established.
* Development guidelines documented for contributors.
* Dataset metadata and failure type references centralized.
* Sprint objectives and project context documented for future development.

Status: ✅ Completed


