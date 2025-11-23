class Engine:
    def start(self):
        print("The engine is starting...")
    def stop(self):
        print("The engine is stopped...")
class Car:
    def __init__(self):
        self.engine = Engine()
    def start(self):
        self.engine.start()
    def stop(self):
        self.engine.stop()
my_car = Car()

my_car.start()
my_car.stop()