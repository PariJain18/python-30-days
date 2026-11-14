from book import Book
from member import Member
from library import Library


# Create Library
library = Library()

# Create Books
b1 = Book(1, "Python Basics", "John")
b2 = Book(2, "Java Programming", "James")
b3 = Book(3, "HTML Guide", "David")
b4 = Book(4, "CSS Basics", "Alex")

# Add Books
library.add_book(b1)
library.add_book(b2)
library.add_book(b3)
library.add_book(b4)

# Register Member
m1 = Member(101, "Pari")
library.register_member(m1)

# Borrow Books
library.borrow_book(101, 1)
library.borrow_book(101, 2)

# Show Books
print("\nAll Books:")
library.show_books()

# Search Book
print("\nSearch Result:")
library.search_book("Python")

# Return Book
library.return_book(101, 1)

# Save Data
library.save_data()

# Load Data
new_library = Library()
new_library.load_data()

print("\nLoaded Books:")
new_library.show_books()