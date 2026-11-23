# Search using lowercase
results, comparisons = binary_search(offers, "nike")

print("Offers found:", len(results))
print("Comparisons:", comparisons)


# Search for a brand that does not exist
results, comparisons = binary_search(offers, "Ferrari")

print("Offers found:", len(results))
print("Comparisons:", comparisons)


# Search using an empty string
results, comparisons = binary_search(offers, "")

print("Offers found:", len(results))
print("Comparisons:", comparisons)

# python -m tests.test_binary_search