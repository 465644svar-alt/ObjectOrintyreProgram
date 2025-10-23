# store_demo.py
import datetime

class Store:
    def __init__(self, name: str, address: str, items: dict | None = None):
        """
        Инициализация магазина.
        items: словарь вида {"название_товара": цена, ...}
        """
        self.name = name
        self.address = address
        self.items = items if items is not None else {}

    # ----- Немедленный (программный) интерфейс -----
    def add_product(self, item_name: str, price: float):
        """Добавить товар с ценой (или обновить цену, если товар уже есть)."""
        self.items[item_name] = price
        print(f"[{self.name}] Товар '{item_name}' установлен/обновлён по цене {price}.")

    def remove_product(self, item_name: str):
        """Удалить товар по названию; если нет — вернуть False."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"[{self.name}] Товар '{item_name}' удалён.")
            return True
        else:
            print(f"[{self.name}] Товар '{item_name}' не найден — удаление невозможно.")
            return False

    def get_price(self, item_name: str):
        """Вернуть цену товара или None, если товара нет."""
        price = self.items.get(item_name)
        if price is None:
            print(f"[{self.name}] Товар '{item_name}' отсутствует. Возвращаю None.")
        else:
            print(f"[{self.name}] Цена на '{item_name}': {price}")
        return price

    def update_price(self, item_name: str, new_price: float):
        """Обновить цену существующего товара; вернёт True при успехе."""
        if item_name in self.items:
            old = self.items[item_name]
            self.items[item_name] = new_price
            print(f"[{self.name}] Цена '{item_name}' обновлена: {old} → {new_price}")
            return True
        else:
            print(f"[{self.name}] Товар '{item_name}' не найден — обновление невозможно.")
            return False

    def show_products(self):
        """Показать все товары и их цены в магазине."""
        print(f"\n📋 Список товаров магазина '{self.name}' ({self.address}):")
        if not self.items:
            print("  (в магазине нет товаров)")
            return
        for name, price in self.items.items():
            print(f"  - {name}: {price} руб.")
        print()  # пустая строка для читаемости

    # ----- Интерактивный интерфейс (через input) -----
    def add_product_interactive(self):
        """Добавление товара через ввод с клавиатуры."""
        item_name = input(f"[{self.name}] Введите название товара: ").strip()
        price_str = input(f"[{self.name}] Введите цену товара: ").strip()
        try:
            price = float(price_str)
        except ValueError:
            print("Ошибка: цена должна быть числом.")
            return
        self.add_product(item_name, price)


# ------------------- ТЕСТИРОВАНИЕ: создаём магазины и проверяем методы -------------------

# Создаём 3 магазина с начальными товарами
store_a = Store("Черкизка", "Ленина 20", {"арбуз": 20.0, "яблоко": 15.0})
store_b = Store("Уютный Дом", "Пушкина 5", {"хлеб": 25.0, "молоко": 55.0, "сыр": 180.0})
store_c = Store("ЭкоМаркет", "Советская 12", {"банан": 12.5})

# Показать содержимое всех магазинов
store_a.show_products()
store_b.show_products()
store_c.show_products()

# Тест: добавление товаров (программно)
store_a.add_product("дыня", 30.0)            # новый товар
store_b.add_product("молоко", 60.0)          # обновление цены молока (было 55.0)

# Тест: получить цену (существующего и несуществующего товара)
store_a.get_price("арбуз")                   # ожидаем 20.0
store_a.get_price("манго")                   # товара нет -> None

# Тест: обновление цены (существующего и несуществующего)
store_b.update_price("сыр", 200.0)           # успешно обновит
store_b.update_price("йогурт", 40.0)         # не существует -> False

# Тест: удаление товара
store_c.remove_product("банан")              # удаление успешное
store_c.remove_product("банан")              # теперь не найден

# Финальная печать состояния магазинов
store_a.show_products()
store_b.show_products()
store_c.show_products()
