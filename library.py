#STEP 2 --------
class Book: #create the Book class
    def __init__(self, book_id, title, author): #giving it properties
        self.book_id = book_id 
        self.title = title 
        self.author = author 
        self.is_loaned = False #Boolean variable

class Borrower: #class to instantiate a borrower or register a borrower
    def __init__(self, borrower_id, name):
        self.borrower_id = borrower_id
        self.name = name

class Loan: #class to create a loan object that links a book and a borrower
    def __init__(self, book, borrower):
        self.book = book
        self.borrower = borrower

class BookManager: #class to manage the books in the library
    def __init__(self):
        self.books = {} #

    def add_book(self, book_id, title, author): #method to add a book to the library if the book ID does not already exist
        if book_id in self.books:
            raise ValueError("Book ID already exists.")
        self.books[book_id] = Book(book_id, title, author)

    def remove_book(self, book_id): #method to remove a book from the library if the book ID exists
        if book_id in self.books:
            del self.books[book_id]
        else:
            raise ValueError("Book ID not found.")

    def search_book(self, book_id): #method to search for a book in the library by its ID and return the book object if found.
        return self.books.get(book_id, None)

class BorrowerManager: # class to manage borrowers in the library
    def __init__(self):
        self.borrowers = {}

    def add_borrower(self, borrower_id, name): #method to add a borrower to the library if the borrower ID does not already exist
        if borrower_id in self.borrowers:
            raise ValueError("Borrower ID already exists.")
        self.borrowers[borrower_id] = Borrower(borrower_id, name)

    def remove_borrower(self, borrower_id): #method to remove a borrower from the library if the borrower ID exists.
        if borrower_id in self.borrowers:
            del self.borrowers[borrower_id]
        else:
            raise ValueError("Borrower ID not found.")

    def search_borrower(self, borrower_id): #method to search for a borrower in the library by their ID and return the borrower object if found.
        return self.borrowers.get(borrower_id, None)

class LoanManager: #class to manage loans in the library.
    def __init__(self):
        self.loans = [] #store all loans in a list

    def create_loan(self, book, borrower): #method to create a loan for a book and a borrower.
        if book.is_loaned:
            raise ValueError("Book is already loaned.") #if book is loaned it will print this error message
        loan = Loan(book, borrower)
        self.loans.append(loan) #add the loan to the list of loans
        book.is_loaned = True

    def return_loan(self, book): #method to return a loaned book
        for loan in self.loans:
            if loan.book.book_id == book.book_id: #check if the book ID of the loaned book matches the book ID of the book being returned.
                self.loans.remove(loan)
                book.is_loaned = False
                break

#STEP 3 ---------
class LibraryFacade: #class to provide a simplifed interface to the library system, allowing users to interact with the library without needing to understand the underlying complexity of the system.
    def __init__(self):
        self.book_manager = BookManager()
        self.borrower_manager = BorrowerManager()
        self.loan_manager = LoanManager()

    def add_book(self, book_id, title, author): #method to add a book to the library using the BookManager class.
        self.book_manager.add_book(book_id, title, author)

    def remove_book(self, book_id): #method to remove a book from the library using the BookManager class.
        self.book_manager.remove_book(book_id)

    def search_book(self, book_id): #method to search for a book in the library using the BookManager class.
        return self.book_manager.search_book(book_id)

    def add_borrower(self, borrower_id, name): #method to add a borrower to the library using the BorrowerManager class.
        self.borrower_manager.add_borrower(borrower_id, name)

    def remove_borrower(self, borrower_id): #method to remove a borrower from the library using the BorrowerManager class.
        self.borrower_manager.remove_borrower(borrower_id)

    def search_borrower(self, borrower_id): #method to search for a borrower in the library using the BorrowerManager class.
        return self.borrower_manager.search_borrower(borrower_id)

    def create_loan(self, book_id, borrower_id): #method to create a loan for a book and a borrower using the LoanManager class.
        book = self.book_manager.search_book(book_id)
        borrower = self.borrower_manager.search_borrower(borrower_id)
        if book and borrower:
            self.loan_manager.create_loan(book, borrower)
        else:
            raise ValueError("Book or Borrower not found.")

    def return_loan(self, book_id): #method to return a loaned book using the LoanManager class.
        book = self.book_manager.search_book(book_id)
        if book:
            self.loan_manager.return_loan(book)
        else:
            raise ValueError("Book not found.")

#STEP 4 --------

if __name__ == "__main__": #main function to demonstrate the use of the library system.
    library = LibraryFacade()

    # Adding books
    library.add_book(1, "The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book(2, "1984", "George Orwell")

    # Adding borrowers
    library.add_borrower(1, "Alice")
    library.add_borrower(2, "Bob")

    # Creating a loan
    library.create_loan(1, 1)  # Alice borrows "The Great Gatsby"

    # Searching for a book
    book = library.search_book(1)
    print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Is Loaned: {book.is_loaned}")

    # Returning a loan
    library.return_loan(1)

    # Checking the book status again
    book = library.search_book(1)
    print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Is Loaned: {book.is_loaned}")


