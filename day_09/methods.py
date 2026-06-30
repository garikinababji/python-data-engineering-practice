=============================================
# Topic:   __init__
# Author: Garikina Babji
# Purpose: Practice for GCP Data Engineering
=============================================

class Customer:

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print("Welcome", self.name)

customer = Customer("Babji")

customer.welcome()
