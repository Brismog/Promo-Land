from src.data_loader import load_offers
from Algorithms.linear_search import linear_search

offers = load_offers()
results, comparisons = linear_search(offers, "Nike")

print("Search offers:")

for offer in results:
    print(offer["brand_name"], offer["offer_title"])

print("Comparisons:", comparisons)
print("Offers found:", len(results))

# python -m tests.test_linear_search