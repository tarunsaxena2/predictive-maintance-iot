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

def rolling_feature_generator(df, window=5):
    """
    Skeleton for rolling feature generator.
    Will generate rolling mean, std, variance for sensor columns.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame
        window (int): Rolling window size (default=5)
    Returns:
        pd.DataFrame: DataFrame with rolling features
    """
    # To be implemented in Day 3
    pass

print("Feature engineering module loaded successfully")