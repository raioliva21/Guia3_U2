import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from tree_view import TreeView

class DialogShowTree(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title="Registro de ordenes", transient_for=parent, flags=0)
        self.set_default_size(150, 100)
        self.tree = TreeView()
        box = self.get_content_area()
        box.add(self.tree)
        self.show_all()