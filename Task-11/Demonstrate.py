class Father:
    def father_method(self):
        print("Father Method")

class Mother:
    def mother_method(self):
        print("Mother Method")

class Child(Father, Mother):
    pass

c = Child()
c.father_method()
c.mother_method()