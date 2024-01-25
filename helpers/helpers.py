import json
import re


class Helpers:
    def __init__(self):
        pass

    def loadData(self, file):
        try:
            db = open(file, 'r')
            data_string = db.read()
            db.close()
            data = json.loads(data_string)
            return data
        except Exception:
            return []

    def saveData(self, file, data):
        try:
            db = open(file, 'w')
            db.write(json.dumps(data))
            db.close()
        except Exception:
            print(f"{file} Doesn't exists")

    def find_word(self, keyword):
        return re.compile(r'\b({0})\b'.format(keyword), flags=re.IGNORECASE).search

    def print_menu_data(self):
        print("==== Book Manager ====")
        print(f"[1] View all books")
        print(f"[2] Add a book")
        print(f"[3] Edit a book")
        print(f"[4] Search for a book")
        print(f"[5] Save and exit")
        choice = input("Choose [1-5]:")
        return choice

    def not_found(self):
        print("================")
        print("Not Found In Menu")
        print("================")

    def input_book_data(self):
        print("==== Add a Book ====")
        print("Please enter the following information:")
        title = input("Title: ")
        author = input("Author: ")
        description = input("Description: ")
        return title, author, description

    def edit_book_data(self, title, author, description):
        print("Input the following information. To leave a field unchanged, hit <Enter>")
        title = input(f"Title: {[title]}: ")
        author = input(f"Author: {[author]}: ")
        description = input(f"Description: {[description]}: ")
        return title, author, description

    def edit_book_text(self):
        print("==== Edit a Book ====")

    def search_book_text(self):
        print("==== Search ====")
        print('Type in one or more keywords to search for')
        search_word = input('Search: ')
        return search_word
