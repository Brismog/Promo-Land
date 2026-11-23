def linear_search(offers, brand_name):

    matching_offers = []
    comparisons = 0
    brand_name = brand_name.strip() # Remove spaces

    for offer in offers:
        comparisons += 1
        offer_brand = offer["brand_name"]

        if offer_brand.lower() == brand_name.lower(): # To ignore capital then add
            matching_offers.append(offer)

    return matching_offers, comparisons