from Algorithms.hash_search import HashTable, hash_function

# Create offers, test Hash, create table, insert to the table, and display
offer_1 = {"brand_name": "Nike", "offer_title": "10% discount"}
offer_2 = {"brand_name": "Nike", "offer_title": "20% discount"}
offer_3 = {"brand_name": "Apple", "offer_title": "15% discount"}
offer_4 = {"brand_name": "Kine", "offer_title": "Test offer"}

print("Hash Function: ")
print("Nike:", hash_function("Nike", 10))
print("Apple:", hash_function("Apple", 10))
print("Samsung:", hash_function("Samsung", 10))
print("Kine:", hash_function("Kine", 10))

hash_table = HashTable(10)

hash_table.insert(offer_1)
hash_table.insert(offer_2)
hash_table.insert(offer_3)
hash_table.insert(offer_4)

print("\nHash Table:")
print(hash_table.table)


print("\nNike offers:")
print(hash_table.table[3][1]) # Index 3(Nike), Index 1(offer)


print("\nCollision Test:") # Test collision handling
print("Nike index:", hash_function("Nike", 10))
print("Kine index:", hash_function("Kine", 10))
print("Nike stored at index 3")
print("Kine stored at index 4")


print("\nSearch Test:") # Test for Nike
nike_offers, nike_comparisons = hash_table.search("Nike")
print("Nike offers:", nike_offers)
print("Comparisons:", nike_comparisons)


# Check what happens when searching for a brand that is not in the hash table
print("\nSearching for a brand that does not exist:")
unknown_offers, unknown_comparisons = hash_table.search("Adidas")
print("Offers found for Adidas:", unknown_offers)
print("Number of comparisons:", unknown_comparisons)


# Check if the search works when the brand name uses lowercase letters
print("\nTesting search with lowercase letters:")
nike_offers, nike_comparisons = hash_table.search("nike")
print("Nike offers:", nike_offers)
print("Number of comparisons:", nike_comparisons)


# Check if the hash table can still find an offer after a collision
print("\nTesting search after a collision:")
kine_offers, kine_comparisons = hash_table.search("Kine")
print("Kine offers:", kine_offers)
print("Number of comparisons:", kine_comparisons)


# Run the test using:
# python -m tests.test_hash_search