from library import Library
from book import Book
from member import Member


library = Library()


while True:

    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book")
    print("2. Delete Book")
    print("3. Search Book")
    print("4. Display Books")
    print("5. Register Member")
    print("6. Display Members")
    print("7. Issue Book")
    print("8. Return Book")
    print("9. Exit")

    choice = input("\nEnter your choice: ")


    if choice == "1":

        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        library.add_book(Book(book_id, title, author))


    elif choice == "2":

        book_id = int(input("Enter Book ID: "))

        library.delete_book(book_id)


    elif choice == "3":

        title = input("Enter Book Title: ")

        library.search_book(title)

 

    elif choice == "4":

        library.display_books()

  

    elif choice == "5":

        member_id = int(input("Enter Member ID: "))
        name = input("Enter Member Name: ")

        library.register_member(Member(member_id, name))



    elif choice == "6":

        library.display_members()


    elif choice == "7":

        member_id = int(input("Enter Member ID: "))
        book_id = int(input("Enter Book ID: "))

        library.issue_book(member_id, book_id)


    elif choice == "8":

        member_id = int(input("Enter Member ID: "))
        book_id = int(input("Enter Book ID: "))

        library.return_book(member_id, book_id)


    elif choice == "9":

        print("\nThank you for using the Library Management System.")
        break

    else:

        print("Invalid choice. Please try again.")