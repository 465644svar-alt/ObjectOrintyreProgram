class Test():
    def __init__(self):
        self.public = "публичный атрибут"
        self._protected = "защищенный атрибут"
        self.__privated = "приватный атрибут"
    def get_private(self):
        return self.__privated
    def set_private(self,value):
        self.__privated = value

test = Test()
print(test.public)
print(test._protected)
print(test.get_private())
test.set_private("теперь мы получили значение приватного атрибута")
print(test.get_private())