=============================================
# Topic: Python for_loop
# Author: Garikina Babji
# Purpose: Practice for GCP Data Engineering
=============================================

files = [
    "customers.csv",
    "orders.csv",
    "invalid.txt",
    "sales.csv"
]

for file in files:
    if file.endswith(".csv"):
        print("Processing", file)
