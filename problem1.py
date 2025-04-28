# Q.No.1:- You are working on a Library Management System where books are represented as objects. How would you create a Book class with attributes like title, author, and available (defaulting to True)? Can you implement methods to borrow and return a book and demonstrate borrowing and returning one using two book objects?

class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False
            print(f"You have borrowed '{self.title}'")
        else:
            print(f"'{self.title}' is currently not available.")

    def return_book(self):
        self.available = True
        print(f"You have returned '{self.title}'")

# Demo
book1 = Book("1984", "George Orwell")
book2 = Book("Python 101", "John Smith")

book1.borrow()
book1.return_book()
book2.borrow()
