import sys

class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}, ISBN: {self.isbn}'


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Book "{book.title}" added to the library.')

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f'Book "{book.title}" removed from the library.')
                return
        print('Book not found!')

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f'Found: {book}')
                return
        print('Book not found!')

    def list_books(self):
        if not self.books:
            print('No books in the library.')
            return
        print('Books in the library:')
        for book in self.books:
            print(book)

def display_menu():
    print("\nLibrary Menu")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. List Books")
    print("5. Exit")


def main():
    library = Library()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            year = input("Enter the year of publication: ")
            isbn = input("Enter the ISBN: ")
            book = Book(title, author, year, isbn)
            library.add_book(book)

        elif choice == '2':
            isbn = input("Enter the ISBN of the book to remove: ")
            library.remove_book(isbn)

        elif choice == '3':
            title = input("Enter the book title to search: ")
            library.search_book(title)

        elif choice == '4':
            library.list_books()

        elif choice == '5':
            print("Exiting the program...")
            sys.exit()

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()