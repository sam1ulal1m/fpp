# data_loader.py
import pandas as pd

def load_transactions(filepath):
    # Load the transaction data from a CSV file
    df = pd.read_csv(filepath, header=None)
    transactions = df.apply(lambda row: row.dropna().tolist(), axis=1).tolist()
    return transactions
