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

    df = df.dropna()
    df = df.reset_index(drop=True)

    rolling_features = [col for col in df.columns if 'rolling' in col]
    print(f"Output shape after rolling features (window={window}): {df.shape}")
    print(f"Total rolling features added: {len(rolling_features)}")
    return df

def merge_external_context(df):
    """
    Simulate and merge external context signals with IoT DataFrame.
    Adds ambient_temp_C, factory_load_pct, humidity_pct columns.

    Parameters: df (pd.DataFrame): Input DataFrame
    Returns: pd.DataFrame: DataFrame with external context merged
    """
    np.random.seed(42)

    # Print column count before merge
    cols_before = len(df.columns)
    print(f"Columns before merge: {cols_before}")

    # Simulate external signals
    df['ambient_temp_C'] = np.random.normal(loc=28, scale=5, size=len(df))
    df['factory_load_pct'] = np.random.uniform(50, 100, size=len(df))
    df['humidity_pct'] = np.random.normal(loc=60, scale=10, size=len(df))

    # Print column count after merge
    cols_after = len(df.columns)
    print(f"Columns after merge: {cols_after}")
    print(f"New columns added: {cols_after - cols_before}")
    print(f"New shape: {df.shape}")

    return df

def add_rolling_var(df, window=5):
    for col in SENSOR_COLUMNS:
        df[f"{col}_rolling_var"] = df[col].rolling(window).var()


    return df
def generate_rolling_features(df, window=5):

# Test function end to end
if __name__ == "__main__":
    df = pd.read_csv('../data/ai4i2020.csv')
    df = sort_and_reset(df)
    df = generate_rolling_features(df, window=5)
    df = merge_external_context(df)
    print("Full pipeline completed successfully!")

# ============================================
# MODULE SUMMARY
# ============================================
# 1. SENSOR_COLUMNS — standardized list of all 5 sensor features
# 2. sort_and_reset() — sorts and resets DataFrame index
# 3. generate_rolling_features() — rolling mean, std, variance
# 4. merge_external_context() — adds ambient_temp, factory_load, humidity
# ============================================

    df = add_rolling_mean(df, window)
    df = add_rolling_std(df, window)
    df = add_rolling_var(df, window)

    df = df.dropna()


    return df