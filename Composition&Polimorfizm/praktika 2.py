import math


# Создать базовый класс Shape с методом area(), который просто возвращает 0.
# Создать несколько производных классов для разных форм (например, Circle, Rectangle, Square), каждый из которых переопределяет метод area().
# В каждом из этих классов метод area() должен возвращать площадь соответствующей фигуры.
# Написать функцию, которая принимает объект класса Shape и выводит его площадь.
class Shape():
    def __init__(self):
        self.figure = None
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.figure = "Круг"

    def area(self):
        return math.pi * self.radius ** 2
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.figure = "Прямоугольник"
    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side
        self.figure = "Квадрат"
    def area(self):
        return self.side ** 2
circle_1 = Circle(2)
print(circle_1.area())
rectangle_1 = Rectangle(4, 5)
print(rectangle_1.area())
square_1 = Square(3)
print(square_1.area())

ploshad = [Square(3), Rectangle(2,4), Circle(10)]
for p in ploshad:
    p.area()
    print(p.area())

def print_area(shape):
    print(f"Площадь фигуры = {shape.area()} - {shape.figure}")

print_area(Rectangle(4,5))
print_area(Circle(3))
print_area(Square(5))
