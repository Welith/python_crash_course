from collections import namedtuple

class Library():
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def addBooks(self, addedBooks):
        for book in addedBooks:
            self.books.append(book)

    
    def deleteBooks(self):
        self.books.clear()

    def deleteBook(self, selectedBook):
        self.books.pop(selectedBook)

    def searchByAuthor(self, author):
        written_by_author = []
        for book in self.books:
            if book.author == author:
                written_by_author.append(book)
        return written_by_author

library = Library()

Book = namedtuple('Book', 'title author ISBN release_date')

library.addBooks([Book("Gosho", "ivan", "21391238", "29/09/95"), Book("Gosho", "GoSho", "21391238", "29/09/95")])
library.deleteBooks()
print(library.searchByAuthor("ivan"))

