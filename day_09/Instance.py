=============================================
# Topic:  Instance
# Author: Garikina Babji
# Purpose: Practice for GCP Data Engineering
=============================================

class Customer:

    def __init__(self, name, city):

        self.name = name
        self.city = city

customer1 = Customer("Ravi", "Hyderabad")

print(customer1.name)
print(customer1.city)
