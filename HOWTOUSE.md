
---

### How to Use:
1. **Prepare the transaction data**: Add your transaction history to the `data/transactions.csv` file.
2. **Train the model**: The Apriori model will be trained on your transaction data, generating frequent itemsets and association rules.
3. **Make predictions**: Modify the `main.py` to input the products for which you want to get recommendations and run the script to get predictions.

This setup allows you to build and extend the model easily. You can experiment with different datasets and tweak parameters like `min_support` and `min_confidence` to adjust the model's behavior.
