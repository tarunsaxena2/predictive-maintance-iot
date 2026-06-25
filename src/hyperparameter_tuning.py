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