#=============================================
# Topic:  Filter and Transform Data
# Author: Garikina Babji
# Purpose: Practice for GCP Data Engineering
#=============================================


# Real Data Engineering Example
#
employees = [
    {"name":"Ravi","salary":30000},
    {"name":"Sita","salary":70000},
    {"name":"Babji","salary":60000},
]

high_salary = list(filter(lambda emp: emp["salary"] >= 50000,employees))

print(high_salary)

# Transform Data
# Only names:

names = list(map(lambda emp: emp["name"],employees))

print(names)