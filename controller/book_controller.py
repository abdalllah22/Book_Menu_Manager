from models.book import Book


class BookController:
    def __init__(self, Helpers):
        self.helper = Helpers()

    def call_menu(self):
        try:
            choice = self.helper.print_menu_data()
            self.call_choice(choice)
        except Exception as e:
            print(f'Indide Exception of call_menu', e)

    def call_choice(self, choice):
        try:
            if choice == '1':
                self.view_all_books()
                self.print_details_or_back()
            elif choice == '2':
                book = self.book_data()
                self.create_book(book)
                self.call_menu()
            elif choice == '3':
                self.helper.edit_book_text()
                self.view_all_books()
                self.edit_details_or_back()
            elif choice == '4':
                search_word = self.helper.search_book_text()
                self.search(search_word)
            elif choice == '5':
                print('Library saved.')
            else:
                self.helper.not_found()
                choice = self.helper.print_menu_data()
                self.call_choice(choice)
        except Exception as e:
            print(f'Indide Exception of call_choice', e)

    def print_details_or_back(self):
        try:
            details_choice = input(
                "To view details enter the book ID, to return press <Enter>")

            if details_choice == '':
                self.call_menu()
            else:
                IDs = self.view_all_books_IDS()
                if details_choice in IDs:
                    self.view_specific_book(details_choice)
                    self.print_details_or_back()
                else:
                    self.helper.not_found()
                    self.call_menu()
        except Exception as e:
            print(f'Indide Exception of print_details_or_back', e)

    def view_all_books(self):
        try:
            loadData = self.helper.loadData("db/books.json")
            for i in range(len(loadData)):
                print(f"{[int(loadData[i]['ID'])]} {loadData[i]['Title']}")
        except Exception as e:
            print(f'Indide Exception of view_all_books', e)

    def view_specific_book(self, book_id):
        try:
            loadData = self.helper.loadData("db/books.json")
            for i in range(len(loadData)):
                if book_id == loadData[i]['ID']:
                    print("ID: ", loadData[i]['ID'])
                    print("Title: ", loadData[i]['Title'])
                    print("Author: ", loadData[i]['Author'])
                    print("Description: ", loadData[i]['Description'])
                    break
        except Exception as e:
            print(f'Indide Exception of view_specific_book', e)

    def view_all_books_IDS(self):
        try:
            IDs = []
            loadData = self.helper.loadData("db/books.json")
            for i in range(len(loadData)):
                IDs.append(loadData[i]['ID'])

            return IDs
        except Exception as e:
            print(f'Indide Exception of view_all_books_IDS', e)

    def create_book(self, book):
        try:
            new_book = {}
            data = self.helper.loadData("db/books.json")
            number_of_books = len(self.view_all_books_IDS())
            listed_books_after_added = number_of_books + 1
            new_book['ID'] = str(listed_books_after_added)
            new_book['Title'] = book.title
            new_book['Author'] = book.author
            new_book['Description'] = book.description
            data.append(new_book)
            self.helper.saveData("db/books.json", data)
            print(f"Book {[listed_books_after_added]} Saved")
        except Exception as e:
            print(f'Indide Exception of create_book', e)

    def book_data(self):
        try:
            title, author, description = self.helper.input_book_data()
            book = Book(
                title=title,
                author=author,
                description=description
            )
            return book
        except Exception as e:
            print(f'Indide Exception of book_data', e)

    def edit_details_or_back(self):
        try:
            details_choice = input(
                "Enter the book ID of the book you want to edit; to return press <Enter>.")

            if details_choice == '':
                self.call_menu()
            else:
                IDs = self.view_all_books_IDS()
                if details_choice in IDs:
                    self.edit_specific_book(details_choice)
                else:
                    self.helper.not_found()
                    self.call_menu()
        except Exception as e:
            print(f'Indide Exception of edit_details_or_back', e)

    def edit_specific_book(self, book_id):
        try:
            loadData = self.helper.loadData("db/books.json")
            for i in range(len(loadData)):
                if book_id == loadData[i]['ID']:

                    title, author, description = self.helper.edit_book_data(
                        loadData[i]['Title'],
                        loadData[i]['Author'],
                        loadData[i]['Description'])

                    if title == '':
                        title = loadData[i]['Title']
                    if author == '':
                        author = loadData[i]['Author']
                    if description == '':
                        description = loadData[i]['Description']

                    loadData[i]['Title'] = title
                    loadData[i]['Author'] = author
                    loadData[i]['Description'] = description
                    self.helper.saveData("db/books.json", loadData)
                    print('Book saved.')
                    self.edit_details_or_back()
        except Exception as e:
            print(f'Indide Exception of edit_specific_book', e)

    def search(self, keyword=''):
        try:
            books = self.helper.loadData("db/books.json")
            for i in range(len(books)):
                result = self.helper.find_word(keyword)(books[i]['Title'])
                if result:
                    print(f"{[int(books[i]['ID'])]} {books[i]['Title']}")
                    choice = input(
                        'The following books matched your query. Enter the book ID to see more details, or <Enter> to return.')

                    if choice == '':
                        self.call_menu()

                    if books[i]['ID'] == choice:
                        self.view_specific_book(choice)
                        self.call_menu()
                    else:
                        print(
                            "This Book Doesn't Exists In Search Result .. Try Anthor Search")

                else:
                    pass

            print("This Book Doesn't Exists")
            self.call_menu()
        except Exception as e:
            print(f'Indide Exception of search', e)
