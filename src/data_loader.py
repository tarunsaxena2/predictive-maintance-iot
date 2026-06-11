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

def clean_data(df):
    """
    Clean AI4I dataset.

    Parameters:
        df (pandas.DataFrame): Input dataset

    Returns:
        pandas.DataFrame: Cleaned dataset
    """

    df = df.copy()
    df = df.drop_duplicates()
    df = df.dropna()

    return df