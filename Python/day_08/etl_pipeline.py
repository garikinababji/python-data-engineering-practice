=============================================
# Topic:  etl_pipeline
# Author: Garikina Babji
# Purpose: Practice for GCP Data Engineering
=============================================

import csv

try:
    with open(r"D:\GCP_2026\practice\sample_csv_3.txt", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(row["name"])

except FileNotFoundError:
    print("Customer file not found")

except KeyError:
    print("Required column is missing")

finally:
    print("ETL Job Completed")
