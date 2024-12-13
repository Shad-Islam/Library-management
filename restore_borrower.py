import json

def borrower_restore(borrowers):
    with open("lend_book.json","r")as file:
        borrowers = json.load(file)
        return borrowers