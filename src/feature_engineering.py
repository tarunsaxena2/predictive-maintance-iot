import pandas as pd

SENSOR_COLUMNS = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]"
]

def add_rolling_mean(df, window=5):
    for col in SENSOR_COLUMNS:
        df[f"{col}_rolling_mean"] = df[col].rolling(window).mean()

    return df

def add_rolling_std(df, window=5):
    for col in SENSOR_COLUMNS:
        df[f"{col}_rolling_std"] = df[col].rolling(window).std()

    return df

def add_rolling_var(df, window=5):
    for col in SENSOR_COLUMNS:
        df[f"{col}_rolling_var"] = df[col].rolling(window).var()

    return df
def generate_rolling_features(df, window=5):

    df = add_rolling_mean(df, window)
    df = add_rolling_std(df, window)
    df = add_rolling_var(df, window)

    df = df.dropna()

    return df

# Test function end to end
if __name__ == "__main__":
    df = pd.read_csv('../data/ai4i2020.csv')
    df = sort_and_reset(df)
    df = generate_rolling_features(df, window=5)
    print("Feature engineering pipeline completed successfully!")

# ============================================
# MODULE SUMMARY
# ============================================
# 1. SENSOR_COLUMNS — standardized list of all 5 sensor features
# 2. sort_and_reset() — sorts and resets DataFrame index
# 3. generate_rolling_features() — generates rolling mean, std
#    and variance for all sensor columns in single pipeline
# ============================================

print("Feature engineering module loaded successfully")