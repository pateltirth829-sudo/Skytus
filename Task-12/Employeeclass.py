class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name =", self.name)
        print("Salary =", self.salary)

e = Employee("Hiral", 30000)

e.display()