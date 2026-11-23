import csv
from pathlib import Path


# Create a function to load the offers.
def load_offers():

    # Find the location of this Python file.
    current_folder = Path(__file__).resolve().parent

    # Go back to the main project folder.
    project_folder = current_folder.parent

    # Find the CSV file.
    file_path = project_folder / "data" / "discount_offers.csv"

    # Create an empty list.
    offers = []

    # Open the CSV file.
    with open(file_path, "r", encoding="utf-8-sig") as file:

        # Read the CSV data.
        reader = csv.DictReader(file)

        # Read each row.
        for row in reader:

            # Add the row to our list.
            offers.append(row)

    # Return all offers.
    return offers