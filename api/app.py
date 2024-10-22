from flask import Flask, request, jsonify
from models.apriori_model import AprioriModel
from utils.data_loader import load_transactions

app = Flask(__name__)

# Initialize the AprioriModel
apriori_model = AprioriModel(min_support=0.1, min_confidence=0.5)

# Load the transaction data and train the model
transactions = load_transactions('data/transactions.csv')
apriori_model.train(transactions)

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        # Get the input data from the request
        data = request.json
        input_products = data.get('products', [])

        if not input_products:
            return jsonify({'error': 'No products provided'}), 400

        # Generate recommendations
        recommendations = apriori_model.predict(input_products, num_recommendations=4)

        # Return the recommendations as JSON
        return jsonify({'recommended_products': recommendations})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
