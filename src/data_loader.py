import csv
from pathlib import Path

def load_offers():
    current_folder = Path(__file__).resolve().parent
    project_folder = current_folder.parent
    file_path = project_folder / "data" / "discount_offers.csv"
    offers = []

    with open(file_path, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            offers.append(row)
            
    return offers
