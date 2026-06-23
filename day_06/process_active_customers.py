import csv

with open("D:\\GCP_2026\\practice\\customers_csv2.txt", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["status"] == "Active":
            print(row["name"])