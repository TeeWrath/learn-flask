class BookShelf:
    def __init__(self, *books):
        self.books = books
        
    def __str__(self):
        return f"Bookshelf has a total of {len(self.books)} books"
    
class Book:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Book {self.name}"
    
book1 = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book1,book2)

print(shelf.books[0], shelf.books[1])