from src.data_loader import load_offers
from Algorithms.binary_search import binary_search

offers = load_offers()

results, comparisons = binary_search(offers, "Nike")
print("Offers found:", len(results))
print("Comparisons:", comparisons)

results, comparisons = binary_search(offers, "Ferrari")
print("Offers found:", len(results))
print("Comparisons:", comparisons)

results, comparisons = binary_search(offers, "")
print("Offers found:", len(results))
print("Comparisons:", comparisons)

# python -m tests.test_binary_search