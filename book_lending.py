from datetime import datetime
import random

class Book:

    """ A class representing a collection of books. """

    # class variables
    on_shelf = []
    on_loan = []

    # class methods
    @classmethod
    def create(cls, title, author, isbn):
        new_book = Book(title, author, isbn)
        cls.on_shelf.append(new_book)
        return new_book

    @classmethod
    def browse(cls):
        if len(cls.on_shelf) != 0:
            return random.choice(cls.on_shelf)
        else:
            return "There are no more books to loan!"

    @classmethod
    def current_due_date(cls):
        now = datetime.now()
        two_weeks = 60 * 60 * 24 * 14 # two weeks expressed in seconds
        future_timestamp = now.timestamp() + two_weeks
        return datetime.fromtimestamp(future_timestamp)

    @classmethod
    def overdue(cls):
        overdue_books = []
        for book in cls.on_loan:
            if book.due_date < datetime.now():
                overdue_books.append(book)
        return overdue_books

    # instance methods
    def __init__(self, title, author, isbn):
        # instance variables
        self.title = title
        self.author = author
        self.isbn = isbn
        self.due_date = None

    def borrow(self):
        if self.lent_out():
            return False
        else:
            self.due_date = Book.current_due_date()
            Book.on_shelf.remove(self)
            Book.on_loan.append(self)
            return True

    def lent_out(self):
        return self in Book.on_loan

    def return_to_library(self):
        if not self.lent_out():
            return False
        else:
            self.due_date = None
            Book.on_loan.remove(self)
            Book.on_shelf.append(self)
            return True
