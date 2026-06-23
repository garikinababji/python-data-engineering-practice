import csv

with open("D:\\GCP_2026\\practice\\customers_csv.txt", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"])
