class BankAccount:
    def display(self):
        print("Bank Account")

class SavingsAccount(BankAccount):
    def display(self):
        print("Savings Account")

class CurrentAccount(BankAccount):
    def display(self):
        print("Current Account")

s = SavingsAccount()
c = CurrentAccount()

s.display()
c.display()