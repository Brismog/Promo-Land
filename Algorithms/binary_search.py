def binary_search(offers, brand_name):

    def get_brand_name(offer):
        return offer["brand_name"].lower()
    
    sorted_offers = sorted(offers, key=get_brand_name)
    brand_name = brand_name.strip().lower() # Remove spaces, make lower case

    left = 0
    right = len(sorted_offers) - 1 # Ending position
    comparisons = 0

    while left <= right:
        middle = (left + right) // 2 
        middle_brand = sorted_offers[middle]["brand_name"].lower()

        matching_offers = []
        comparisons += 1  
        index = middle

        if middle_brand == brand_name:
            while index >= 0:
                current_brand = sorted_offers[index]["brand_name"].lower()

                if current_brand != brand_name:
                    break
                matching_offers.append(sorted_offers[index]) # Add the offer

                index -= 1 # Move left
                index = middle + 1 # Move right for leftovers 

            while index < len(sorted_offers):
                current_brand = sorted_offers[index]["brand_name"].lower()

                if current_brand != brand_name:
                    break
                matching_offers.append(sorted_offers[index])

                index += 1 # Move right
            return matching_offers, comparisons
        
        elif brand_name < middle_brand: # If brands name smaller, go left
            right = middle - 1

        else:
            left = middle + 1 # Otherwise, go right

    return [], comparisons # Empty if not found