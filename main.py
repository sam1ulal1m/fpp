from flask import Flask, request, jsonify
import subprocess
from models.apriori_model import AprioriModel
from utils.data_loader import load_transactions

app = Flask(__name__)

# Configure CORS for all origins (consider modifying for production)
@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Allow all origins (adjust for production)
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST'
    return response

# Initialize the Apriori model (but do not train it yet)
apriori_model = AprioriModel(min_support=0.05, min_confidence=0.2)

@app.route('/train', methods=['POST'])
def train():
    try:
        # Run the convert.py script to fetch and convert data into the CSV
        subprocess.run(['python3', 'data/convert.py'], check=True)

        # Load transactions from the newly created CSV file
        transactions = load_transactions('data/transactions.csv')

        # Train the model with the loaded transactions
        apriori_model.train(transactions)

        return jsonify({'message': 'Model trained successfully.'})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': f'Failed to run data conversion: {e}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/recommend', methods=['GET'])
def recommend():
    # Get product handle from query parameters
    product_handle = request.args.get('product_handle')

    if not product_handle:
        return jsonify({'error': 'Product handle is required'}), 400

    # Get recommendations for the provided product handle
    recommendations = apriori_model.predict([product_handle], num_recommendations=4)

    return jsonify({'recommended_products': recommendations})

if __name__ == "__main__":
    app.run(debug=True)