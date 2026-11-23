# Create a function to search for offers by brand
def linear_search(offers, brand_name):

    # Create an empty list to store matching offers
    matching_offers = []

    # Store the number of comparisons
    comparisons = 0

    # Remove spaces from the search input
    brand_name = brand_name.strip()

    # Go through every offer in the list
    for offer in offers:

        # Count each comparison
        comparisons += 1

        # Get the brand name from the current offer
        offer_brand = offer["brand_name"]

        # Compare the brand names
        # lower() makes the search ignore capital letters
        if offer_brand.lower() == brand_name.lower():

            # Add the offer to the matching list
            matching_offers.append(offer)

    # Return the results and the number of comparisons
    return matching_offers, comparisons