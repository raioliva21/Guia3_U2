from gi.repository import Gtk
import gi
gi.require_version("Gtk", "3.0")

class FileChooser(Gtk.FileChooserDialog):

    def __init__(self, parent) -> None:
        super().__init__(title="Please choose a file", transient_for=parent,
        action=Gtk.FileChooserAction.OPEN)
    
        self.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK
        )

        """ APLICAN FILTROS DE SELECCION """
        
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        self.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        self.add_filter(filter_py)

        wanted_file = Gtk.FileFilter()
        wanted_file.set_name("orders data file")
        wanted_file.add_mime_type("text/Json")
        wanted_file.add_pattern("registro_de_pedidos.json")
        self.add_filter(wanted_file)

        self.show_all()