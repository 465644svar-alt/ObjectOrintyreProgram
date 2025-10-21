class Warrior:
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f'{self.name} Лег спать')
        self.endurance += 2

    def eat(self):
        print(f'{self.name} Покушал')
        self.power += 5

    def hit(self):
        print(f'{self.name} Бьет')
        self.power -= 1
        self.endurance = -6

    def walk(self):
        print(f'{self.name} Гуляет')

    def info(self):
        print(f"Имя воина: {self.name}")
        print(f"Сила воина: {self.power}")
        print(f"Выносливость воина: {self.endurance}")
        print(f"Цвет волос воина: {self.hair_color}")

# def __init__(self, name, power, endurance, hair_color):
war1 = Warrior("Валера", 100, 45, "Каштановый")
war2 = Warrior("Кларк кент", 999, 999, "Черный")

war1.sleep()
war1.eat()
war1.walk()
war1.hit()
print(war1.name, war1.power, war1.endurance, war1.hair_color)
war1.info()

war2.sleep()
war2.eat()
war2.walk()
war2.hit()
print(war2.name, war2.power, war2.endurance, war2.hair_color)
war2.info()


