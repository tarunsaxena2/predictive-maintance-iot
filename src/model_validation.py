print("Week 3 Day 2 Started")
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from imblearn.over_sampling import SMOTE
from lightgbm import LGBMClassifier
from imblearn.pipeline import Pipeline
from sklearn.model_selection import cross_validate

df = pd.read_csv("data/fused_dataset.csv")

print("Dataset Loaded Successfully")

print("Shape:", df.shape)

target_col = "Machine failure"

X = df.drop(
    columns=[
        target_col,
        "Product ID"
    ]
)

X = pd.get_dummies(
    X,
    columns=["Type"],
    drop_first=True
)

y = df[target_col]
# Clean column names for LightGBM

X.columns = (
    X.columns
    .str.replace("[", "", regex=False)
    .str.replace("]", "", regex=False)
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
    .str.replace(" ", "_", regex=False)
    .str.replace("/", "_", regex=False)
)
print("\nSample Feature Names:")

for col in X.columns[:10]:
    print(col)
print("\nFeature Shape:", X.shape)

print("Target Shape:", y.shape)
cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

print("\nCross Validation Ready")
print("Number of Folds:", cv.n_splits)

smote = SMOTE(
    random_state=42
)

print("\nSMOTE Ready")
print("Random State:", 42)

model = LGBMClassifier(
    random_state=42
)

print("\nLightGBM Ready")
print("Model Initialized Successfully")

pipeline = Pipeline([
    ("smote", smote),
    ("model", model)
])

print("\nPipeline Created Successfully")

print("Step 1: SMOTE")

print("Step 2: LightGBM")

print("\nRunning Cross Validation...\n")

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

print("Cross Validation Completed")

print("\nPer Fold F1 Scores\n")

for i, score in enumerate(
    scores["test_f1_macro"],
    start=1
):
    print(
        f"Fold {i}: {score:.4f}"
    )