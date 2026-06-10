import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("data/ai4i2020.csv")

print("=== Before Encoding ===")
print(df["Type"].value_counts())

encoder = LabelEncoder()

df["Type_enc"] = encoder.fit_transform(df["Type"])

print("\n=== Encoding Mapping ===")
for original, encoded in zip(
        encoder.classes_,
        encoder.transform(encoder.classes_)):
    print(f"{original} -> {encoded}")

print("\n=== After Encoding ===")
print(df["Type_enc"].value_counts())