# Python code to define classes Person, Book, and Library.

# Define a class Person with attributes name, surname, and age.
class Person:
    def __init__(self, name, surname, age) -> None:
        self.name = name
        self.surname = surname
        self.age = age
    
    # String representation of a Person object.
    def __str__(self) -> str:
        return f"Person: {self.name} {self.surname}, Age: {self.age}"

# Create instances of the Person class.
person1 = Person("John", "Snow", 26)
person2 = Person("Arya", "Johnson", 18)
person3 = Person("Daenerys", "Targaryen", 30)
people = [person1, person2, person3]

# Print the list of people.
print("People in the list:")
for person in people:
    print(person)

# Define a Book class with attributes name, author, and year.
class Book:
    def __init__(self, name, author, year) -> None:
        self.name = name
        self.author = author
        self.year = year

# Define a Library class with a list of books as an attribute.
class Library:
    def __init__(self, list_of_books) -> None:
        self.list_of_books = list_of_books
    
    # Method to check the availability of a book in the library.
    def check_availability(self, book) -> bool:
        return book in self.list_of_books
    
    # Method to borrow a book from the library.
    def borrow_book(self, book):
        if self.check_availability(book):
            self.list_of_books.remove(book)
            print(f"Book '{book.name}' has been borrowed.")
        else:
            print(f"Book '{book.name}' is not available.")
    
    # Method to return a book to the library.
    def return_book(self, book):
        if book not in self.list_of_books:
            self.list_of_books.append(book)
            print(f"Book '{book.name}' has been returned.")
        else:
            print(f"Book '{book.name}' is already in the library.")

# Create instances of Book class.
book1 = Book("Marvel", "Jane Schpritz", 2023)
book2 = Book("Japan", "Onzo", 1877)
book3 = Book("Minsk", "Dabreha", 1807)

# Create a list of books and a Library instance with the list of books.
books = [book1, book2]
library1 = Library(books)

# Check the availability of books and perform borrow and return operations.
print("\nChecking book availability:")
print(f"Is '{book1.name}' available? {library1.check_availability(book1)}")
library1.borrow_book(book3)
library1.borrow_book(book2)
print(f"Is '{book2.name}' available? {library1.check_availability(book2)}")
library1.return_book(book2)
print(f"Is '{book2.name}' available? {library1.check_availability(book2)}")