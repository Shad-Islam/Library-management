import json

def save_borrowers(borrowers):
    with open("all_borrowers.json","w")as file:
        json.dump(borrowers,file,indent = 4)