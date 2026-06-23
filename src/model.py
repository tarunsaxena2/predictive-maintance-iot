import pandas as pd
import numpy as np
from imblearn.pipeline import Pipeline as ImbPipeline
from imblearn.over_sampling import SMOTE
from lightgbm import LGBMClassifier

def build_pipeline():
    """
    Build SMOTE + LightGBM imbalanced classification pipeline.
    SMOTE is applied only inside training folds to prevent data leakage.
    
    Returns:
        ImbPipeline: Pipeline with SMOTE and LGBMClassifier
    """
    # Define SMOTE for handling class imbalance
    smote = SMOTE(random_state=42)
    
    # Define LightGBM classifier with default parameters
    lgbm = LGBMClassifier(
        random_state=42,
        n_jobs=-1,
        verbose=-1
    )
    
    # Build pipeline: SMOTE first, then LightGBM
    pipeline = ImbPipeline([
        ('smote', smote),
        ('lgbm', lgbm)
    ])
    
    return pipeline

if __name__ == "__main__":
    pipeline = build_pipeline()
    print("Pipeline built successfully!")
    print(pipeline)

# ============================================
# MODEL SUMMARY
# ============================================
# Pipeline: SMOTE → LightGBM
# SMOTE: Handles class imbalance (28.5:1 ratio)
# LightGBM: Gradient boosting classifier
# random_state=42: Reproducibility ensured
# ============================================

print("Model module loaded successfully")