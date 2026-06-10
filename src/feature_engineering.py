import pandas as pd
import numpy as np

# Define sensor columns
SENSOR_COLUMNS = [
    'Air temperature [K]',
    'Process temperature [K]',
    'Rotational speed [rpm]',
    'Torque [Nm]',
    'Tool wear [min]'
]

def sort_and_reset(df):
    """
    Sort DataFrame by index and reset index.
    
    Parameters: df (pd.DataFrame): Input DataFrame
    Returns: pd.DataFrame: Sorted and reset DataFrame
    """
    df = df.sort_index()
    df = df.reset_index(drop=True)
    return df

def rolling_mean(df, window=5):
    """
    Generate rolling mean for all sensor columns.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame
        window (int): Rolling window size (default=5)
    Returns:
        pd.DataFrame: DataFrame with rolling mean features
    """
    for col in SENSOR_COLUMNS:
        df[f'{col}_rolling_mean'] = df[col].rolling(window=window).mean()
    
    # Drop NaN rows created by rolling
    df = df.dropna()
    df = df.reset_index(drop=True)
    
    print(f"Output shape after rolling mean (window={window}): {df.shape}")
    return df

# Test the function
if __name__ == "__main__":
    df = pd.read_csv('../data/ai4i2020.csv')
    df = sort_and_reset(df)
    df = rolling_mean(df, window=5)
    print("Rolling mean features added successfully!")
    print("New columns:", [col for col in df.columns if 'rolling' in col])

print("Feature engineering module loaded successfully")