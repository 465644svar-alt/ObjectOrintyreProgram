#Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи,
# срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task():
    def __init__(self):
        self.tasks = []

    def add_task(self, deadline, description):
        self.tasks.append({'deadline': deadline,
                           'description': description,
                          "status":"unComplete"})
    def completed_task(self, description):
        found = False
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = "Complete"
                found = True
                print(f"Задача '{description}' отмечена как выполненная.")
        if not found:
            print(f"Задача '{description}' не найдена.")
    def show_tasks(self):
        print("текущие задачи")
        for task in self.tasks:
            if task ['status'] == "Complete":
                print(f"{task['description']} - {task['deadline']}")
t = Task()
t.add_task("05.05.2025", "Пробежать 700км")
t.add_task("05.05.2025", "Купить арбуз")
t.add_task("05.05.2025", "Прочитать Книгу")
t.completed_task("Купить арбуз")
t.show_tasks()


