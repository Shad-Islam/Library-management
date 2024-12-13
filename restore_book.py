import json

def all_book_restore(all_books):
    with open("all_books.json","r")as file:
        all_books = json.load(file)
        return all_books 