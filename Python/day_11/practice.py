=============================================
# Topic:  Practice on MAP(), Filter(),lambda
# Author: Garikina Babji
# Purpose: Practice for GCP Data Engineering
=============================================

employees = [
    {"name":"Ravi","salary":30000},
    {"name":"Sita","salary":70000},
    {"name":"Babji","salary":60000},
]

'''
emp=list(filter(lambda x: x["salary"]>=50000, employees))


emp_name = list(map(lambda x: x["name"],emp))

print(emp_name)

'''


emp = list(
    filter(
        lambda employee: employee["salary"] >= 50000,
        employees
    )
)

emp_name = list(
    map(
        lambda employee: employee["name"],
        emp
    )
)
print(emp_name)
