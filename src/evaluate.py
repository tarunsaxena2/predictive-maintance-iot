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

    return scores