import datetime

# Book class for managing book information
class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def __str__(self):
        # Returns a string representation of the book
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Copies Available: {self.copies}"

# User class for managing user data and their borrowed books
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.borrowed_books = {}  # Stores borrowed books with due dates

    def borrow(self, library, isbn):
        # Handles borrowing a book
        book = library.find_book(isbn)
        if book and book.copies > 0:
            book.copies -= 1
            due_date = datetime.date.today() + datetime.timedelta(days=14)  # 14 days from today
            self.borrowed_books[isbn] = due_date
            print(f"Book '{book.title}' borrowed successfully! Due date: {due_date}")
        else:
            print("Sorry, this book is not available right now or it doesn't exist.")

    def return_book(self, library, isbn):
        # Handles returning a borrowed book
        if isbn in self.borrowed_books:
            book = library.find_book(isbn)
            due_date = self.borrowed_books.pop(isbn)
            today = datetime.date.today()
            if today > due_date:
                overdue_days = (today - due_date).days
                fine = overdue_days * 1  # Fine of $1 per day
                print(f"Book '{book.title}' returned. Fine: ${fine}")
            else:
                print(f"Book '{book.title}' returned on time.")
            book.copies += 1
        else:
            print("You have not borrowed this book.")

    def check_fine(self):
        # Check for any overdue fines
        total_fine = 0
        today = datetime.date.today()
        for isbn, due_date in self.borrowed_books.items():
            if today > due_date:
                overdue_days = (today - due_date).days
                total_fine += overdue_days * 1  # Fine of $1 per day
        if total_fine > 0:
            print(f"Total overdue fine: ${total_fine}")
        else:
            print("No overdue fines.")

# Library class for managing the collection of books and users
class Library:
    def __init__(self):
        self.books = []  # List of books in the library
        self.users = []  # List of registered users

    def add_book(self, book):
        # Adds a new book to the library
        self.books.append(book)

    def display_books(self):
        # Displays all books available in the library
        if self.books:
            print("Books in Efe Humber Library Project:")
            for book in self.books:
                print(book)
        else:
            print("No books available in the library.")

    def search_book(self, title):
        # Searches for books by title
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            print("Found the following books:")
            for book in found_books:
                print(book)
        else:
            print(f"No books found with the title '{title}'.")

    def find_book(self, isbn):
        # Finds a book by ISBN
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def register_user(self, username, password):
        # Registers a new user
        new_user = User(username, password)
        self.users.append(new_user)
        print(f"User '{username}' registered successfully!")

    def login_user(self, username, password):
        # Logs in a user
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

# Main function to simulate the Library Management System
def main():
    # Creating the Efe Humber Library Project instance
    library = Library()

    # Adding books to the library
    book1 = Book("Python Programming", "John Doe", "12345", 5)
    book2 = Book("Data Structures and Algorithms", "Jane Smith", "67890", 2)
    library.add_book(book1)
    library.add_book(book2)

    # Registering users
    library.register_user("alice", "password123")
    library.register_user("bob", "mypassword")

    print("Welcome to Efe Humber Library Project")

    # Main loop to interact with the library system
    while True:
        print("\nEfe Humber Library Project Management System")
        print("1. Display Books")
        print("2. Search Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Check Fine")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            library.display_books()
        elif choice == '2':
            title = input("Enter the book title to search: ")
            library.search_book(title)
        elif choice == '3':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user = library.login_user(username, password)
            if user:
                isbn = input("Enter the ISBN of the book to borrow: ")
                user.borrow(library, isbn)
            else:
                print("Invalid username or password.")
        elif choice == '4':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user = library.login_user(username, password)
            if user:
                isbn = input("Enter the ISBN of the book to return: ")
                user.return_book(library, isbn)
            else:
                print("Invalid username or password.")
        elif choice == '5':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user = library.login_user(username, password)
            if user:
                user.check_fine()
            else:
                print("Invalid username or password.")
        elif choice == '6':
            print("Exiting the Efe Humber Library Project.")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()
