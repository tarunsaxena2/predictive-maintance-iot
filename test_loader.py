from src.data_loader import load_data

df = load_data("data/cleaned_ai4i.csv")

print(df.shape)
print(df.head())