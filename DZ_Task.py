#Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи,
# срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.
import datetime


tasks =[]

class Task:
    def __init__(self,name, opisanie, end_time, status = False):
        self.name = name
        self.opisanie = opisanie
        self.end_time = end_time
        self.status = status
    def task_time(self):
        formatted_time = self.end_time.strftime("%H:%M")
        print(f"Задача должна быть выполнена до:, {formatted_time}")
    def show_status(self):
        if self.status:
            print("✅Задача выполнена")
        else:
            print("❌ Не выполнено")
    def task_completed(self):
        self.status = True
    def __str__(self):
        status_text = "✅Выполнено" if self.status else "❌ Не выполнено"
        time_text = self.end_time.strftime("%H:%M")
        return(f"{self.name}: {self.opisanie} (Выполнить до:{time_text}) Статус{status_text}")
first_task = Task("Сходить в магазин", "Купить картошки", datetime.time(21,00), False)
tasks.append(first_task)
second_task = Task("Сходить в парк", "Прочитать книгу", datetime.time(21,00), False)
tasks.append(second_task)

for task in tasks:
    print(task)


