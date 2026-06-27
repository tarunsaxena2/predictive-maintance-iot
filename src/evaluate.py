import pandas as pd

from sklearn.model_selection import (
    StratifiedKFold,
    cross_validate
)

from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline

from lightgbm import LGBMClassifier

print("Evaluate Module Ready")


def evaluate_model(X, y, model):

    cv = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=42
    )

    pipeline = Pipeline([
        ("smote", SMOTE(random_state=42)),
        ("model", model)
    ])

    scores = cross_validate(
        pipeline,
        X,
        y,
        cv=cv,
        scoring=[
            "f1_macro",
            "precision_macro",
            "recall_macro"
        ],
        n_jobs=-1
    )

    # Calculate Mean Scores
    f1_mean = scores["test_f1_macro"].mean()
    f1_std = scores["test_f1_macro"].std()

    precision_mean = scores["test_precision_macro"].mean()

    recall_mean = scores["test_recall_macro"].mean()

    # Return Results
    return {
        "f1_macro": f1_mean,
        "precision_macro": precision_mean,
        "recall_macro": recall_mean,
        "std_dev": f1_std
    }