class Customer:

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print("Welcome", self.name)

customer = Customer("Babji")

customer.welcome()