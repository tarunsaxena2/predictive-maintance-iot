import pandas as pd

df = pd.read_csv("data/ai4i2020.csv")

print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.head())

import pandas as pd

df = pd.read_csv("data/ai4i2020.csv")

print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows of the Dataset:")
print(df.head())    