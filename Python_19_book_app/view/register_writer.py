import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from actions.writers_actions import *

class WriterRegister(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Writer Register")
        self.set_border_width(10)
        self.set_resizable(False)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        self.render_form(vbox)

        self.show_all()
        self.connect("destroy", lambda x: self.hide())


    def render_form(self, vbox):
        hbox_name = Gtk.Box(spacing=10)
        hbox_name.set_homogeneous(False)
        vbox.pack_start(hbox_name, True, True, 0)
        label_name = Gtk.Label("Autor's name: ")
        label_name.set_width_chars(20)
        hbox_name.pack_start(label_name, True, True, 0)

        self.entry_name = Gtk.Entry()
        self.entry_name.set_placeholder_text("Entry name here...") # чомусь не працює(((
        hbox_name.pack_start(self.entry_name, True, True, 0)

        hbox_buttons = Gtk.Box(spacing=10)
        hbox_buttons.set_homogeneous(False)
        vbox.pack_start(hbox_buttons, True, True, 0)

        button = Gtk.Button("Save")
        button.connect("clicked", self.on_open_clicked)
        hbox_buttons.pack_start(button, True, True, 0)

    def on_open_clicked(self, button):
        writer_name = self.entry_name.get_text()
        
        add_writer(writer_name)
