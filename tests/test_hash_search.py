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
print(hash_table.table[3][1]) # index 3(Nike), Index 1(offer)


print("\nCollision Test:") # Test collision handling
print("Nike index:", hash_function("Nike", 10))
print("Kine index:", hash_function("Kine", 10))
print("Nike stored at index 3")
print("Kine stored at index 4")


print("\nCase-Insensitive Search Test:") # Test case insensitive search
print(hash_table.search("nike"))


print("\nCollision Search Test:") # Test searching for the collision brand
print(hash_table.search("Kine"))

# python -m hash_search.py