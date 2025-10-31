from bookModule import Book

books = {}   # Dictionary to store books (key = book id, value = Book object)

def add_book():
    bid = input("Enter Book ID: ")
    if bid in books:
        print("Book ID already exists!")
        return
    name = input("Enter Book Name: ")
    price = float(input("Enter Book Price: "))
    author = input("Enter Author Name: ")
    books[bid] = Book(bid, name, price, author)
    print("Book added successfully!...")

def delete_book():
    bid = input("Enter Book ID to delete: ")
    if bid in books:
        del books[bid]
        print("Book Deleted successfully!...")
    else:
        print("Book not found!...")

def display_all():
    if not books:
        print("No books available.")
    else:
        print("\nAll Books:")
        for b in books.values():
            b.display()

def search_book():
    bid = input("Enter Book ID to search: ")
    if bid in books:
        print("Book Found:")
        books[bid].display()
    else:
        print("Book not found!")

while True:
    print("\n==== BOOK MANAGEMENT MENU ====")
    print("1. Add Book")
    print("2. Delete Book by ID")
    print("3. Display All Books")
    print("4. Search Book by ID")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        delete_book()
    elif choice == '3':
        display_all()
    elif choice == '4':
        search_book()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")