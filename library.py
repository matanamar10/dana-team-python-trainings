# library.py

from book import Book
from patron import Patron
from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.books = []
        self.teachers = {}
        self.students = {}
        self.borrowed_books = {}  # Dictionary to store borrowed books with due dates

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            # Remove from borrowed books if it's borrowed
            if book in self.borrowed_books:
                del self.borrowed_books[book]

    def add_teacher(self, teacher_name):
        if teacher_name not in self.teachers:
            self.teachers[teacher_name] = {}

    def get_students_for_teacher(self, teacher_name):
        if teacher_name in self.teachers:
            return self.teachers[teacher_name]
        else:
            return {}

    def add_student_to_teacher(self, teacher_name, student_name):
        if teacher_name in self.teachers:
            teacher = self.teachers[teacher_name]
            teacher[student_name] = student_name

    def remove_student_from_teacher(self, teacher_name, student_name):
        if teacher_name in self.teachers:
            teacher = self.teachers[teacher_name]
            if student_name in teacher:
                del teacher[student_name]
                print(f"Removed {student_name} from {teacher_name}'s list.")
            else:
                print(f"{student_name} is not associated with {teacher_name}.")
        else:
            print(f"No such teacher named {teacher_name}.")

    def borrow_book(self, book, patron):
        if book in self.books and patron in self.students:
            if book not in self.borrowed_books:
                due_date = datetime.now() + timedelta(days=14)  # 14 days borrowing period
                self.borrowed_books[book] = due_date
                return True, due_date
            else:
                return False, self.borrowed_books[book]
        else:
            return False, None

    def return_book(self, book):
        if book in self.borrowed_books:
            del self.borrowed_books[book]

    def calculate_fine(self, book):
        if book in self.borrowed_books:
            due_date = self.borrowed_books[book]
            if datetime.now() > due_date:
                days_overdue = (datetime.now() - due_date).days
                return days_overdue * 0.50  # Fine of $0.50 per day overdue
            else:
                return 0
        else:
            return None

    def search_books(self, title=None, author=None, isbn=None):
        results = []
        for book in self.books:
            if (not title or title.lower() in book.title.lower()) and \
                    (not author or author.lower() in book.author.lower()) and \
                    (not isbn or isbn == book.isbn):
                results.append(book)
        return results
