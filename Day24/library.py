import json
from book import Book
from member import Member


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    # Add Book
    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    # Remove Book
    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_borrowed:
                    print("Book is currently borrowed")
                    return

                self.books.remove(book)
                print("Book removed successfully!")
                return

        print("Book not found")

    # Register Member
    def register_member(self, member):
        self.members.append(member)
        print("Member registered successfully!")

    # Borrow Book
    def borrow_book(self, member_id, book_id):
        for member in self.members:
            if member.member_id == member_id:

                if len(member.borrowed_books) >= 3:
                    print("Maximum 3 books allowed")
                    return

                for book in self.books:
                    if book.book_id == book_id:

                        if not book.is_borrowed:
                            book.is_borrowed = True
                            member.borrow_book(book)
                            print("Book borrowed successfully!")
                            return

                        print("Book already borrowed")
                        return

                print("Book not found")
                return

        print("Member not found")

    # Return Book
    def return_book(self, member_id, book_id):
        for member in self.members:
            if member.member_id == member_id:

                for book in member.borrowed_books:
                    if book.book_id == book_id:
                        book.is_borrowed = False
                        member.return_book(book)
                        print("Book returned successfully!")
                        return

                print("Borrowed book not found")
                return

        print("Member not found")

    # Search Book
    def search_book(self, keyword):
        found = False

        for book in self.books:
            if (keyword.lower() in book.title.lower()
                    or keyword.lower() in book.author.lower()):
                print(book)
                found = True

        if not found:
            print("Book not found")

    # Show Books
    def show_books(self):
        for book in self.books:
            print(book)

    # Save Data
    def save_data(self):
        data = {
            "books": [
                {
                    "book_id": b.book_id,
                    "title": b.title,
                    "author": b.author,
                    "is_borrowed": b.is_borrowed
                }
                for b in self.books
            ],

            "members": [
                {
                    "member_id": m.member_id,
                    "name": m.name,
                    "borrowed_books": [
                        b.book_id for b in m.borrowed_books
                    ]
                }
                for m in self.members
            ]
        }

        with open("library_data.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Data saved successfully!")

    # Load Data
    def load_data(self):
        try:
            with open("library_data.json", "r") as file:
                data = json.load(file)

            self.books = []

            for b in data["books"]:
                book = Book(
                    b["book_id"],
                    b["title"],
                    b["author"]
                )
                book.is_borrowed = b["is_borrowed"]
                self.books.append(book)

            self.members = []

            for m in data["members"]:
                member = Member(
                    m["member_id"],
                    m["name"]
                )

                for book_id in m["borrowed_books"]:
                    for book in self.books:
                        if book.book_id == book_id:
                            member.borrow_book(book)

                self.members.append(member)

            print("Data loaded successfully!")

        except FileNotFoundError:
            print("No saved data found")