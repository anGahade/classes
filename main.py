class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.name}' by {self.author}, Year: {self.year}"


class Library:
    books = []

    def add_book(self, book):
        self.books.append(book)

    def __str__(self):
        return "\n".join(str(book) for book in self.books)


book1 = Book("Harry Potter", "J.K. Rowling", 1997)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 1937)
book3 = Book("Pride and Prejudice", "Jane Austen", 1813)


library = Library()


library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


print(library)
