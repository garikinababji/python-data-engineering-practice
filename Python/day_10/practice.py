# This is a simple Python code that creates a list of numbers from 1 to 10 and then uses a list comprehension to filter and print the numbers that are in the range from 1 to 10.

from os import name


list=[1,2,3,4,5,6,7,8,9,10]
print([i for i in list if i in range(1,11)])



# Print even numbers from the list

list=[1,2,3,4,5,6,7,8,9,10]
print([i for i in list if i%2==0])

# Print squares of numbers from the list
list=[1,2,3,4,5,6,7,8,9,10]
print([i*i for i in list])


#uppercase of names in the list
names=["ravi","sita","babji"]
print([name.upper() for name in names])

# find odd and even numbers from the list
list=[1,2,3,4,5,6,7,8,9,10]
print(["Even" if i%2==0 else "Odd" for i in list])


# Filter employees with salary greater than 50000
employees = [
    {"name":"Ravi","salary":30000},
    {"name":"Sita","salary":70000},
    {"name":"Babji","salary":60000},
]
print([emp["name"] for emp in employees if emp["salary"] > 50000])