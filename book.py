from datetime import datetime,timedelta

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

        self.is_issued = False
        self.issued_to = None

        self.issue_date = None
        self.due_date = None
    def issue(self,member_name):
        self.is_issued = True
        self.issued_to = member_name

        self.issue_date = datetime.now()
        self.due_date = self.issue_date + timedelta(days=14)

    def return_book(self):
        self.is_issued = False
        self.issued_to = None

        self.issue_date = None
        self.due_date = None

    def calculate_fine(self):
        if not self.is_issued:
            return 0
        today=datetime.now()
        if today<=self.due_date:
            return 0
        last_date=(today-self.due_date).days
        return last_date*10
    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "is_issued": self.is_issued,
            "issued_to": self.issued_to,
            "issue_date": self.issue_date.isoformat() if self.issue_date else None,
            "due_date": self.due_date.isoformat() if self.due_date else None
        }
    @classmethod
    def from_dict(cls,data):
        book = cls(
            data["book_id"],
            data["title"],
            data["author"]
        )
        book.is_issued = data["is_issued"]
        book.issued_to = data["issued_to"]
        issue_date = data.get("issue_date") or data.get("issued_date")

        if issue_date:
            book.issue_date = datetime.fromisoformat(issue_date)

        if data["due_date"]:
            book.due_date = datetime.fromisoformat(data["due_date"])
        return book
    def __str__(self):

        status = "Issued" if self.is_issued else "Available"

        return (
            f"ID: {self.book_id} | "
            f"{self.title} | "
            f"{self.author} | "
            f"{status}"
        )


        