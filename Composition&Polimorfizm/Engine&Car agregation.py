class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    def __str__(self):
        return f"{self.horsepower} horsepower"

class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine
    def __str__(self):
        return f"Car - {self.model}, engine = {self.engine}"
engine = Engine(280)
print(engine)
car = Car("Toyota", engine)

print(car)