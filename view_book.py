def view_book(all_books):
    if all_books != []:
        for book in all_books:
            print(f"\nTitle: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Year: {book['year']}, Ptice: {book['price']}, Quantity: {book['quantity']}, Book Added At: {book['bookAddedAt']}, Book update: {book["book_last_update"]}")
    else:
        print("No book found\n")