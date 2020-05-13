import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from actions.books_actions import *

class BooksView(Gtk.Window):
    columns = ["Id", "Name", "Description", "Writer"]

    def __init__(self):
        Gtk.Window.__init__(self, title="Books List")
        self.set_border_width(10)
        #self.set_default_size(640, 480)

        self.render_table()

        self.show_all()
        self.connect("destroy", lambda x: self.hide())

    def render_table(self):
        books = books_list()
        #print(books)

        books_list_store = Gtk.ListStore(int, str, str, str)
        for book in books:
            books_list_store.append(book.values())

        books_view = Gtk.TreeView.new_with_model(Gtk.TreeModelSort(books_list_store))
        
        for i, column_title in enumerate(self.columns):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            if i == 1:
                column.set_sort_column_id(1)
            books_view.append_column(column)

        self.add(books_view)