from about_dialog import AboutDialog
from create_RowsAndBoxs import create_box, create_row
from dialog_show_tree import DialogShowTree
from file_actions import open_file, save_data
from dialog_confirm_order import Dialog_confirm_order
from dialog_add_drink import Dialog_add_drink
from file_chooser import FileChooser
import datetime
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Main(Gtk.Window):

    def __init__(self):
        super().__init__(title="HeaderBar Demo")
        self.file = None
        self.burguer_price = 3500
        self.set_border_width(10)
        self.set_default_size(400, 100)

        HB = Gtk.HeaderBar()
        HB.set_show_close_button(True)
        HB.props.title = "ARMA TU RICA"
        self.set_titlebar(HB)

        self.button_open_file = Gtk.Button.new_from_icon_name(
            "gtk-open", Gtk.IconSize.MENU)
        self.button_open_file.connect("clicked", self.button_open_file_clicked)
        HB.pack_start(self.button_open_file)

        self.button_about = Gtk.Button.new_from_icon_name(
            "gtk-about", Gtk.IconSize.MENU)
        self.button_about.connect("clicked", self.button_about_clicked)
        HB.pack_start(self.button_about)

        self.listbox = Gtk.ListBox()
        self.listbox.set_selection_mode(Gtk.SelectionMode.NONE)

        label_unidades = Gtk.Label(label="Unidades")
        adjustment = Gtk.Adjustment(upper=100, step_increment=1, page_increment=10)
        self.unidades = Gtk.SpinButton()
        self.unidades.set_adjustment(adjustment)
        self.unidades.connect("value-changed", self.units_changed)
        box = create_box(label_unidades, self.unidades)
        row_1 = Gtk.ListBoxRow()
        row_1.add(box)
        self.listbox.add(row_1)

        label = "Pan"
        pancitos = [
            "Betarraga",
            "Espinaca",
            "Zapallo"
        ]
        row_2, self.combo_panes = create_row(label, lista=pancitos)
        self.listbox.add(row_2)

        label = "Hamburguesa"
        hamburguesas = [
            "Garbanzos",
            "Lentejas",
            "Porotos negros "
        ]
        row_3, self.combo_hamburguesa = create_row(label, lista=hamburguesas)
        self.listbox.add(row_3)

        label = "Agregados"
        agregados = [
            "Palta",
            "Tomate",
            "Cebolla Dulce",
            "Choclo",
            "Lechuga",
            "Champiñones",
            "Poroto Verde",
            "Ají"
        ]

        row_4, self.combo_agregados = create_row(label, lista=agregados)
        self.listbox.add(row_4)

        label = "Mayonesa"
        mayonesas = [
            "Zanahoria",
            "Ajo",
            "Mixta"
        ]
        row_5, self.combo_mayonesas = create_row(label, lista=mayonesas)
        self.listbox.add(row_5)

        label_bebestible = Gtk.Label(label="Bebestible")
        self.button1 = Gtk.RadioButton.new_with_label_from_widget(None, "Si")
        self.button1.connect("toggled", self.on_button_toggled, "Si")
        self.button2 = Gtk.RadioButton.new_from_widget(self.button1)
        self.button2.set_label("No")
        self.button2.connect("toggled", self.on_button_toggled, "No")
        hbox = Gtk.Box(spacing=3)
        hbox.pack_start(self.button1, False, False, 0)
        hbox.pack_start(self.button2, False, False, 0)

        box = create_box(label_bebestible, hbox)
        row_6 = Gtk.ListBoxRow()
        row_6.add(box)
        self.listbox.add(row_6)

        continue_button = Gtk.Button(label="Continuar")
        continue_button.connect("clicked", self.continue_button_clicked)
        delate_button = Gtk.Button(label="Borrar")
        delate_button.connect("clicked", self.delate_button_clicked)
        box = create_box(delate_button, continue_button)
        row_7 = Gtk.ListBoxRow()
        row_7.add(box)
        self.listbox.add(row_7)

        self.message = Gtk.Label()
        self.message.set_label("Abrir archivo con data historica para habilitar operaciones")

        self.add(self.message)
    
        self.connect("destroy", Gtk.main_quit)

        self.show_all()

    def units_changed(self, scroll):
        print("Unidades: ",self.unidades.get_value_as_int())

    def on_button_toggled(self, button, name):

        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Boton", name, "pasa a estado", state)

    def continue_button_clicked(self, widget):

        combos = [self.combo_panes, self.combo_hamburguesa, 
        self.combo_agregados, self.combo_mayonesas]

        if self.unidades.get_value_as_int() != 0:
            for combo in combos:
                if combo.get_active_iter() is not None:
                    continue
                else:
                    print("Error, linea de seleccion sin completar.")
                    return
        else:
            print("Error, agregue minimo de una unidad.")
            return 

        self.dialog_add_drink = Dialog_add_drink(self)
        self.add(self.dialog_add_drink)
        if self.button1.get_active():
            self.dialog_add_drink.show_all()
            self.dialog_add_drink.state = True
            response = self.dialog_add_drink.run()
            if response == Gtk.ResponseType.OK:
                print("OK clicked")
                print(self.dialog_add_drink.state)
                self.open_dialog_confirm_order()
            elif response == Gtk.ResponseType.CANCEL:
                print("Cancel clicked")
            self.dialog_add_drink.destroy()
        else:
            self.dialog_add_drink.state = False
            self.open_dialog_confirm_order()
    
    def open_dialog_confirm_order(self):
        
        total_burguer_price = self.burguer_price * self.unidades.get_value_as_int()
        self.dialog_confirm_order = Dialog_confirm_order(self, total_burguer_price,\
                self.dialog_add_drink.total_cost)
        self.dialog_confirm_order.show_all()
        response = self.dialog_confirm_order.run()
        if response == Gtk.ResponseType.OK:
            print("OK clicked")
            self.ok_button_clicked()
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        self.dialog_confirm_order.destroy()
    
    """ se aprieta boton Ok tal que se añade data ingresada por usuario"""
    def ok_button_clicked(self):

        current_time = datetime.datetime.now()
        current_time = str(current_time)

        data = open_file(self.file)
        new_data = {"Fecha": str(current_time),
                    "Nombre": str(self.dialog_confirm_order.get_name),
                    "Metodo de Pago": str(self.dialog_confirm_order.get_payment_method),
                    "Costo pedido": str(self.dialog_confirm_order.get_order_cost)
                    }

        data.append(new_data)
        save_data(data, self.file)

    def delate_button_clicked(self, widget):
        pass

    def button_open_file_clicked(self, widget):
        
        flchooser = FileChooser(parent=self)

        response = flchooser.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            file = flchooser.get_filename()
            print("File selected: " + file)
            file_name = flchooser.get_filename()
            file_name = file_name.split("/")
            if file_name[-1] == "registro_de_pedidos.json":
                self.message.destroy()
                self.add(self.listbox)
                self.show_all()
                self.file = file
                dialog_show_tree = DialogShowTree(self)
                dialog_show_tree.tree.load_json_data(self.file)
            else:
                print("Archivo es incompatible a mostrar en TreeView.")
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        flchooser.destroy()

    def button_about_clicked(self, widget):
        AboutDialog()


if __name__ == "__main__":
    # Llama
    Main()
    Gtk.main()
