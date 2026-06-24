import pandas as pd

df = pd.read_csv("data/fused_dataset.csv")

print("Dataset Loaded Successfully")

print("Shape:", df.shape)

print("\nColumns:\n")

for col in df.columns:
    print(col)

print("\nData Types:\n")

print(df.dtypes)