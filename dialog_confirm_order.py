from tkinter import dialog
from dialog_add_drink import Dialog_add_drink
from gi.repository import Gtk
import gi
gi.require_version("Gtk", "3.0")

class Dialog_confirm_order(Gtk.Dialog):

    def __init__(self, parent):
        super().__init__(title="Confirmar orden", transient_for=parent, flags=0)
        self._name = str
        self._cost = 3500
        self.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK
        )
        self.set_border_width(10)

        label_name = Gtk.Label(label="Nombre: ")
        self.name = Gtk.Entry()
        label_payment_method = Gtk.Label(label="Metodo de Pago: ")
        lista = ["Efectivo","Tarjeta Credito/Debito"]
        self.payment_method = Gtk.ComboBoxText()
        self.payment_method.set_entry_text_column(0)
        for indice in lista:
            self.payment_method.append_text(indice)
        #self.payment_method.set_active(0)
        self.total_pay = Gtk.Label(label=f"TOTAL: ${self._cost}")

        grid = Gtk.Grid()
        grid.add(label_name)
        grid.attach(self.name, 1, 0, 2, 1)
        grid.attach_next_to(label_payment_method, label_name, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(self.payment_method, label_payment_method, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(self.total_pay, label_payment_method, Gtk.PositionType.BOTTOM, 2, 1)

        self.add(grid)

        box = self.get_content_area()
        box.add(grid)

        #self.show_all()

    
    def get_name(self):
        return self.name.get_text()

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, add_cost):
        print("entra a metodo cost")
        if isinstance(add_cost, int):
            self._cost = self._cost + add_cost
            self.total_pay.set_label(f"TOTAL: ${self._cost}")
        else:
            print("Clase de variable: ",type(add_cost))
            print("Dato ingresado no corresponde a clase solicitada.")
            return False