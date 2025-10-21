#Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи,
# срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.
import datetime



class Task:
    def __init__(self,name, opisanie, end_time, status = True):
        self.name = name
        self.opisanie = opisanie
        self.end_time = end_time
        self.status = status
    def task_time(self):
        formatted_time = self.end_time.strftime("%H:%M")
        print(f"Задача должна быть выполнена до:, {formatted_time}")
    def show_status(self):
        if self.status == True:
            print("Задача выполнена")
        elif self.status == False:
            print("не выполнено")
point1 = Task("Поход в магазин", "Купить картошку", end_time=datetime.time(21,00), status=False)
print(point1.name, point1.opisanie, point1.end_time, point1.status)
point1.task_time()
point1.show_status()

