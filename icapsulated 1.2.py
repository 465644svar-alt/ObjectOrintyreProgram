class Test():
    def public_func (self):
       print("public func")
    def _protected_func(self):
        print("protected func")
    def __private_func(self):
        print("private func")

test = Test()

test.public_func()
test._protected_func()
test._Test__private_func()