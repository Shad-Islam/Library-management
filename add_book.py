from save_book import save_book
import random
from datetime import datetime 

def add_book(all_books):
    title = input("Enter the book title: ")
    author = input("Enter the author name: ")
    price = int(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))
    year = int(input("Enter the publishing year: "))

    isbn = random.randint(10000,99999)
    bookAddedAt = datetime.now().strftime("%d-%m-%y %H:%M:%S")

    book = {
        "title":title,
        "author":author,
        "isbn":isbn,
        "year":year,
        "price":price,
        "quantity":quantity,
        "bookAddedAt":bookAddedAt,
        "book_last_update":"Not update yet"
    }

    all_books.append(book)
    save_book(all_books)
    print("Book added succesfully")
    return all_books