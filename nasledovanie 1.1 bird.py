from traceback import walk_stack


class Pigeon():
    def __init__(self,name,voice,color):
        self.name = name
        self.voice = voice
        self.color = color
    def fly(self):
        print(f"{self.name} летает")
    def eat(self):
        print(f"{self.name} кушает")
    def sing(self):
        print(f"{self.name} поет")
    def info(self):
        print(f"{self.name} - имя")
        print(f"{self.voice} - голос")
        print(f"{self.color} - окрас птицы")
# bird1 = Bird("Гошан","кукареку","пестрый")
# bird1.info()
class Bird(Pigeon):
    def __init__(self,name,voice,color, favorite_food):
        super().__init__(name, voice, color)
        self.favorite_food = favorite_food
    def walk(self):
        print(f"{self.name} -  на пробежке")





bird2 = Bird("Олежка", "курлысимо", "зеленый", "хлебушек")
bird3 = Pigeon("Маша", "чик чирик", "фиолетовый")
bird2.info()
bird2.walk()
bird2.sing()
bird3.info()