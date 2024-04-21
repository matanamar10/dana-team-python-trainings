# book.py

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def update_details(self, title=None, author=None, isbn=None):
        if title:
            if isinstance(title, str):
                self.title = title
        if author:
            if isinstance(author, str):
                self.author = author
        if isbn:
            if isinstance(isbn, str):
                self.isbn = isbn
