from models.writer import TABLE_NAME
from services.data_service import (get_data, execute_command)

def writers_count():
    query = ("SELECT count(*) as count FROM {0}".format(TABLE_NAME))
    writers_count = get_data(query)
    return writers_count[0]

def view_writers():
    query = ("SELECT * FROM %s" % TABLE_NAME)
    writers = get_data(query)
    return writers

def add_writer(name):
    autor_name = name
    
    query = ("INSERT INTO {} (name) VALUES ('{}')".format(TABLE_NAME, autor_name))
    execute_command(query)

    print(" Saved ".center(30, "*"))
