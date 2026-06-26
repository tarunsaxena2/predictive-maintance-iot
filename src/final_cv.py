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