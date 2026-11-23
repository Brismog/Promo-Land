def hash_function(brand_name, table_size):

    total = 0

    brand_name = brand_name.lower()

    for character in brand_name:
        total += ord(character)

    index = total % table_size

    return index

# python -m tests.test_hash_search