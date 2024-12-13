import restore_borrower
import save_book
import save_borrowers

borrowers =[]

def borrow_book(all_books):
    name = input("Enter your name: ")
    phone= int(input("Enter your phone number: "))
    return_date = input("Enter return date: ")
    book_title = input("Enter the book title: ")
    restore_borrower.borrower_restore(borrowers)

    borrower ={
       "name":name,
        "phone":phone,
        "book_title":book_title,
        "return_date":return_date
    }

    for book in all_books:
        if book['title'] == book_title:
            if book["quantity"] > 0:
                book["quantity"] = book["quantity"]-1
                print("Book borrowed successfully\n")
                borrowers.append(borrower)
                save_borrowers.save_borrowers(borrowers)
                save_book.save_book(all_books)
                return all_books
            else:
                print("Not enough books are available to lend\n")
                return all_books
    print("No book found\n")




