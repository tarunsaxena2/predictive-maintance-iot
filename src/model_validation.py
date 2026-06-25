print("Week 3 Day 2 Started")
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from imblearn.over_sampling import SMOTE
from lightgbm import LGBMClassifier
from imblearn.pipeline import Pipeline

df = pd.read_csv("data/fused_dataset.csv")

print("Dataset Loaded Successfully")

print("Shape:", df.shape)

target_col = "Machine failure"

X = df.drop(columns=[target_col])

y = df[target_col]

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