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
    return df

def rolling_std(df, window=5):
    """
    Generate rolling standard deviation for all sensor columns.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame
        window (int): Rolling window size (default=5)
    Returns:
        pd.DataFrame: DataFrame with rolling std features
    """
    for col in SENSOR_COLUMNS:
        df[f'{col}_rolling_std'] = df[col].rolling(window=window).std()
    return df

def rolling_var(df, window=5):
    """
    Generate rolling variance for all sensor columns.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame
        window (int): Rolling window size (default=5)
    Returns:
        pd.DataFrame: DataFrame with rolling variance features
    """
    for col in SENSOR_COLUMNS:
        df[f'{col}_rolling_var'] = df[col].rolling(window=window).var()
    return df

def generate_all_rolling_features(df, window=5):
    """
    Apply rolling mean, std and variance to all sensor columns.
    Drop NaN rows and print new shape.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame
        window (int): Rolling window size (default=5)
    Returns:
        pd.DataFrame: DataFrame with all rolling features
    """
    df = rolling_mean(df, window)
    df = rolling_std(df, window)
    df = rolling_var(df, window)
    
    # Drop NaN rows
    df = df.dropna()
    df = df.reset_index(drop=True)
    
    print(f"New shape after all rolling features: {df.shape}")
    return df

# ============================================
# MODULE SUMMARY
# ============================================
# 1. SENSOR_COLUMNS — standardized list of all 5 sensor features
# 2. sort_and_reset() — sorts and resets DataFrame index
# 3. rolling_mean() — generates rolling mean for all sensor columns
# 4. rolling_std() — generates rolling standard deviation
# 5. rolling_var() — generates rolling variance
# 6. generate_all_rolling_features() — applies all rolling features
# ============================================

print("Feature engineering module loaded successfully")