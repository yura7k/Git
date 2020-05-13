import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from actions.books_actions import *
from actions.writers_actions import *

class BookRegister(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Book Register")
        self.set_border_width(10)
        self.set_resizable(False)
        #self.set_default_size(400, 300)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        self.render_form(vbox)

        self.show_all()
        self.connect("destroy", lambda x: self.hide())


    def render_form(self, vbox):
        hbox_name = Gtk.Box(spacing=10)
        hbox_name.set_homogeneous(False)
        vbox.pack_start(hbox_name, True, True, 0)
        label_name = Gtk.Label("Name: ")
        label_name.set_width_chars(20)
        #label_name.set_justify(Gtk.Justification.LEFT)
        hbox_name.pack_start(label_name, True, True, 0)

        self.entry_name = Gtk.Entry()
        hbox_name.pack_start(self.entry_name, True, True, 0)

        hbox_description = Gtk.Box(spacing=10)
        hbox_description.set_homogeneous(False)
        vbox.pack_start(hbox_description, True, True, 0)
        label_description = Gtk.Label("Description: ")
        label_description.set_width_chars(20)
        hbox_description.pack_start(label_description, True, True, 0)

        self.entry_description = Gtk.Entry()
        hbox_description.pack_start(self.entry_description, True, True, 0)

        hbox_writer = Gtk.Box(spacing=10)
        hbox_writer.set_homogeneous(False)
        vbox.pack_start(hbox_writer, True, True, 0)
        label_writer = Gtk.Label("Writer Name: ")
        label_writer.set_width_chars(20)
        #label_writer.set_justify(Gtk.Justification.LEFT)
        hbox_writer.pack_start(label_writer, True, True, 0)
        
        writers = view_writers()

        wirter_list = Gtk.ListStore(int, str)
        for writer in writers:
            wirter_list.append(writer.values())
        
        writers_combo = Gtk.ComboBox.new_with_model(wirter_list)
        writers_combo.connect("changed", self.on_country_combo_changed)
        renderer_text = Gtk.CellRendererText()
        writers_combo.pack_start(renderer_text, True)
        writers_combo.add_attribute(renderer_text, "text", 1)
        hbox_writer.pack_start(writers_combo, True, True, 0)
        
        # entry_writer = Gtk.Entry()
        # hbox_writer.pack_start(entry_writer, True, True, 0)
        
        hbox_buttons = Gtk.Box(spacing=10)
        hbox_buttons.set_homogeneous(False)
        vbox.pack_start(hbox_buttons, True, True, 0)

        button = Gtk.Button("Save")
        button.connect("clicked", self.on_save_clicked)
        hbox_buttons.pack_start(button, True, True, 0)

    def on_country_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        model = combo.get_model()
        self.writer_id, self.writer_name = model[tree_iter][:2]
    
    def on_save_clicked(self, widget):
        book_name = self.entry_name.get_text()
        book_desc = self.entry_description.get_text()
        add_book(book_name, book_desc, self.writer_id)

