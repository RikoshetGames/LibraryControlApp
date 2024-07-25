from book import Library


def interface():
    library = Library()
    while True:
        print("\nВыберите действие:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Отобразить все книги")
        print("5. Изменение статуса книги")
        print("6. Выход")

        choice = input("Ваш выбор: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            library.add_book(title, author, year)

        elif choice == '2':
            book_id = int(input("Введите ID книги, которую нужно удалить: "))
            library.remove_book(book_id)

        elif choice == '3':
            search_term = input("Введите название, автора или год для поиска: ")
            library.search_books(search_term)

        elif choice == '4':
            library.display_books()

        elif choice == '5':
            book_id = int(input("Введите ID книги: "))
            new_status = input("Введите новый статус (в наличии/выдана): ").lower()
            library.change_status(book_id, new_status)

        elif choice == '6':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор, попробуйте еще раз.")