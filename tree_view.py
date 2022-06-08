import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from file_actions import open_file


class TreeView(Gtk.TreeView):

    def __init__(self) -> None:
        super().__init__()

        self.modelo = Gtk.ListStore(str, str, str, str)
        self.set_model(model=self.modelo)

        nombre_columnas = ("Fecha", "Nombre", "Metodo de Pago", "Costo pedido")
        cell = Gtk.CellRendererText()
        for item in range(len(nombre_columnas)):
            column = Gtk.TreeViewColumn(nombre_columnas[item], cell, text=item)
            self.append_column(column)


    """Carga datos desde archivo json"""
    def load_json_data(self, file):
        # llamamos al metodo de abrir el archivo
        datos = open_file(file)
        print("se carga data json en treeview")
        for item in datos:
            # proceso por medio de listas por comprensión
            line = [x for x in item.values()]
            print(line)
            self.modelo.append(line)


    """Elimina todo el contenido del TreeView (modelo, ListStore)."""
    def delate_displayed_data(self):
        for index in range(len(self.modelo)):
            # iter(0) por que nunca va a estar vacio.
            iter_ = self.modelo.get_iter(0)
            self.modelo.remove(iter_)