import add_book
import delete_book
import restore_book
import update_book
import view_book

all_books = []

while True:
    print("Welcome to our library")
    print("1. Add book")
    print("2. View all books")
    print("3. Update book")
    print("4. Remove book")
    print("5. Exit")
    all_books = restore_book.all_book_restore(all_books)

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
        print("Thanks for using library management system")
        break
    else:
        print("Please enter a valid number")