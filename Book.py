from pydantic import BaseModel, conint

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

class Book(BaseModel):
    id_: conint(gt=0)
    name: str
    pages: conint(gt=0)
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


if __name__ == '__main__':
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)

    print(list_books)