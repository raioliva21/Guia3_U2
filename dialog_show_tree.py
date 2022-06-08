import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from tree_view import TreeView

class DialogShowTree(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title="Registro de ordenes", transient_for=parent, flags=0)
        #self.add_buttons(
        #    Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK
        #)

        self.set_default_size(150, 100)

        self.tree = TreeView()
        box = self.get_content_area()
        box.add(self.tree)
        self.show_all()