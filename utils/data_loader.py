import pandas as pd

def load_transactions(filepath):
    # Load the transaction data from a CSV file, treating missing values as empty strings
    df = pd.read_csv(filepath, header=None, dtype=str)
    
    # Fill any NaN values with empty strings to avoid issues during split
    df.fillna('', inplace=True)

    # Ensure that each row is treated as a single transaction by splitting on commas
    transactions = df[0].apply(lambda x: str(x).split(',')).tolist()

    # Optionally, remove any leading or trailing whitespace from items
    transactions = [[item.strip() for item in transaction] for transaction in transactions]
    
    return transactions
