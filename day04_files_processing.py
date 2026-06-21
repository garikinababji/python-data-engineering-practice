# ==========================================
# Topic   : Python CSV files_processing
# Author  : Garikina Babji
# Purpose : Practice for GCP Data Engineering
# ==========================================

files = [
    "customers.csv",
    "orders.csv",
    "products.csv",
    "sales.csv",
    "returns.csv"
]

for file in files:
    print("Processing:", file)


    gcs_files = ["day1.csv", "day2.csv", "day3.csv"]

for file in gcs_files:
    print("Loading", file, "into BigQuery")
