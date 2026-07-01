#=============================================
# Topic:  map() transforms every element.
# Author: Garikina Babji
# Purpose: Practice for GCP Data Engineering
#=============================================

# map() transforms every element.

numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))

print(result)

# Without map()

numbers = [1,2,3,4]

result = []

for i in numbers:
    result.append(i * 2)

print(result)