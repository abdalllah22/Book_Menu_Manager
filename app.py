from controller.book_controller import BookController
from helpers.helpers import Helpers


project_controller = BookController(Helpers)
helper = Helpers()


def main():
    try:
      project_controller.call_menu()
    except Exception as e:
        print(f'Indide Exception of main',e)
        


if __name__ == '__main__':
    main()
