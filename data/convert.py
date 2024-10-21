import csv

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

# Example data
data = [
    {
      "lineItems": {
        "nodes": [
          {
            "product": {
              "handle": "california-sun-kissed-navel-oranges",
              "category": None
            },
            "name": "California Sun Kissed Navel Oranges"
          },
          {
            "product": {
              "handle": "fresh-organic-honeycrisp-apples",
              "category": {
                "name": "Apples"
              }
            },
            "name": "Fresh Organic Honeycrisp Apples"
          },
          {
            "product": {
              "handle": "seedless-green-table-grapes",
              "category": None
            },
            "name": "Seedless Green Table Grapes"
          }
        ]
      }
    },
    {
      "lineItems": {
        "nodes": [
          {
            "product": {
              "handle": "farm-fresh-whole-organic-milk-1-gallon",
              "category": None
            },
            "name": "Farm Fresh Whole Organic Milk"
          },
          {
            "product": {
              "handle": "premium-grass-fed-unsalted-butter-1-lb",
              "category": None
            },
            "name": "Premium Grass Fed Unsalted Butter"
          },
          {
            "product": {
              "handle": "cage-free-organic-large-brown-eggs-dozen",
              "category": None
            },
            "name": "Cage Free Organic Large Brown Eggs"
          }
        ]
      }
    },
    {
      "lineItems": {
        "nodes": [
          {
            "product": {
              "handle": "california-sun-kissed-navel-oranges",
              "category": None
            },
            "name": "California Sun Kissed Navel Oranges"
          },
          {
            "product": {
              "handle": "freshly-squeezed-orange-juice-1-quart",
              "category": None
            },
            "name": "Freshly Squeezed Orange Juice"
          }
        ]
      }
    },
    {
      "lineItems": {
        "nodes": [
          {
            "product": {
              "handle": "red-organic-heirloom-tomatoes",
              "category": None
            },
            "name": "Red Organic Heirloom Tomatoes"
          },
          {
            "product": {
              "handle": "organic-russet-potatoes",
              "category": None
            },
            "name": "Organic Russet Potatoes"
          },
          {
            "product": {
              "handle": "locally-grown-organic-baby-spinach",
              "category": None
            },
            "name": "Locally Grown Organic Baby Spinach"
          }
        ]
      }
    }
]

# Convert the data to CSV and save it as 'output.csv'
convert_to_csv(data, 'transactions.csv')
