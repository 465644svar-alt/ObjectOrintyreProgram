class Car:
    def __init__(self, make, model):

        self.public_make = make # Открытый атрибут
        self._protected_model = model # Защищенный атрибут
        self.__private_year = 2022 # Приватный атрибут

    def public_method(self):
        return f"Это открытый метод. Машина: {self.public_make} {self._protected_model}."

    def _protected_method(self):

        return "Это защищенный метод."

    def __private_method(self):
        return "Это приватный метод."
car = Car("Toyota", "Camry")
print(car.public_method())
print(car._protected_method())
#print(car.__private_method())


class ElectricCar(Car):
    def __init__ (self, make, model, battery_size):
        super() .__init__(make, model)
        self.battery_size = battery_size

#Также добавлен еще один метод get_details, которого изначально не было.
#Это метод для получения информации о производителе (public), модели машины (protected), и размере батареи (public).

def get_details(self):
    # Можно обратиться к открытому и защиценному атрибуту, но не к приватному
    details = f"{self.public_make} {self ._protected_model}, Батарея: {self.battery_size} kWh."
    # Нельзя напряную обратиться к __ private_method и __ private_year
    return details
tesla = ElectricCar('tesla', 'model s', 2000)
print(tesla.public_make)
print(tesla.public_method())

# Доступ к защищённому атрибуту (не рекомендуется, но возможно):
print(tesla._protected_model)
print(tesla._protected_method())

print(tesla._Car__private_year)