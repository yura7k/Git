from colorama import Fore

from helpers.output_helper import pretty_print
from models.writer import TABLE_NAME
from services.data_service import (get_data, execute_command)

def view_writers():
    query = ("SELECT * FROM %s" % TABLE_NAME)
    writers = get_data(query)
    pretty_print(writers)
    print(Fore.GREEN, " Enter <key> comand ".center(30, "*"), Fore.RESET)

def add_writer():
    autor_name = None
    while True:
        autor_name = input("Please enter autor name: ")

        if len(autor_name.strip()) > 0:
            break
    query = ("INSERT INTO {} (name) VALUES ('{}')".format(TABLE_NAME, autor_name))
    execute_command(query)

    print(" Saved ".center(30, "*"))
