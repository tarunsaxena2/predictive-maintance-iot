import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("data/ai4i2020.csv")

# Create LabelEncoder
encoder = LabelEncoder()

# Encode Type column
df["Type_enc"] = encoder.fit_transform(df["Type"])

print("Encoding completed successfully")