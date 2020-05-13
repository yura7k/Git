import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from actions.writers_actions import *

class WritersView(Gtk.Window):
    columns = ["Id", "Name"]

    def __init__(self):
        Gtk.Window.__init__(self, title="Writers List")
        self.set_border_width(10)
        self.set_default_size(250, 150)

        self.render_table()

        self.show_all()
        self.connect("destroy", lambda x: self.hide())

    def render_table(self):
        writers = view_writers()
        #print(writers)

        writers_list_store = Gtk.ListStore(int, str)
        for writer in writers:
            writers_list_store.append(writer.values())

        writers_view = Gtk.TreeView.new_with_model(Gtk.TreeModelSort(writers_list_store))
        
        for i, column_title in enumerate(self.columns):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            if i == 1:
                column.set_sort_column_id(1)
            writers_view.append_column(column)

        self.add(writers_view)