# Import the function that loads our CSV data
from src.data_loader import load_offers

# Import our Linear Search algorithm.
from Algorithms.linear_search import linear_search


# Load all offers from the CSV file
offers = load_offers()

# Search for Nike.
results, comparisons = linear_search(offers, "Nike")

# Display the results
print("Search results:")

# Display each matching offer
for offer in results:
    print(offer["brand_name"], offer["offer_title"])

# Display the number of comparisons
print("Comparisons:", comparisons)

# Display the number of results
print("Offers found:", len(results))

# python -m tests.test_linear_search