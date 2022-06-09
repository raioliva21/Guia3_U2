import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def create_row(label, lista):

    combo_box = Gtk.ComboBoxText()
    combo_box.set_entry_text_column(0)
    lista.insert(0, "seleccionar")
    for indice in lista:
        combo_box.append_text(indice)
    combo_box.set_active(0)
    _label = Gtk.Label(label=label)
    box = create_box(_label, combo_box)
    row = Gtk.ListBoxRow()
    row.add(box)

    return row, combo_box

def create_box(widget1, widget2):

    box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    box.set_homogeneous(True) 
    box.pack_start(widget1, True, True, 0)
    box.pack_start(widget2, True, True, 0)

    return box