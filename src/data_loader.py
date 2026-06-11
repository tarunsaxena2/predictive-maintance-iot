import pandas as pd


def load_data(filepath):
    """
    Load AI4I dataset from CSV file.

    Parameters:
        filepath (str): Path to CSV file

    Returns:
        pandas.DataFrame: Loaded dataset
    """
    return pd.read_csv(filepath)