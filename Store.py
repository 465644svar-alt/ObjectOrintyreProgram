# 1. Создай класс `Store`:
# -Атрибуты класса:
# - `name`: название магазина.
# - `address`: адрес магазина.
# - `items`: словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`.
# - Методы класса:
# - `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`.
# -  метод для добавления товара в ассортимент.
# - метод для удаления товара из ассортимента.
# - метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
# - метод для обновления цены товара.
# 2. Создай несколько объектов класса `Store`:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
# 3. Протестировать методы:
class Store:
    def __init__(self, name, address,items = None):
        self.name = name
        self.address = address
        self.items = items if items is not None else {}
    def add_product(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар: {item_name} добавлен по цене {price}")
    def remove_product(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар {item_name} - Удален")
        else:
            print(f"Товар {item_name} -  Не найден")

    def get_price(self, item_name):
        """Возвращает цену товара или None, если товара нет."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара, если он существует."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена на '{item_name}' обновлена до {new_price} руб.")
        else:
            print(f"Товар '{item_name}' не найден, невозможно обновить цену.")

    def show_products(self):
        """Выводит список всех товаров и цен."""
        if not self.items:
            print("В магазине нет товаров.")
        else:
            print(f"\nСписок товаров магазина '{self.name}':")
            for name, price in self.items.items():
                print(f"- {name}: {price} руб.")
# 🧪 Пример использования
store1 = Store("Черкизка", "Ленина 20", {"арбуз": 20})

store1.show_products()
store1.add_product("яблоко", 15)
store1.add_product("дыня", 30)
store1.add_product("кокос", 35)
store1.add_product("апельсин", 44)
store1.add_product("тыблоки", 11)
store1.show_products()

print("\nЦена арбуза:", store1.get_price("арбуз"))
print("Цена банана:", store1.get_price("банан"))  # товара нет → None

store1.update_price("арбуз", 25)
store1.remove_product("дыня")
store1.show_products()


