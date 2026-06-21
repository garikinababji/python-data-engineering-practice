files = [
    "customers.csv",
    "orders.csv",
    "invalid.txt",
    "sales.csv"
]

for file in files:
    if file.endswith(".csv"):
        print("Processing", file)