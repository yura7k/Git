import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class BookApp(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Menu Books")

        self.set_default_size(400, 300)
        self.connect("destroy", Gtk.main_quit)

        grid = Gtk.Grid()
        self.add(grid)

        menubar = Gtk.MenuBar()
        menubar.set_hexpand(True)
        grid.attach(menubar, 0, 0, 1, 1)

        #  add books submenu
        item_book = Gtk.MenuItem(label="Book")
        menubar.append(item_book)

        submenu_book = Gtk.Menu()    
        item_book.set_submenu(submenu_book)    
        
        item_new = Gtk.ImageMenuItem(Gtk.STOCK_NEW, label="Register book")
        submenu_book.append(item_new)
        item_new.connect("activate", self.new_book)
        
        item_info_book = Gtk.MenuItem(label="Book info")
        submenu_book.append(item_info_book)
        item_info_book.connect("activate", self.info_book)

        item_book_list = Gtk.MenuItem(label="Book list")
        submenu_book.append(item_book_list)
        item_book_list.connect("activate", self.book_list)

        #  add hotkeys book submenu
        accelgroup = Gtk.AccelGroup()
        self.add_accel_group(accelgroup)        
        item_new.add_accelerator("activate", 
                                accelgroup,
                                Gdk.keyval_from_name("n"),
                                Gdk.ModifierType.CONTROL_MASK,
                                Gtk.AccelFlags.VISIBLE)

        #  add writers submenu
        item_writer = Gtk.MenuItem(label="Writer")
        menubar.append(item_writer)

        submenu_writer = Gtk.Menu()
        item_writer.set_submenu(submenu_writer)

        item_new_writer = Gtk.MenuItem(label="Register writer")
        submenu_writer.append(item_new_writer)
        item_new_writer.connect("activate", self.new_writer)

        item_list_writer = Gtk.MenuItem(label="List of writer")
        submenu_writer.append(item_list_writer)
        item_list_writer.connect("activate", self.writer_list)

        #  add info dialog
        item_info = Gtk.MenuItem(label="Info")
        menubar.append(item_info)
        item_info.connect("activate", self.info_window)
        
        #  add exit button
        item_exit = Gtk.MenuItem(label="Exit")
        menubar.append(item_exit)
        item_exit.connect("activate", self.exit_program)
        
        #  add status bar
        self.statusbar = Gtk.Statusbar()
        self.statusbar.push(1, "Ready")

        grid1 = Gtk.Grid()
        grid1.add(self.statusbar)

        self.messagedialog = Gtk.MessageDialog(message_format="Info")
        self.messagedialog.set_transient_for(self)
        self.messagedialog.set_title("My info")
        self.messagedialog.set_markup("<span size='12000'><b>This is a MessageDialog widget.</b></span>")
        self.messagedialog.format_secondary_text("The MessageDialog can display a main message, and further secondary content.")
        self.messagedialog.add_button("_Close", Gtk.ResponseType.CLOSE)    


    def new_book(self, widget):
        print("New book")

    def info_book(self, widget):
        print("Info book")

    def book_list(self, widget):
        print("List book")

    def new_writer(self, widget):
        print("New writer")

    def writer_list(self, widget):
        print("List writer")

    def info_window(self, widget):
        print("Show info box")
        self.messagedialog.set_property("message-type", Gtk.MessageType.INFO)

        self.messagedialog.run()
        self.messagedialog.hide()

    def exit_program(self, widget):
        print("Windows quit")
        Gtk.main_quit()
      
window = BookApp()
window.show_all()
Gtk.main()