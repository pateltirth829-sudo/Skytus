class Circle:
    def area(self):
        print("Area of Circle")

class Rectangle:
    def area(self):
        print("Area of Rectangle")

def show_area(shape):
    shape.area()

c = Circle()
r = Rectangle()

show_area(c)
show_area(r)