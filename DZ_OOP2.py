class User:
    def __init__(self, user_id: int, name: str):
        self._id = user_id
        self._name = name
        self._access_level = "user"
    def get_id(self) :
        return self._id
    def get_name(self) :
        return self._name
    def get_access_level(self):
        return self._access_level
    def set_name(self, new_name)    :
        if new_name and len(new_name)>0 :
            self._name = new_name

    def user_info(self):
        return f"ID:{self._id}, Имя:{self._name}, Уровень доступа: {self._access_level}"

# 2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа,
# специфичный для администраторов ('admin'). Класс должен также содержать методы add_user и remove_user, которые
# позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).
class Admin(User):
    def __init__(self, user_id: int, name: str):
        super().__init__(user_id, name)
        self._access_level = "admin"
        self._user_list:list[User] = []
    def add_user(self, user: User) -> None:
        # проверяем тип и отсутствие пользователя с таким же ID
        if not isinstance(user, User):
            print("Ошибка: передан не экземпляр User")
            return

        if any(u.get_id() == user.get_id() for u in self._user_list):
            print(f"Ошибка: пользователь с ID {user.get_id()} уже существует")
            return

        self._user_list.append(user)
        print(f"Пользователь: {user.get_name()} (ID {user.get_id()}) добавлен в систему")
    def remove_user(self, user_id):
        for user in self._user_list:
            if user.get_id() == user_id:
                self._user_list.remove(user)
                print(f"Пользователь {user.get_name()}(ID {user_id}) удален из системы")
                return
        print(f"Пользователь с ID {user_id} не найден")

    def list_users(self):
        print("\n--- Список пользователей системы ---")
        for user in self._user_list:
            print(user.user_info())
        print(f"Всего пользователей: {len(self._user_list)}\n")

    def admin_info(self):
        return f"Администратор - ID: {self._id}, Имя: {self._name}"
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. Предоставь доступ к
# необходимым атрибутам через методы (например, get и set методы).

if __name__ == "__main__":
    # Создаем администратора
    admin = Admin(1, "Виктор")
    print(admin.admin_info())
    # Создаем обычных пользователей
    user1 = User(2, "Галина")
    user2 = User(3, "Алексей")
    user3 = User(4, "Мария")

    # Администратор добавляет пользователей в систему
    admin.add_user(user1)
    admin.add_user(user2)
    admin.add_user(user3)
    print(f"Имя пользователя user3: {user3.get_access_level()}")
    # Просматриваем список пользователей
    admin.list_users()

    # Удаляем пользователя
    admin.remove_user(2)

    # Снова просматриваем список
    admin.list_users()

    # Информация о конкретных пользователях
    print("\n" + user1.user_info())
    print(user2.user_info())
    print(user3.user_info())




















#     def __init__(self, id, name, dostupid=False, _admin=True):
#         super() .__init__(id, name, dostupid = False)
#         self.id = id
#         self.name = name
#         self.dostupid = dostupid
#         self._admin = _admin
#
#     def admin_info(self):
#        dostup_text = "Open" if self.dostupid else "Close"
#        admin_text = "Администратор" if self._admin else "Недостаточно полномочий"
#        return f"Код пользователя {self.id}, Имя {self.name}, доступ: {dostup_text}, Права доступа: {admin_text}"
#
# admin1 = User(1, "Viktor", True, True)
# print(admin1.admin_info())