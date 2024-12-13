import json

def borrower_restore(borrowers):
    with open("all_borrowers.json","r")as file:
        borrowers = json.load(file)
        return borrowers