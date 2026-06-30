=============================================
# Topic:  csv_as_dictionary
# Author: Garikina Babji
# Purpose: Practice for GCP Data Engineering
=============================================

import csv

with open("D:\\GCP_2026\\practice\\customers_csv.txt", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)

