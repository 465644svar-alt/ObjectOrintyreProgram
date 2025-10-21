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
        print(f'{self.name} Покушал'))
        self.power += 5

    def hit(self):
        print(f'{self.name} Бьет'))
        self.power -= 1
        self.endurance = -6

    def walk(self):
        print(f'{self.name} Гуляет'))

def info(self):
    print(f"Имя воина: {self.name}")
    print(f"Сила воина: {self.power}")
    print(f"Выносливость воина: {self.endurance}")
    print(f"Цвет волос воина: {self.hair_color}")


