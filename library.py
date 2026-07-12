import json
import os

from book import Book
from member import Member


class Library:

    def __init__(self, filename="data.json"):

        self.filename = filename

        self.books = []
        self.members = []

        self.load_data()

    # -------------------------
    # Save Data
    # -------------------------

    def save_data(self):

        data = {
            "books": [book.to_dict() for book in self.books],
            "members": [member.to_dict() for member in self.members]
        }

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    # -------------------------
    # Load Data
    # -------------------------

    def load_data(self):

        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r") as file:

            if os.path.getsize(self.filename) == 0:
                return

            data = json.load(file)

        self.books = [
            Book.from_dict(book)
            for book in data.get("books", [])
        ]

        self.members = [
            Member.from_dict(member)
            for member in data.get("members", [])
        ]

    def add_book(self, book):

    # Prevent duplicate Book ID
        for b in self.books:
            if b.book_id == book.book_id:
                print("Book ID already exists.")
                return

        # Prevent duplicate Title + Author
        for b in self.books:
            if (
                b.title.lower() == book.title.lower()
                and b.author.lower() == book.author.lower()
            ):
                print("Book already exists.")
                return

        self.books.append(book)

        self.save_data()

        print("Book added successfully.")


    def delete_book(self, book_id):

        for book in self.books:

            if book.book_id == book_id:

                if book.is_issued:
                    print("Cannot delete an issued book.")
                    return

                self.books.remove(book)

                self.save_data()

                print("Book deleted successfully.")
                return

        print("Book not found.")

    def search_book(self, title):

        for book in self.books:

            if title.lower() in book.title.lower():

                print("\nBook Found")
                print(book)
                return

        print("Book not found.")

    def display_books(self):

        if not self.books:
            print("No books available.")
            return

        print("\n========== BOOKS ==========")

        for book in self.books:
            print(book)


    def register_member(self, member):

        # Prevent duplicate Member ID
        for m in self.members:
            if m.member_id == member.member_id:
                print("Member ID already exists.")
                return

        self.members.append(member)

        self.save_data()

        print("Member registered successfully.")


    def display_members(self):

        if not self.members:
            print("No members registered.")
            return

        print("\n========== MEMBERS ==========")

        for member in self.members:
            print(member)

    def issue_book(self, member_id, book_id):

            member = None
            book = None

            # Find Member
            for m in self.members:
                if m.member_id == member_id:
                    member = m
                    break

            if member is None:
                print("Member not found.")
                return

            # Find Book
            for b in self.books:
                if b.book_id == book_id:
                    book = b
                    break

            if book is None:
                print("Book not found.")
                return

            # Already issued?
            if book.is_issued:
                print("Book is already issued.")
                return

            # Borrow limit
            if not member.borrow_book(book_id):
                return

            # Issue book
            book.issue(member.name)

            self.save_data()

            print("Book issued successfully.")


    def return_book(self, member_id, book_id):

            member = None
            book = None

            # Find Member
            for m in self.members:
                if m.member_id == member_id:
                    member = m
                    break

            if member is None:
                print("Member not found.")
                return

            # Find Book
            for b in self.books:
                if b.book_id == book_id:
                    book = b
                    break

            if book is None:
                print("Book not found.")
                return

            # Check whether this member borrowed the book
            if book_id not in member.borrowed_books:
                print("This member didn't borrow this book.")
                return

            # Fine
            fine = book.calculate_fine()

            # Return
            member.return_book(book_id)

            book.return_book()

            self.save_data()

            print("Book returned successfully.")

            if fine > 0:
                print(f"Fine: ₹{fine}")