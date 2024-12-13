import save_book

def delete_book(all_books):
    search_book = input("Enter the name of the book you want to delete: ")
    for book in all_books:
        if book['title'] == search_book:
            all_books.remove(book)
            print("Book deleted succesfully.\n")
            save_book.save_book(all_books)
            return all_books
    else:
        print("Book not found\n")

