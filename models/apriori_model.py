import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from utils.data_loader import load_transactions

class AprioriModel:
    def __init__(self, min_support=0.1, min_confidence=0.5):
        self.min_support = min_support
        self.min_confidence = min_confidence
        self.rules = None

    def train(self, transactions):
        # One-hot encode the transaction data
        df_encoded = self._encode_transactions(transactions)

        # Apply the Apriori algorithm
        frequent_itemsets = apriori(df_encoded, min_support=self.min_support, use_colnames=True)

        # Generate association rules
        self.rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=self.min_confidence)
        self.rules = self.rules.sort_values(by="lift", ascending=False)

    def predict(self, input_products, num_recommendations=4):
        input_products = frozenset(input_products)
        matching_rules = self.rules[self.rules['antecedents'].apply(lambda x: input_products.issubset(x))]

        recommended_products = set()
        for _, row in matching_rules.iterrows():
            recommended_products.update(row['consequents'])

        return list(recommended_products)[:num_recommendations]

    def _encode_transactions(self, transactions):
        from mlxtend.preprocessing import TransactionEncoder
        te = TransactionEncoder()
        te_ary = te.fit(transactions).transform(transactions)
        return pd.DataFrame(te_ary, columns=te.columns_)

