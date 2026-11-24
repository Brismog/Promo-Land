def binary_search(offers, brand_name):

    def get_brand_name(offer):
        return offer["brand_name"].strip().lower()

    # Sort the offers by brand name before searching
    sorted_offers = sorted(offers, key=get_brand_name)
    brand_name = brand_name.strip().lower()

    left = 0
    right = len(sorted_offers) - 1
    comparisons = 0

    while left <= right:
        middle = (left + right) // 2
        middle_brand = sorted_offers[middle]["brand_name"].lower()

        comparisons += 1

        if middle_brand == brand_name:
            matching_offers = [sorted_offers[middle]]
            left_index = middle - 1
            left_matches = []

            # Check if there are more offers with the same brand on the left
            while left_index >= 0:
                comparisons += 1
                current_brand = sorted_offers[left_index]["brand_name"].lower()

                if current_brand != brand_name:
                    break

                left_matches.append(sorted_offers[left_index])
                left_index -= 1

            left_matches.reverse()
            matching_offers = left_matches + matching_offers

            right_index = middle + 1

            # Check for any other matching offers on the right
            while right_index < len(sorted_offers):
                comparisons += 1
                current_brand = sorted_offers[right_index]["brand_name"].strip().lower()

                if current_brand != brand_name:
                    break

                matching_offers.append(sorted_offers[right_index])
                right_index += 1

            return matching_offers, comparisons

        elif brand_name < middle_brand:
            right = middle - 1  # Search the left half

        else:
            left = middle + 1  # Search the right half

    return [], comparisons