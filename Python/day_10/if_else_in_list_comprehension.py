=============================================
# Topic:  if_else_in_list_comprehension
# Author: Garikina Babji
# Purpose: Practice for GCP Data Engineering
=============================================




numbers = [1,2,3,4,5]

result = [
    "Even" if i % 2 == 0 else "Odd"
    for i in numbers
]

print(result)
