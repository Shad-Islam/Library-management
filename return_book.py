import save_borrowers
import save_book

def return_book(borrowers,all_books):
    name = input("Enter your name: ").strip()
    if not name:
        print("Error: Name cannot be empty")
        return borrowers

    book_name = input("Enter the book name: ").strip()
    if not book_name:
        print("Error: Book name cannot be empty")
        return borrowers

    # Normalize inputs to ensure they match the stored data
    for borrower in borrowers:
        if (borrower["name"].strip().lower() == name.lower() and 
            borrower["book_title"].strip().lower() == book_name.lower()):
            borrowers.remove(borrower)
            save_borrowers.save_borrowers(borrowers)

            for book in all_books:
                if book["title"].strip().lower()==book_name.lower():
                    book["quantity"]=book["quantity"]+1
                    save_book.save_book(all_books)
                    print("\nBook returned successfully")
                    return borrowers
    
    print("\nNo matching record found. Please check the name and book title.")
    return borrowers
