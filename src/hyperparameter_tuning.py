print("Week 3 Day 3 Started")

import pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_validate

from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline

from lightgbm import LGBMClassifier

print("Week 3 Day 3 Started")

df = pd.read_csv("data/fused_dataset.csv")

print("\nDataset Loaded Successfully")

print("Shape:", df.shape)

target_col = "Machine failure"

X = df.drop(columns=[target_col])

# Remove ID column
if "Product ID" in X.columns:
    X = X.drop(columns=["Product ID"])

# Encode machine type
if "Type" in X.columns:
    X = pd.get_dummies(
        X,
        columns=["Type"],
        drop_first=True
    )

y = df[target_col]

# Clean feature names
X.columns = (
    X.columns
    .str.replace("[", "", regex=False)
    .str.replace("]", "", regex=False)
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
    .str.replace(" ", "_", regex=False)
    .str.replace("/", "_", regex=False)
)

print("\nFeature Shape:", X.shape)
print("Target Shape :", y.shape)

# Hyperparameter Grid

n_estimators_list = [200, 500, 800]

learning_rate_list = [0.01, 0.05, 0.1]

num_leaves_list = [15, 31, 63]

print("\nHyperparameter Grid Ready")

print("n_estimators :", n_estimators_list)

print("learning_rate :", learning_rate_list)

print("num_leaves :", num_leaves_list)

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

print("\nCross Validation Ready")

def evaluate_model(
    n_estimators,
    learning_rate,
    num_leaves
):

    model = LGBMClassifier(
        n_estimators=n_estimators,
        learning_rate=learning_rate,
        num_leaves=num_leaves,
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
        scoring=["f1_macro"],
        n_jobs=-1
    )

    mean_f1 = scores["test_f1_macro"].mean()

    return mean_f1
print("\nRunning First Hyperparameter Tests...\n")

for n_estimators in n_estimators_list:

    score = evaluate_model(
        n_estimators,
        0.05,
        31
    )

    print(
        f"n_estimators={n_estimators} | "
        f"F1={score:.4f}"
    )