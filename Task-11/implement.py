class Parent:
    def display(self):
        print("Parent Class")

class Child(Parent):
    def display(self):
        print("Child Class")

obj = Child()
obj.display()