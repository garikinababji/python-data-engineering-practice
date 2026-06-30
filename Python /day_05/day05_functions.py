=============================================
# Topic: Python functions
# Author: Garikina Babji
# Purpose: Practice for GCP Data Engineering
=============================================

# Task 1: Create a function called welcome that takes a name as an argument and prints a welcome message with that name.

def welcome(name):
    print(f"Welcome, {name}!")

welcome("babji")
welcome("Ravi")

# Task 2: Create a function called add that takes two numbers as arguments and returns their sum.

def add(a, b):
     return a+b
print(add(2,3))

# Task 3: Create a function called is_even that takes a number as an argument and returns True if the number is even, and False otherwise.

def is_even(num):
	if num%2==0:
		return True
	else:
		return False

print(is_even(10))
print(is_even(7))

# Task 4: Create a function called print_customer that takes a customer dictionary as an argument and prints the customer's name and city.

customer = {
    "name": "Ravi",
    "city": "Hyderabad"
}

def print_customer(customer):
    print(customer["name"])
    print(customer["city"])

print_customer(customer)


# Task 5: Create a function called is_high_salary that takes a salary as an argument and returns True if the salary is greater than or equal to 50000, and False otherwise.

def is_high_salary(salary):
    if salary>= 50000:
	    return True
    else:
        return False
print(is_high_salary(60000))
print(is_high_salary(35000))
