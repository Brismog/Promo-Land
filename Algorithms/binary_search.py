# Create a function to search for offers using Binary Search
def binary_search(offers, brand_name):

    # Sort the offers by brand name
    sorted_offers = sorted(
        offers,
        key=lambda offer: offer["brand_name"].lower()
    )

    # Convert the search input to lowercase
    brand_name = brand_name.strip().lower()

    # Set the starting position
    left = 0

    # Set the ending position
    right = len(sorted_offers) - 1

    # Count the comparisons
    comparisons = 0

    # Search while there are items to check
    while left <= right:

        # Find the middle position
        middle = (left + right) // 2

        # Get the brand name in the middle
        middle_brand = sorted_offers[middle]["brand_name"].lower()

        # Count this comparison
        comparisons += 1

        # Check if we found the brand
        if middle_brand == brand_name:

            # Create a list for matching offers
            matching_offers = []

            # Move left to find the first matching offer
            index = middle

            while index >= 0:

                # Get the current brand
                current_brand = sorted_offers[index]["brand_name"].lower()

                # Stop if the brand does not match
                if current_brand != brand_name:
                    break

                # Add the offer
                matching_offers.append(sorted_offers[index])

                # Move one position to the left
                index -= 1

            # Move right to find the remaining offers
            index = middle + 1

            while index < len(sorted_offers):

                # Get the current brand.
                current_brand = sorted_offers[index]["brand_name"].lower()

                # Stop if the brand does not match
                if current_brand != brand_name:
                    break

                # Add the offer
                matching_offers.append(sorted_offers[index])

                # Move one position to the right
                index += 1

            # Return the matching offers and comparisons
            return matching_offers, comparisons

        # If the brand is alphabetically smaller
        # search the left half.
        elif brand_name < middle_brand:
            right = middle - 1

        # Otherwise, search the right half
        else:
            left = middle + 1

    # Return an empty list if we did not find the brand
    return [], comparisons