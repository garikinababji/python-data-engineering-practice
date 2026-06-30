=============================================
# Topic:  Exception Handling
# Author: Garikina Babji
# Purpose: Practice for GCP Data Engineering
=============================================

try:
    with open("D:\\GCP_2026\\practice\\customers_csv2.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist")
