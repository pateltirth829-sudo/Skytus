class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print("Speed =", self.speed)

    def brake(self):
        self.speed -= 10
        print("Speed =", self.speed)

c = Car("Toyota", "Fortuner", 50)

c.accelerate()
c.brake()