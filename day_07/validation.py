=============================================
# Topic:  validation
# Author: Garikina Babji
# Purpose: Practice for GCP Data Engineering
=============================================



def is_valid_salary(salary):
    return salary >= 50000

import validation

print(validation.is_valid_salary(60000))
print(validation.is_valid_salary(30000))
