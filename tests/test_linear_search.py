from src.data_loader import load_offers
from Algorithms.linear_search import linear_search

# Load all offers from the dataset
offers = load_offers()

# Search for offers from Nike
results, comparisons = linear_search(offers, "Nike")

# Display the offers that match the search
print("Search results:")

for offer in results:
    print(offer["brand_name"], "-", offer["offer_title"])

# Show how many comparisons were made
print("Total comparisons:", comparisons)

# Show how many offers were found
print("Total offers found:", len(results))


# To run this test:
# python -m tests.test_linear_search