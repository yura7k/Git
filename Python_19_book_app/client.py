import os
import sys
sys.path.append(os.getcwd())

from colorama import Fore
from switchlang import switch

from actions.books_actions import *
from actions.writers_actions import *

import models.book as book
import models.writer as writer

from services.data_service import (create_db)

def main():
    show_command()

    while True:
        action = get_action()

        with switch(action) as s:
            s.case('b', books_list)
            s.case('i', book_info)
            s.case('r', add_book)
            s.case('l', view_writers)
            s.case('w', add_writer)
            s.case('?', show_command)
            s.case('e', exit)
            s.default(lambda: print("Sorry? Enter True Command"))

def show_command():
    print(Fore.GREEN, "What action would you like to do:", Fore.RESET)
    print("[B]ooks list")
    print("Book [i]nfo")
    print("[R]egister book")
    print("Writer [L]ist")
    print("Register a [W]riter")
    print("[?] Help info")
    print("[E] Exit")

def get_action():
    action = input(Fore.YELLOW + "> " + Fore.RESET)
    return action.strip().lower()

if __name__ == '__main__':
    create_db(writer.TABLE, book.TABLE)
    main()