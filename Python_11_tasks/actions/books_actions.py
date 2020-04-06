from colorama import Fore

from helpers.output_helper import pretty_print
import models.book as BOOKS
import models.writer as WRITERS
from services.data_service import (get_data, execute_command)
from actions.writers_actions import view_writers


def book_list():
    query = (f"SELECT b.id, b.nameb, w.name FROM {BOOKS.TABLE_NAME} as b, {WRITERS.TABLE_NAME} as w WHERE b.writerId = w.id")
    books = get_data(query)
    pretty_print(books)
    print(Fore.GREEN, " Enter <key> comand ".center(30, "*"), Fore.RESET)
    
def book_info():
    book_list()
    book_id = None
    
    while True:
        book_id = input("Please enter book ID: ")

        if len(book_id.strip()) > 0:
            break
    
    query = (f"SELECT b.nameb, b.description, w.name FROM {BOOKS.TABLE_NAME} as b, {WRITERS.TABLE_NAME} as w WHERE b.id = {book_id} and b.writerId = w.id")
    book_description = get_data(query)
    
    pretty_print(book_description)
    print(" Done ".center(30, "*"))
    print(Fore.GREEN, " Enter <key> comand ".center(30, "*"), Fore.RESET)

def add_book():
    view_writers()
    autor_id = None
    while True:
        autor_id = input("Please enter autor ID: ")
        query = (f"SELECT id FROM {WRITERS.TABLE_NAME} WHERE id = {autor_id}")
        writers = get_data(query)

        if len(autor_id.strip()) > 0 and len(writers) > 0:
            break

    book_name = None
    book_description = None
    while True:
        book_name = input("Please enter book name: ")
        book_description = input("Please enter book description: ")

        if len(book_name.strip()) > 0 and len(book_description.strip()) > 0:
            break
    
    query = (f"INSERT INTO {BOOKS.TABLE_NAME} (nameb, description, writerId) VALUES ('{book_name}', '{book_description}', {autor_id})")
    execute_command(query)

    print(" Saved ".center(30, "*"))
    print(Fore.GREEN, " Enter <key> comand ".center(30, "*"), Fore.RESET)