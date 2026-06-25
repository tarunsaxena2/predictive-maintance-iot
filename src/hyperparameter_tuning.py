print("Week 3 Day 3 Started")

import pandas as pd

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