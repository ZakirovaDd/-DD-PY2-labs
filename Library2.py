BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:

    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages

    """
         Создание и подготовка к работе объекта "Книга"
        :param id_: id_ книги
        :param name: Имя книги
        :param pages: Кол-во страниц в книге
    """

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'


class Library:
    book_count: int = 1

    def __init__(self, books: list[Book] = None):
        if books is None:
            books = []
        self.books = books

    """
         Создание и подготовка к работе объекта "Библиотека"
            :param books: список книг, т.е. список объктов класса Book
    """

    def get_index_by_book_id(self, id_: int) -> int:
        """
            Метод, возвращающий индекс книги в списке по id
                :param id_: id
                :raise ValueError: Если книги нет, то вызывается ошибка
                :return: индекс книги
        """
        for index, book in enumerate(self.books):
            if book.id_ == id_:
                #print (id_, index) - проверка
                return index
        if book not in range(1, len(self.books)):
            raise ValueError(f'Книги с запрашиваемым id не существует')

    def get_next_book_id(self) -> int:
        """
            Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
                :return Если книги нет, то возвращается 1
                :return: количество книг в библиотеке
         """
        if not len(self.books) == 0:
            return self.books[-1].id_+self.book_count
        else:
            return self.book_count


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
