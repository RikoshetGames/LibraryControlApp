import json
import os


class Book:
    def __init__(self, book_id, title, author, year, status='в наличии'):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        return {
            "id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Book(data['id'], data['title'], data['author'], data['year'], data['status'])

    def __str__(self):
        return f"ID: {self.book_id}, Название: {self.title}, Автор: {self.author}, Год: {self.year}, Статус: {self.status}"


class Library:
    def __init__(self, filename='library.json'):
        self.books = []
        self.next_id = 1
        self.filename = filename
        self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.books = [Book.from_dict(book) for book in data]
                if self.books:
                    self.next_id = max(book.book_id for book in self.books) + 1

    def save_books(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([book.to_dict() for book in self.books], f, ensure_ascii=False, indent=4)

    def add_book(self, title, author, year):
        book = Book(book_id=self.next_id, title=title, author=author, year=year)
        self.books.append(book)
        self.next_id += 1
        self.save_books()
        print(f"Книга '{title}' добавлена в библиотеку.")

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                self.save_books()
                print(f"Книга с ID {book_id} удалена.")
                return
        print("Книга не найдена.")

    def search_books(self, search_term):
        results = [book for book in self.books if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower() or search_term == str(book.year)]
        if not results:
            print("Книги не найдены.")
        else:
            for book in results:
                print(book)

    def display_books(self):
        if not self.books:
            print("Нет доступных книг.")
            return
        for book in self.books:
            print(book)

    def change_status(self, book_id, new_status):
        if new_status not in ['в наличии', 'выдана']:
            print("Неверный статус! Используйте 'в наличии' или 'выдана'.")
            return
        for book in self.books:
            if book.book_id == book_id:
                book.status = new_status
                self.save_books()
                print(f"Статус книги с ID {book_id} изменен на '{new_status}'.")
                return
        print("Книга не найдена.")
