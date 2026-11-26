from flask import Flask, render_template, request
from src.data_loader import load_offers
from Algorithms.linear_search import linear_search
from Algorithms.binary_search import binary_search
from Algorithms.hash_search import HashTable


# Start the PromoLand app
app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Load the offers from the CSV file
offers = load_offers()

# Create a hash table and add all offers
table_size = max(10, len(offers) * 2)
hash_table = HashTable(table_size)

for offer in offers:
    hash_table.insert(offer)

@app.route('/', methods=['GET', 'POST'])
def home():

    search_results = []
    brand_name = ""
    comparisons = 0
    algorithm = "linear"

    # Get the search details when the user submits the form
    if request.method == 'POST':
        brand_name = request.form.get('brand_name', '').strip()
        algorithm = request.form.get('algorithm', 'linear')

        # Search only if a brand name has been entered
        if brand_name:

            if algorithm == "linear":
                search_results, comparisons = linear_search(offers, brand_name)

            elif algorithm == "binary":
                search_results, comparisons = binary_search(offers, brand_name)

            elif algorithm == "hash":
                search_results, comparisons = hash_table.search(brand_name)


    # Put the highest discounts at the top of the results
    def get_offer_value(offer):
        return float(offer["discount_value"].replace("%", ""))

    search_results = sorted(
        search_results,
        key=get_offer_value,
        reverse=True
    )


    # Display the results on the website
    return render_template(
        'index.html',
        offers=search_results,
        brand_name=brand_name,
        algorithm=algorithm,
        comparisons=comparisons
    )

if __name__ == '__main__':
    app.run(debug=True)

# to run python -m src.app --> http://127.0.0.1:5000