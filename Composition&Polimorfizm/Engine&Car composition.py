class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    def __str__(self):
        return f"{self.horsepower} horsepower"

class Car:
    def __init__(self, model, engine_horsepower):
        self.model = model
        self.engine = Engine(engine_horsepower)

    def __str__(self):
        return f"Car - {self.model}, engine = {self.engine}"

car = Car("Toyota", 250)
engine = Engine(280)
print(engine.horsepower)

print(car.model)
print(car.engine)
print(car)

print(car.model)                    # Toyota
print(car.engine.horsepower)        # 250 - обращаемся к атрибуту двигателя