from src.data_loader import load_offers
from Algorithms.binary_search import binary_search

# Load the offers from the dataset
offers = load_offers()


# Search for offers from Nike
print("Searching for Nike:")
results, comparisons = binary_search(offers, "Nike")
print("Offers found:", len(results))
print("Comparisons made:", comparisons)


# Test the search with a brand that is not in the dataset
print("\nTesting a brand that does not exist:")
results, comparisons = binary_search(offers, "Ferrari")
print("Offers found:", len(results))
print("Comparisons made:", comparisons)


# Test what happens when the search term is empty
print("\nTesting an empty search:")
results, comparisons = binary_search(offers, "")
print("Offers found:", len(results))
print("Number of comparisons:", comparisons)


# Run the test from the terminal:
# python -m tests.test_binary_search