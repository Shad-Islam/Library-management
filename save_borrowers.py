import json

def save_borrowers(borrowers):
    with open("lend_book.json","w")as file:
        json.dump(borrowers,file,indent = 4)