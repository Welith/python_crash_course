#TODO sorting multidimensional array with random key
class Book:
    def __init__(self, title, author, publisher,  ISBN, release_date):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.ISBN = ISBN
        self.release_date = release_date
    
    def getBookInfo(self):
        print(f'The book {self.title} by {self.author}, is published by {self.publisher} and was released {self.release_date}')

book = Book("Ivan", "Gosho", "Georg", 17628862, "29/09/1995")
book.getBookInfo()
