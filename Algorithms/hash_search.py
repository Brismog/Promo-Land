def hash_function(brand_name, table_size):
    total = 0

    brand_name = brand_name.lower()
    for character in brand_name:
        total += ord(character) # Convert character to ASCII

    index = total % table_size # Remainder
    return index
    
# print(hash_function("Nike", 10)),print(hash_function("Apple", 10)),print(hash_function("Samsung", 10))
# python -m hash_search.py

class HashTable:

    def __init__(self, table_size):

        self.table_size = table_size
        self.table = [None] * table_size
        
    def insert(self, offer):
        brand_name = offer["brand_name"]
        index = hash_function(brand_name, self.table_size)

        for i in range(self.table_size):
            if self.table[index] is None:

                self.table[index] = [brand_name, [offer]]
                return
            
            elif self.table[index][0].lower() == brand_name.lower(): # If already exist

                self.table[index][1].append(offer)
                return

            index = (index + 1) % self.table_size # Next position/ Wrap around if on last index

    def search(self, brand_name):
        index = hash_function(brand_name, self.table_size)

        for i in range(self.table_size): # If no brand there
            if self.table[index] is None:
                return[]

            elif self.table[index][0].lower() == brand_name.lower(): # Return if exist
                return self.table[index][1]

            index = (index + 1) % self.table_size # Next position

        return []

