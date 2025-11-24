# Создайте класс Author и класс Book. Класс Book должен использовать композицию для включения автора в качестве объекта.


class Author():
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def book_info(self):
        print(f"Книга автора {self.author.name}, Произведение {self.title}")
author = Author("Kianu Rivz","Serb")
book = Book("Matrix", author)
print(author.name)
book.book_info()