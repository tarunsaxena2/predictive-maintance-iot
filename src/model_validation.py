print("Week 3 Day 2 Started")
import pandas as pd

df = pd.read_csv("data/fused_dataset.csv")

print("Dataset Loaded Successfully")

print("Shape:", df.shape)

target_col = "Machine failure"

X = df.drop(columns=[target_col])

y = df[target_col]

print("\nFeature Shape:", X.shape)

print("Target Shape:", y.shape)