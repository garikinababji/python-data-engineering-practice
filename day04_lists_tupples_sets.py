=============================================
# Topic: Python lists_tupples_sets
# Author: Garikina Babji
# Purpose: Practice for GCP Data Engineering
=============================================

# Task 1
employees = ["Babji", "Ravi", "Sita", "Anil"]
print(employees)
print(employees[0])   # Babji
print(employees[2])   # Sita
employees.append("Kumar")
print(employees)
employees.remove("Ravi")
print(employees)


# Real time example for list on GCS pipeline
# Task 2
gcs_files = [
    "customers.csv",
    "orders.csv",
    "products.csv"
]

for file in gcs_files:
    print("Processing:", file)

# Task 3

# duplicate list
skills = {"Python", "SQL", "Python", "GCP"}

print(skills)
# Task 4

# dictionary practice
employee = {
    "id": 1001,
    "name": "Babji",
    "experience": 4,
    "role": "Data Engineer"
}
print(employee["name"])
print(employee["role"])


# Task 5
employee= {
"emp_id":101,
"emp_name" : "Babji",
"emp_salary": 10000
}
print(employee["emp_name"])
print(employee["emp_id"])

# Task 6
employee["emp_salary"] = 12000
print(employee["emp_salary"])
employee["emp_department"] = "Data Engineering"
print(employee["emp_department"])
print(employee["emp_name"])
print(employee["emp_salary"])

# Task 7

employee = ["Babji", "Ravi", "Sita"]

print(employee[0:3])   
employee.append("anil")
print(employee[0:4])
location = ("Hyderabad", "India")
print(location[0])


# Task 8
numbers = [1, 2, 3, 2, 4, 1, 5]
print(set(numbers))  # Output: {1, 2, 3, 4, 5}

customer = {
    "id": 101,
    "name": "Ravi",
    "city": "Hyderabad"
}
customer["country"] = "India"
print(customer["name"], customer["country"])

# Task 9
customers = [
    {"id": 1, "name": "Ravi", "city": "Hyderabad"},
    {"id": 2, "name": "Sita", "city": "Vijayawada"},
    {"id": 3, "name": "Anil", "city": "Hyderabad"}
]

for customer in customers:
	if customer["city"] == "Hyderabad":
		print(customer)
		

# Task 10

from operator import index


employees = ["Babji", "Ravi", "Sita", "Anil", "Kumar"]
print(len(employees))

# Task 11

from unicodedata import name


employees = ["Babji", "Ravi", "Sita", "Anil"] 
if "Sita" in employees:
	print("YES")


# Task 12	

employees = ["Babji", "Ravi", "Sita"]
for employee in employees:
	print(employee)
	
# Task 13

location = ("Hyderabad", "Telangana", "India")
print(location[0])
print(location[-1])
print(len(location))

# Task 14

cities = ["Hyderabad", "Chennai", "Hyderabad", "Bangalore", "Chennai"]
print(set(cities))

# Task 15

skills = {"Python", "SQL", "GCP"}
skills.add("Airflow")
print(skills)

# Task 16

employee = {
    "id": 101,
    "name": "Babji",
    "experience": 4
}

employee["experience"]=5
print(employee)

# Task 17

employee = {
    "id": 101,
    "name": "Babji",
    "city": "Hyderabad"
}
print(employee.keys())
print(employee.values())

# Task 18

from os import name


customers = [
    {"id": 1, "name": "Ravi", "city": "Hyderabad"},
    {"id": 2, "name": "Sita", "city": "Vijayawada"},
    {"id": 3, "name": "Anil", "city": "Hyderabad"},
    {"id": 4, "name": "Kumar", "city": "Chennai"}
]
for customer in customers:
	if customer["city"]=="Hyderabad":
		print(customer["name"])


# Task 19

customer_ids = [101, 102, 103, 101, 104, 102, 105]
unique_ids = set(customer_ids)
print(unique_ids)
print(sorted(unique_ids, reverse=True))
print(len(unique_ids))

# Task 20

student = {
    "id": 1,
    "name": "Babji",
    "course": "GCP Data Engineering",
    "duration": "3 Months",
    "completed_days": 4
}
print(student["name"],student["course"])
student["trainer"] = "ChatGPT"
print(student.keys())
print(student.values())

# Task 21

orders = [
    {"order_id": 1, "amount": 500},
    {"order_id": 2, "amount": 1500},
    {"order_id": 3, "amount": 300},
    {"order_id": 4, "amount": 2500}
]
for order in orders:
	if order["amount"]>=1000:
		print(order["order_id"])

# Task 22

products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mouse", "price": 500},
    {"id": 3, "name": "Keyboard", "price": 1500},
    {"id": 4, "name": "Monitor", "price": 12000}
]
for product in products:
	if product["price"]>=1000:
		print(product["name"])
