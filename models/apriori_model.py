# apriori_model.py
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from utils.data_loader import load_transactions

class AprioriModel:
    def __init__(self, min_support=0.1, min_confidence=0.5):
        self.min_support = min_support
        self.min_confidence = min_confidence
        self.rules = None

    def train(self, transactions):
        # Convert transactions to a one-hot encoded DataFrame
        self.transaction_df = pd.DataFrame([{item: True for item in transaction} for transaction in transactions]).fillna(False)

        # Apply apriori algorithm
        frequent_itemsets = apriori(self.transaction_df, min_support=self.min_support, use_colnames=True)
        print("Frequent Itemsets:\n", frequent_itemsets)

        # Check if frequent_itemsets is empty
        if frequent_itemsets.empty:
            print("No frequent itemsets found with the given support threshold.")
            return

        # Generate association rules with a lower confidence threshold
        self.rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.3)  # Lowered to 0.3
        print("Association Rules (Confidence >= 0.3):\n", self.rules)

        # Check if rules are generated
        if self.rules.empty:
            print("No association rules generated with the given confidence threshold.")
            # You could try generating rules with lift or other metrics
            self.rules_lift = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
            print("Association Rules (Lift >= 1.0):\n", self.rules_lift)

    def predict(self, input_products, num_recommendations=4):
        # Filter rules based on input_products
        relevant_rules = self.rules[self.rules['antecedents'].apply(lambda x: set(input_products).issubset(x))]
        print("Relevant Rules:\n", relevant_rules)

        recommendations = set()
        for _, rule in relevant_rules.iterrows():
            recommendations.update(rule['consequents'])

        # Return the top N recommendations
        return list(recommendations)[:num_recommendations]

    def _encode_transactions(self, transactions):
        from mlxtend.preprocessing import TransactionEncoder
        te = TransactionEncoder()
        te_ary = te.fit(transactions).transform(transactions)
        return pd.DataFrame(te_ary, columns=te.columns_)
