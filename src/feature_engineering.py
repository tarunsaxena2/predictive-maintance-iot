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