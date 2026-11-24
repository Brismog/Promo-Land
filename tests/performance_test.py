import time
from src.data_loader import load_offers
from Algorithms.linear_search import linear_search
from Algorithms.binary_search import binary_search
from Algorithms.hash_search import HashTable

# Load the dataset and choose a brand to search for
offers = load_offers()
brand_name = "Nike"

# Count the different brands in the dataset
unique_brands = set()

for offer in offers:
    unique_brands.add(offer["brand_name"].lower())

# Set up the hash table and add the offers
table_size = max(10, len(unique_brands) * 2)
hash_table = HashTable(table_size)

for offer in offers:
    hash_table.insert(offer)

# Run each search 1000 times
repetitions = 1000


# Measure the time taken by linear search
start_time = time.perf_counter()

for i in range(repetitions):
    linear_results, linear_comparisons = linear_search(offers, brand_name)

end_time = time.perf_counter()
linear_time = (end_time - start_time) / repetitions


# Measure the time taken by binary search
start_time = time.perf_counter()

for i in range(repetitions):
    binary_results, binary_comparisons = binary_search(offers, brand_name)

end_time = time.perf_counter()
binary_time = (end_time - start_time) / repetitions


# Measure the time taken by hash search
start_time = time.perf_counter()

for i in range(repetitions):
    hash_results, hash_comparisons = hash_table.search(brand_name)

end_time = time.perf_counter()
hash_time = (end_time - start_time) / repetitions


# Print the results for all three searches
print("\n========== Performance Test ==========")
print("Dataset size:", len(offers))
print("Number of brands:", len(unique_brands))
print("Search term:", brand_name)
print("Repetitions:", repetitions)


print("\n---------- Linear Search ----------")
print("Offers found:", len(linear_results))
print("Comparisons:", linear_comparisons)
print("Average time:", round(linear_time * 1000, 6), "ms")


print("\n---------- Binary Search ----------")
print("Offers found:", len(binary_results))
print("Comparisons:", binary_comparisons)
print("Average time:", round(binary_time * 1000, 6), "ms")


print("\n---------- Hash Search ----------")
print("Offers found:", len(hash_results))
print("Comparisons:", hash_comparisons)
print("Average time:", round(hash_time * 1000, 6), "ms")


# Run using: python -m tests.performance_test