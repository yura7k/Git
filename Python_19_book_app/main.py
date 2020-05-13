import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

from actions.books_actions import *
from actions.writers_actions import *
from view.books import BooksView
from view.writers import WritersView
from view.register_book import BookRegister
from view.register_writer import WriterRegister

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Books Strogate")
        self.set_default_size(640, 480)
        self.set_border_width(10)

        menu = self.render_menu()
        grid = Gtk.Grid()
        grid.attach(menu, 0, 0, 1, 1)
        self.add(grid)
        self.render_main(grid)
        self.render_books_list(grid)

    def render_menu(self):
        menu = Gtk.MenuBar()
        menu.set_hexpand(True)

        books_item = Gtk.MenuItem(label="Books")
        menu.append(books_item)

        books_submenu = Gtk.Menu()
        books_item.set_submenu(books_submenu)

        books_list = Gtk.MenuItem(label="Books list")
        books_list.connect("activate", lambda x: BooksView())
        books_register = Gtk.MenuItem(label="Register Book")
        books_register.connect("activate", lambda x: BookRegister())
        books_submenu.append(books_list)
        books_submenu.append(books_register)

        writers_item = Gtk.MenuItem(label="Writers")
        menu.append(writers_item)

        writers_submenu = Gtk.Menu()
        writers_item.set_submenu(writers_submenu)

        writers_list = Gtk.MenuItem(label="Writers list")
        writers_list.connect("activate", lambda x: WritersView())
        writers_register = Gtk.MenuItem(label="Register Writer")
        writers_register.connect("activate", lambda x: WriterRegister())
        writers_submenu.append(writers_list)
        writers_submenu.append(writers_register)
        
        about_item = Gtk.MenuItem(label="About")
        about_item.connect("activate", self.show_about)
        menu.append(about_item)

        exit_item = Gtk.MenuItem(label="Exit")
        menu.append(exit_item)
        exit_item.connect("activate", Gtk.main_quit)

        return menu
    
    def render_main(self, grid):
        book_info = books_count()
        book_count_label = Gtk.Label()
        book_count_label.set_margin_top(20)
        book_count_label.set_margin_end(50)
        book_count_label.set_markup("<b>Books count:</b> {0}".format(book_info['count']))
        book_count_label.set_xalign(0)
        grid.attach(book_count_label, 0, 2, 1, 1)

        writers_info = writers_count()
        writers_count_label = Gtk.Label()
        writers_count_label.set_margin_top(20)
        writers_count_label.set_margin_end(50)
        writers_count_label.set_markup("<b>Writers count:</b> {0}".format(writers_info['count']))
        writers_count_label .set_xalign(0)
        grid.attach(writers_count_label, 0, 3, 1, 1)

    def render_books_list(self, grid):
        books_list = books_preview()
        #print(books_list)

        books_list_store = Gtk.ListStore(int, str, str)
        for book in books_list:
            book['description'] = book['description'][:70]
            books_list_store.append(book.values())

        books_view = Gtk.TreeView.new_with_model(Gtk.TreeModelSort(books_list_store))
        
        for i, column_title in enumerate(
            ["Id", "Name", "Description"]
        ):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            if i == 1:
                column.set_sort_column_id(1)
            books_view.append_column(column)

        grid.attach(books_view, 0, 1, 1, 1)

    def show_about(self, component):
        dialog = Gtk.MessageDialog(
            self,
            0,
            Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK,
            "This is an INFO BOOKS APP",
        )
        dialog.format_secondary_text(
            "Some description for Books Strogate app."
        )
        dialog.run()
        dialog.destroy()

main = MainWindow()
main.connect("destroy", Gtk.main_quit)
main.show_all()
Gtk.main()