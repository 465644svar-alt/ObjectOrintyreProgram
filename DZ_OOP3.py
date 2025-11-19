import json

# ---------- Базовый класс ----------
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Some generic animal sound"

    def eat(self):
        return f"{self.name} ест пищу."


# ---------- Подклассы ----------
class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        return f"{self.name} поёт: Чирик-чирик!"


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return f"{self.name} рычит: Р-р-р!"


class Reptile(Animal):
    def __init__(self, name, age, is_venomous):
        super().__init__(name, age)
        self.is_venomous = is_venomous

    def make_sound(self):
        return f"{self.name} шипит: Ш-ш-ш!"


# ---------- Полиморфизм ----------
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


# ---------- Сотрудники ----------
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")


# ---------- Класс Zoo (композиция) ----------
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк {self.name}.")

    def add_staff(self, employee):
        self.staff.append(employee)
        print(f"Сотрудник {employee.name} теперь работает в {self.name}.")

    def show_animals(self):
        print(f"\nЖивотные в зоопарке {self.name}:")
        for animal in self.animals:
            print(f"- {animal.name} ({animal.__class__.__name__})")

    def show_staff(self):
        print(f"\nСотрудники зоопарка {self.name}:")
        for emp in self.staff:
            print(f"- {emp.name} ({emp.__class__.__name__})")

    # ---------- Сохранение состояния ----------
    def save_to_file(self, filename):
        data = {
            "name": self.name,
            "animals": [
                {
                    "type": a.__class__.__name__,
                    "name": a.name,
                    "age": a.age,
                    "extra": a.__dict__
                }
                for a in self.animals
            ],
            "staff": [
                {
                    "type": e.__class__.__name__,
                    "name": e.name
                }
                for e in self.staff
            ]
        }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"\nДанные зоопарка сохранены в файл {filename}.")

    @staticmethod
    def load_from_file(filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        zoo = Zoo(data["name"])

        # восстановление животных
        for a in data["animals"]:
            cls = globals()[a["type"]]
            extra = a["extra"]
            animal = cls(**{k: v for k, v in extra.items() if k in cls.__init__.__code__.co_varnames})
            zoo.add_animal(animal)

        # восстановление сотрудников
        for e in data["staff"]:
            cls = globals()[e["type"]]
            employee = cls(e["name"])
            zoo.add_staff(employee)

        print(f"\nЗоопарк '{zoo.name}' загружен из файла {filename}.")
        return zoo


# ---------- Демонстрация работы ----------
if __name__ == "__main__":
    # создаём животных
    parrot = Bird("Кеша", 2, 0.3)
    lion = Mammal("Симба", 5, "золотистый")
    snake = Reptile("Наг", 4, True)

    # создаём сотрудников
    keeper = ZooKeeper("Анна")
    vet = Veterinarian("Игорь")

    # создаём зоопарк
    zoo = Zoo("Сафари Парк")

    zoo.add_animal(parrot)
    zoo.add_animal(lion)
    zoo.add_animal(snake)

    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    zoo.show_animals()
    zoo.show_staff()

    # демонстрация полиморфизма
    print("\nЗвуки животных:")
    animal_sound(zoo.animals)

    # взаимодействие сотрудников
    keeper.feed_animal(lion)
    vet.heal_animal(snake)

    # сохраняем и загружаем
    zoo.save_to_file("zoo_data.json")
    loaded_zoo = Zoo.load_from_file("zoo_data.json")
    loaded_zoo.show_animals()
