class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Balance =", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print("Balance =", self.balance)

b = BankAccount(1000)

b.deposit(500)
b.withdraw(300)