class Test():
    def __init__(self):
        self.public = "публичный атрибут"
        self._protected = "защищенный атрибут"
        self.__privated = "приватный атрибут"
test = Test()
print(test.public)
print(test._protected)
print(test._protected)
