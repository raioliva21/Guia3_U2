from xmlrpc.client import Boolean
from gi.repository import Gtk
import gi
gi.require_version("Gtk", "3.0")

class Dialog_add_drink(Gtk.Dialog):

    def __init__(self, parent):
        super().__init__(title="Añade Bebestible", transient_for=parent, flags=0)
        self._state = bool
        self.drink = str
        self.cost = int
        self.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK
        )
        self.set_border_width(10)

        name_store = Gtk.ListStore(int, str)
        name_store.append([750, "Coca-Cola 350cc $750"])
        name_store.append([750, "Sprite 350cc  $750"])
        name_store.append([750, "Nectar Durazno 350cc  $750"])
        name_store.append([1000, "Jugo Natural Manzana 350cc $1000"])
        name_store.append([1000, "Jugo Natural Naranja 350cc $1000"])
        name_store.append([1500, "Cerveza Artesanal 350cc $1500"])


        name_combo = Gtk.ComboBox.new_with_model_and_entry(name_store)
        name_combo.connect("changed", self.on_name_combo_changed)
        name_combo.set_entry_text_column(1)
        
        label_unidades = Gtk.Label(label="Unidades")
        adjustment = Gtk.Adjustment(upper=100, step_increment=1, page_increment=10)
        self.unidades = Gtk.SpinButton()
        self.unidades.set_adjustment(adjustment)
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        box.set_homogeneous(True) 
        box.pack_start(label_unidades, True, True, 0)
        box.pack_start(self.unidades, True, True, 0)
        
        grid = Gtk.Grid()
        grid.add(name_combo)
        grid.attach_next_to(box, name_combo, Gtk.PositionType.BOTTOM, 1, 1)

        main_box = self.get_content_area()
        main_box.add(grid)

    def on_name_combo_changed(self, combo):
        
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            self.cost, self.drink = model[tree_iter][:2]
            print("Selected: Cost=%d, name=%s" % (self.cost, self.drink))
        else:
            entry = combo.get_child()
            print("Entered: %s" % entry.get_text())
    
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, boolean):
        if isinstance(boolean, bool):
            print("cambia estado")
            print(boolean)
            self._state = boolean
        else:
            print("No es booleano")
            return False
    
    
