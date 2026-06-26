import pandas as pd

print("Week 3 Day 4 Started")

# =====================================
# Load Dataset
# =====================================

df = pd.read_csv("data/fused_dataset.csv")

print("\nDataset Loaded Successfully")

print("Shape:", df.shape)

print("\nColumns:")

for col in df.columns:
    print(col)

# =====================================
# Feature Preparation
# =====================================

target_col = "Machine failure"

X = df.drop(columns=[target_col])

# Remove Product ID
if "Product ID" in X.columns:
    X = X.drop(columns=["Product ID"])

# Convert Type into numeric columns
if "Type" in X.columns:
    X = pd.get_dummies(
        X,
        columns=["Type"],
        drop_first=True
    )

y = df[target_col]

# =====================================
# Clean Feature Names
# =====================================

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

print("\nTarget Distribution:")

print(y.value_counts())