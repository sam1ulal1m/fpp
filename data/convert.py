import csv
import requests

def convert_to_csv(data, output_file):
    # Open the CSV file for writing
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)

        # Loop through each item in the data (each order)
        for item in data:
            handles = []
            
            # Loop through each line item in the current order's nodes
            for line_item in item['lineItems']['nodes']:
                # Extract product handle if the product is not None
                if line_item['product']:
                    handles.append(line_item['product']['handle'])
            
            # Write the row to the CSV file (joining handles with commas)
            writer.writerow([','.join(handles)])

def fetch_order_data(api_url):
    try:
        # Send a GET request to the provided API URL
        response = requests.get(api_url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the JSON response
        order_data = response.json()

        # Return the list of orders
        return order_data.get('orders', [])

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data from API: {e}")
        return []

if __name__ == "__main__":
    # API URL to fetch order data
    api_url = 'https://warriors-portfolio-specified-hunt.trycloudflare.com/api/products?shop=dyn-sa-3.myshopify.com'

    # Fetch data from the API
    order_data = fetch_order_data(api_url)

    # Convert the fetched data to CSV
    output_file = 'data/transactions.csv'
    convert_to_csv(order_data, output_file)

    print(f"Data saved to {output_file}")
