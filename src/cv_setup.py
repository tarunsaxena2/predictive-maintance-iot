import pandas as pd
from sklearn.model_selection import StratifiedKFold

df = pd.read_csv("data/fused_dataset.csv")

print("Dataset Loaded Successfully")

print("Shape:", df.shape)

print("\nColumns:\n")

for col in df.columns:
    print(col)

print("\nData Types:\n")

print(df.dtypes)

target_col = "Machine failure"

X = df.drop(columns=[target_col])

y = df[target_col]

print("\nFeature Shape:", X.shape)

print("Target Shape:", y.shape)

print("\nClass Counts:")

print(y.value_counts())

print("\nClass Percentage:")

print(y.value_counts(normalize=True) * 100)
print("\nCreating StratifiedKFold...")

skf = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

print("StratifiedKFold Created Successfully")

print("\nGenerating Folds...\n")

for fold, (train_idx, test_idx) in enumerate(
        skf.split(X, y),
        start=1):

    X_train = X.iloc[train_idx]
    X_test = X.iloc[test_idx]

    y_train = y.iloc[train_idx]
    y_test = y.iloc[test_idx]

    print(f"Fold {fold}")

    print("Train Shape:", X_train.shape)

    print("Test Shape :", X_test.shape)

    print("-" * 40)