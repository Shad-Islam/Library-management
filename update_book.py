import datetime
import save_book

def update_book(all_books):
    search_book = input("Enter the name of the book you want to update: ")
    for book in all_books:
        if search_book == book['title']:
            title = input("Enter the book title: ")
            author = input("Enter the author name: ")
            price = int(input("Enter the price: "))
            quantity = int(input("Enter the quantity: "))
            year = int(input("Enter the publishing year: "))
            book_last_update = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            book['title']=title
            book['author']=author
            book["year"]=year
            book["price"]=price
            book["quantity"]=quantity
            book['book_last_update']=book_last_update
            save_book.save_book(all_books)
            return all_books
    print("Book not found\n")

