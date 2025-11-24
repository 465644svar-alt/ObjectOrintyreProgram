class Dog:
    def speak(self):
        return "Gaw - gaw - gaw"
class Cat:
    def speak(self):
        return "Meow - meow - meow"
def animal_speak(people):
    print(people.speak())

dog = Dog()
cat = Cat()
animal_speak(dog)
animal_speak(cat)

# def soup(animal):
#  for animal in animals:
#     animal.speak()