import time
from src.data_loader import load_offers
from Algorithms.linear_search import linear_search
from Algorithms.binary_search import binary_search
from Algorithms.hash_search import HashTable

offers = load_offers()
brand_name = "Nike"
unique_brands = set() # Count brands

for offer in offers:
    unique_brands.add(offer["brand_name"].lower())
table_size = max(10, len(unique_brands) * 2) # Create Hash table
hash_table = HashTable(table_size)

for offer in offers:
    hash_table.insert(offer)

repetitions =1000


# Linear Search
start_time = time.perf_counter()

for i in range(repetitions):
    linear_results, linear_comparisons = linear_search(offers, brand_name)

end_time = time.perf_counter()
linear_time = (end_time - start_time) / repetitions


# Binary Search 
start_time = time.perf_counter()

for i in range(repetitions):
    binary_results, binary_comparisons = binary_search(offers, brand_name)

end_time = time.perf_counter()
binary_time = (end_time - start_time) / repetitions


# Hash Search 
start_time = time.perf_counter()
for i in range(repetitions):
    hash_results, hash_comparisons = hash_table.search(brand_name)

end_time = time.perf_counter()
hash_time = (end_time - start_time) / repetitions


# Display the results
print("----------------------")
print("Performance Test")
print("----------------------")
print("Dataset size:", len(offers))
print("Unique brands:", len(unique_brands))
print("Brand searched:", brand_name)
print("Repetitions:", repetitions)

print(".....................")
print("\nLinear Search")
print("Offers found:", len(linear_results))
print("Comparisons:", linear_comparisons)
print("Average time:", linear_time * 1000, "ms")

print(".....................")
print("\nBinary Search")
print("Offers found:", len(binary_results))
print("Comparisons:", binary_comparisons)
print("Average time:", binary_time * 1000, "ms")

print(".....................")
print("\nHash Search")
print("Offers found:", len(hash_results))
print("Comparisons:", hash_comparisons)
print("Average time:", hash_time * 1000, "ms")

# python -m tests.performance_test