results, comparisons = binary_search(offers, "nike")

print("Offers found:", len(results))
print("Comparisons:", comparisons)


results, comparisons = binary_search(offers, "Ferrari") # Not existing brand

print("Offers found:", len(results))
print("Comparisons:", comparisons)

results, comparisons = binary_search(offers, "") # Empty string

print("Offers found:", len(results))
print("Comparisons:", comparisons)

# python -m tests.test_binary_search