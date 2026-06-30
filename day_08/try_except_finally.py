=============================================
# Topic:  try_except_finally
# Author: Garikina Babji
# Purpose: Practice for GCP Data Engineering
=============================================

# Task 1 

try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program Ended")

# Task 2

try:
    age = int("abc")

except ValueError:
    print("Invalid Number")



# Task 3

employee = {
    "name": "Babji"
}

try:
    print(employee["city"])

except KeyError:
    print("Key Not Found")
