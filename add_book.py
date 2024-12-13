from datetime import datetime 
import random
from save_book import save_book

def add_book(all_books):
    title = input("Enter the book title: ")
    author = input("Enter the author name: ")
    while True:
        try:
            price = input("Enter the price: ")
            price = int(price)
            if price < 0:
                print("Price cannot be negative. Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
    while True:
        try:
            quantity = input("Enter the quantity: ")
            quantity = int(quantity)
            if quantity < 0:
                print("Quantity cannot be negative. Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
    while True:
        try:
            year = input("Enter the publishing year: ")
            year = int(year)
            current_year = datetime.now().year
            if year < 1000 or year > current_year:
                print(f"Please enter a valid year between 1000 and {current_year}.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid year.")

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