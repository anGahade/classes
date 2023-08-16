"""
Створіть клас Book який має такі атрибути як рік видання, назву, автор та кількість сторінок.
Створіть статік метод який буде приймати список книжок та рік,
та повертати кількість книжок з цього списку які були опубліковані у цьому році.
"""


class Book:
    books = []

    def __init__(self, year, name, author, pages):
        self.year = year
        self.name = name
        self.author = author
        self.pages = pages

    @classmethod
    def add_book(cls, book):
        cls.books.append(book)

    @staticmethod
    def check_books(books, year):
        count = 0
        for book in books:
            if book.year == year:
                count += 1
        return count


book1 = Book(1997, "Harry Potter", "J.K. Rowling", 197)
book2 = Book(1937, "The Hobbit", "J.R.R. Tolkien", 937)
book3 = Book(1813, "Pride and Prejudice", "Jane Austen", 813)

Book.add_book(book1)
Book.add_book(book2)
Book.add_book(book3)

check_year = 1813
result = Book.check_books(Book.books, check_year)
print(f"Кількість книжок, опублікованих у {check_year} році: {result}")
