import add_book
import borrow_book
import delete_book
import restore_book
import restore_borrower
import return_book
import update_book
import view_book

all_books = []
borrowers =[]

while True:
    print("\nWelcome to our library")
    print("1. Add book")
    print("2. View all books")
    print("3. Update book")
    print("4. Remove book")
    print("5. Borrow book")
    print("6. Return book")
    print("7. Exit")
    all_books = restore_book.all_book_restore(all_books)
    borrowers = restore_borrower.borrower_restore(borrowers)

    option = input("Select any number: ")

    if option == "1":
        add_book.add_book(all_books)
    elif option == "2":
        view_book.view_book(all_books)
    elif option == "3":
        update_book.update_book(all_books)
    elif option == "4":
        delete_book.delete_book(all_books)
    elif option == "5":
        borrow_book.borrow_book(all_books,borrowers)
    elif option =="6":
        return_book.return_book(borrowers,all_books)
    elif option == "7":
        print("Thanks for using library management system: ")
        break
    else:
        print("Please enter a valid number\n")