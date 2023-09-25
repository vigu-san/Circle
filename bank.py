class Bank():

    def __init__(self):
        self.customers = {}

    def makeAccount(self, accountnum, initial_bal = 0):
        if accountnum in self.customers:
            print("account already exists")
        else:
            self.customers[accountnum] = initial_bal
            print ("account created successfully")

    def deposit(self, accountnum, amount):
        if accountnum in self.customers:
            self.customers[accountnum] += amount
            print("deposit done")
        else:
            print("account doesn't exist")

    def withdraw(self, accountnum, amount):
        if accountnum in self.customers:
            if self.customers[accountnum] >= amount:
                self.customers[accountnum] -= amount
                print("amount withdrawn")
            else:
                print("insufficient funds")
        else:
            print("account doesn't exist")

    

