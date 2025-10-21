# 5. **Создать класс `Car` с атрибутами `make`, `model`, `year`.**
#    Добавьте метод `display_info()`, который выводит информацию о машине.
#    Создайте объект и вызовите этот метод.
class Car:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year
    def display_info(self):
        print(f"Марка авто:{self.mark},Модель: {self.model},Год выпуска: {self.year}")

auto1 = Car("Subaru", "Impreza",2025)
print(auto1)
auto1.display_info()

