from datetime import datetime, timedelta
import restore_borrower
import save_book
import save_borrowers

borrowers =[]

def borrow_book(all_books,borrowers):
    
    name = input("Enter your name: ")
    phone = int(input("Enter your phone number: "))
    book_title = input("Enter the book title: ")
    days = int(input("Enter number of days to borrow (e.g., 7): "))
    
    # Calculate return date
    current_date = datetime.now()
    return_date = (current_date + timedelta(days=days)).strftime("%d %B %Y")
    # print(f"Return date will be: {return_date}")
    
   

    borrower = {
       "name": name,
        "phone": phone,
        "book_title": book_title,
        "return_date": return_date
    }

    for book in all_books:
        if book['title'].strip().lower() == book_title.strip().lower():
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




