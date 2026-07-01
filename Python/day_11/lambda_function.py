#=============================================
# Topic:  lambda functions
# Author: Garikina Babji
# Purpose: Practice for GCP Data Engineering
#=============================================

# Normal Function

def square(x):
    return x * x

print(square(5))


# Lambda Function

# Example 1

square = lambda x: x * x

print(square(5))


# Example 2
add = lambda a, b: a + b

print(add(10, 20))