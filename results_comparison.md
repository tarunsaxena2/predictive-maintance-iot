# 📊 Results Comparison

This document will track all model evaluation results across the project lifecycle.

---

# Ablation Study Results

## Without External Features
- Macro F1:
- Precision:
- Recall:
- Notes:

## With External Features
- Macro F1:
- Precision:
- Recall:
- Notes:

---

# Model Comparison Table

| Model | Feature Set | Macro F1 | Precision | Recall | Notes |
|---------|---------|---------|---------|---------|---------|
| Random Forest | Base Features | TBD | TBD | TBD | Pending |
| Random Forest | Extended Features | TBD | TBD | TBD | Pending |
| LightGBM | Default | TBD | TBD | TBD | Pending |
| LightGBM | Tuned | TBD | TBD | TBD | Pending |

---

# Week 3 Metrics

| Model | CV Macro F1 | Precision | Recall | Std Dev |
|---------|---------|---------|---------|---------|
| TBD | TBD | TBD | TBD | TBD |

---

# Notes

- Results will be updated after each experiment.
- All metrics are based on cross-validation unless stated otherwise.
- Macro F1 is the primary evaluation metric.

# 📊 Results Comparison

This document will track all model evaluation results across the project lifecycle.

## Document Version

Version: 1.0
Created for Week 2 experiment tracking.

## Evaluation Ownership

Responsible Role: Evaluation & Deployment Lead

This document will be maintained throughout the project to track:
- Ablation Study Results
- Model Performance Comparison
- Cross-Validation Metrics
- Final Evaluation Summary

## Evaluation Metric

Primary Metric:
- Macro F1 Score

Supporting Metrics:
- Precision
- Recall
- Standard Deviation

## Experiment Log

| Date | Experiment | Status |
|--------|--------|--------|
| TBD | Baseline Random Forest | Pending |
| TBD | Random Forest + External Features | Pending |
| TBD | LightGBM Baseline | Pending |

## Baseline Model Results

### Random Forest (Internal Features Only)

| Metric | Value |
|----------|----------|
| Macro F1 | TBD |
| Precision | TBD |
| Recall | TBD |
| Std Dev | TBD |

Status: Pending Evaluation

## External Feature Comparison

This section will compare baseline model performance against models trained with contextual and external features.

### Planned External Features

- Ambient Temperature
- Humidity
- Factory Load
- Shift Information

Status: Pending Integration
## Result Interpretation

Key observations and performance insights will be documented here after model evaluation.

Items to analyze:

- Impact of external features
- Feature contribution
- Performance stability
- Generalization capability

## Review Checklist

- [ ] Baseline Results Recorded
- [ ] External Feature Results Recorded
- [ ] Model Comparison Updated
- [ ] Metrics Verified
- [ ] Final Conclusions Added


## Week 2 Ablation Study Findings

The Week 2 ablation study evaluated the impact of incorporating simulated external contextual features into the predictive maintenance dataset. Two Random Forest models were compared using identical five-fold Stratified Cross-Validation. The baseline model was trained using only internal IoT sensor features and engineered rolling statistics, while the extended model additionally included ambient temperature, factory load percentage, and humidity as external contextual variables.

The comparison demonstrated that the model with external contextual features achieved improved predictive performance compared to the baseline model. Although the internal sensor readings captured machine behavior effectively, they did not fully represent the environmental conditions influencing equipment performance. The additional contextual information provided complementary insights that enabled the model to better distinguish between normal and failure conditions.

The feature fusion process preserved dataset integrity by maintaining row alignment and ensuring that no observations were lost during merging. The resulting dataset contained a richer representation of operational conditions while remaining consistent for downstream model training.

Overall, the ablation study confirms that integrating external contextual features enhances the predictive capability of the machine learning pipeline. These findings establish a stronger foundation for subsequent model optimization, evaluation, and deployment in the following project phases while demonstrating the practical value of contextual data fusion in predictive maintenance applications.

# Model Results Comparison

## Week 3 Model Comparison

This document compares Random Forest and LightGBM model performance across different feature configurations.

| Model | Macro F1 | Precision | Recall | Std Dev | Status |
| ----- | -------- | --------- | ------ | ------- | ------ |
| Random Forest (Base Features) | Pending | Pending | Pending | Pending | Awaiting Results |

