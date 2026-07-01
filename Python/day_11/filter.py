#=============================================
# Topic:  Filter and Transform Data
# Author: Garikina Babji
# Purpose: Practice for GCP Data Engineering
#=============================================

# filter() selects only matching elements.

numbers = [1,2,3,4,5,6]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)


