# main.py

from book import Book
from patron import Patron
from library import Library

# Create some books
book1 = Book("Messi: The GOAT", "M. Amar", "9780743273565")
book2 = Book("From Zero TO Hero In Chiropractic", "A. Vitali", "9780061120084")
book3 = Book("Eyal Golan: My Real Love", "Ran LongSureName", "9780451524935")

# Create some patrons
patron1 = Patron("Meytar", 1001)
patron2 = Patron("Ariel", 1002)

# Create a library
library = Library()

# Add books and patrons to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_patron(patron1)
library.add_patron(patron2)

# Borrow a book
success, due_date = library.borrow_book(book1, patron1)
if success:
    print(f"{patron1.name} borrowed '{book1.title}' and it's due on {due_date}")
else:
    print("Failed to borrow the book.")

# Return a book
library.return_book(book1)

# Search for books
results = library.search_books(author="M. Amar")
print("Books by M. Amar:")
for book in results:
    print(f"- {book.title}")

# Calculate fine for late return
fine = library.calculate_fine(book1)
if fine is not None:
    print(f"Fine for '{book1.title}': ${fine}")
else:
    print("Book not found or not borrowed.")

# Remove a book from the library
library.remove_book(book3)
