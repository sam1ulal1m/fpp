# main.py
from models.apriori_model import AprioriModel
from utils.data_loader import load_transactions

def main():
    # Load transactions from data file
    transactions = load_transactions('data/transactions.csv')

    # Create and train the Apriori model
    apriori_model = AprioriModel(min_support=0.1, min_confidence=0.5)
    apriori_model.train(transactions)

    # Example input: predict products frequently bought together with a specific product
    input_products = ['farm-fresh-whole-organic-milk-1-gallon']
    recommendations = apriori_model.predict(input_products, num_recommendations=4)

    # Print the recommendations
    print("Recommended products:", recommendations)

if __name__ == "__main__":
    main()
