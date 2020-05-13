import models.book as BOOKS
import models.writer as WRITERS
from services.data_service import (get_data, execute_command)
from actions.writers_actions import view_writers

def books_count():
    query = ("SELECT count(*) as count FROM {0}".format(BOOKS.TABLE_NAME))
    books_count = get_data(query)
    return books_count[0]

def books_preview():
    query = ("SELECT id, name, description FROM {0}".format(BOOKS.TABLE_NAME))
    books = get_data(query)
    return books

def books_list():
    query = (f"SELECT b.id, b.name as book, b.description, \
            w.name as writer FROM {BOOKS.TABLE_NAME} as b, \
            {WRITERS.TABLE_NAME} as w WHERE b.writerId = w.id")
    books = get_data(query)
    #pretty_print(books)
    return books

def add_book(name, description, writerId):
    autor_id = writerId
    book_name = name
    book_description = description
    
    query = (f"INSERT INTO {BOOKS.TABLE_NAME} (name, description, writerId) VALUES ('{book_name}', \
            '{book_description}', {autor_id})")
    execute_command(query)

    print(" Saved ".center(30, "*"))