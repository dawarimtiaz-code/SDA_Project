import csv

def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]
