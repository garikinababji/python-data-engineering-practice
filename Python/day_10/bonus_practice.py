=============================================
# Topic:  bonus practice
# Author: Garikina Babji
# Purpose: Practice for GCP Data Engineering
=============================================

# print only >50000

employees = [
    {"name":"Ravi","salary":30000},
    {"name":"Sita","salary":70000},
    {"name":"Babji","salary":60000},
    {"name":"Anil","salary":25000}
]
print([employee["name"] for employee in employees if employee["salary"]>50000])
