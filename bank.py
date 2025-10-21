# 3. **Создать класс `BankAccount` с атрибутами `owner` и `balance`.**
#    Добавьте методы `deposit(amount)` и `withdraw(amount)`, которые изменяют баланс.
#    Проверьте работу методов.
class BankAccount:
    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance
        balance = 0
    def deposit(self, amount):
        self.balance += amount
        print(f"Счет пополнен. Сумма на счете {self.balance}")

    def withdraw(self, amount):
        if self.balance <= amount:
            print("Недостаточно средств для снятия")
        elif self.balance >= amount:
            self.balance -= amount
            print(f"Снятие успешно. Остаток на счете, {self.balance}")
client1 = BankAccount ("Valera",1000)
print(client1.balance)
client1.deposit(10000)
client1.withdraw(9000)
client1.withdraw(90000)
client1.deposit(100000)



