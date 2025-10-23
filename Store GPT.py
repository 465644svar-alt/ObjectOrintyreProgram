import datetime

class Store:
    def __init__(self, name, address, items=None):
        self.name = name
        self.address = address
        self.items = items if items is not None else {}

    def add_product(self):
        """Добавляет новый товар через ввод пользователя."""
        item_name = input("Введите название товара: ").strip()
        price = input("Введите цену товара: ").strip()
        try:
            price = float(price)
            self.items[item_name] = price
            print(f"✅ Товар '{item_name}' добавлен по цене {price} руб.")
        except ValueError:
            print("⚠️ Ошибка: цена должна быть числом!")

    def remove_product(self):
        """Удаляет товар по названию."""
        item_name = input("Введите название товара для удаления: ").strip()
        if item_name in self.items:
            del self.items[item_name]
            print(f"🗑️ Товар '{item_name}' удалён.")
        else:
            print(f"⚠️ Товар '{item_name}' не найден.")

    def get_price(self):
        """Выводит цену товара по названию."""
        item_name = input("Введите название товара: ").strip()
        price = self.items.get(item_name)
        if price is not None:
            print(f"💰 Цена на '{item_name}': {price} руб.")
        else:
            print(f"⚠️ Товар '{item_name}' отсутствует.")

    def update_price(self):
        """Обновляет цену товара."""
        item_name = input("Введите название товара для обновления: ").strip()
        if item_name in self.items:
            new_price = input(f"Введите новую цену для '{item_name}': ").strip()
            try:
                new_price = float(new_price)
                self.items[item_name] = new_price
                print(f"🔁 Цена на '{item_name}' обновлена до {new_price} руб.")
            except ValueError:
                print("⚠️ Ошибка: цена должна быть числом!")
        else:
            print(f"⚠️ Товар '{item_name}' не найден.")

    def show_products(self):
        """Показывает все товары."""
        if not self.items:
            print("🛒 В магазине нет товаров.")
        else:
            print(f"\n📋 Список товаров магазина '{self.name}':")
            for name, price in self.items.items():
                print(f"— {name}: {price} руб.")
            print()

# ---------------------------------------------------

def menu():
    store = Store("Черкизка", "Ленина 20", {"арбуз": 20, "дыня": 30})

    while True:
        print("""
============================
      🏪 МЕНЮ МАГАЗИНА
============================
1. Показать все товары
2. Добавить товар
3. Удалить товар
4. Узнать цену товара
5. Обновить цену
0. Выйти
============================
""")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            store.show_products()
        elif choice == "2":
            store.add_product()
        elif choice == "3":
            store.remove_product()
        elif choice == "4":
            store.get_price()
        elif choice == "5":
            store.update_price()
        elif choice == "0":
            print("👋 Выход из программы. До свидания!")
            break
        else:
            print("⚠️ Ошибка: введите число от 0 до 5.")

# Запуск программы
if __name__ == "__main__":
    menu()
