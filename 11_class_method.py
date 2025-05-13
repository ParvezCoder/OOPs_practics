# 1. Class Methods
# Assignment:
# Create a class Book with a class variable total_books.
#  Add a class method increment_book_count()
# to increase the count when a new book is added.

class Book():
    total_books = 0
    def __init__(self, Title):
        self.Title = Title
        Book.increment_book_count()
    @classmethod    
    def increment_book_count(cls):
        cls.total_books += 1

bb = Book("Acchi kittab")
bb = Book("Acchi kittab")
bb = Book("Acchi kittab")
bb = Book("Acchi kittab")
print("Total book are: ", Book.total_books)