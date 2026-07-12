class Member:

    MAX_BOOKS = 3

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    # Borrow a book
    def borrow_book(self, book_id):

        if len(self.borrowed_books) >= Member.MAX_BOOKS:
            print(f"{self.name} has reached the maximum borrowing limit.")
            return False

        self.borrowed_books.append(book_id)
        return True

    # Return a book
    def return_book(self, book_id):

        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            return True

        return False

    # Convert object to dictionary (for JSON)
    def to_dict(self):

        return {
            "member_id": self.member_id,
            "name": self.name,
            "borrowed_books": self.borrowed_books
        }

    # Create object from dictionary
    @classmethod
    def from_dict(cls, data):

        member = cls(
            data["member_id"],
            data["name"]
        )

        member.borrowed_books = data["borrowed_books"]

        return member

    # String representation
    def __str__(self):

        return (
            f"Member ID: {self.member_id} | "
            f"Name: {self.name} | "
            f"Borrowed Books: {len(self.borrowed_books)}"
        )