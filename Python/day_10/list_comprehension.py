# List Comprehension


numbers = [i for i in range(1, 6)]

print(numbers)


# Example 2 - Squares

square = []

for i in range(1, 6):
    square.append(i*i)

print(square)



# List Comprehension for Squares


square = [i*i for i in range(1,6)]

print(square)


# Example 3 - Even Numbers
even = [i for i in range(1,11) if i % 2 == 0]

print(even)

# Example 4 - Odd Numbers
odd = [i for i in range(1,11) if i % 2 != 0]    
print(odd)


# Example 5 - Uppercase

names = ["ravi","sita","babji"]

upper = [name.upper() for name in names]

print(upper)


# Real Data Engineering Example
# Imagine ETL pipeline.

# Input
customers = [
    {"name":"Ravi","status":"Active"},
    {"name":"Sita","status":"Inactive"},
    {"name":"Babji","status":"Active"}
]

# Need only active customers.
active = [
    customer["name"]
    for customer in customers
    if customer["status"] == "Active"
]

print(active)

