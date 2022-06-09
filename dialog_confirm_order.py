from tkinter import dialog
from dialog_add_drink import Dialog_add_drink
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Dialog_confirm_order(Gtk.Dialog):

    def __init__(self, parent, TBC, TDC):
        super().__init__(title="Confirmar orden", transient_for=parent, flags=0)
        self._name = None
        self._total_burguer_cost = TBC
        self._total_drink_cost = TDC
        self._total_cost = self._total_burguer_cost +\
        self._total_drink_cost
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
        self.total_pay = Gtk.Label(label=f"TOTAL: ${self._total_cost}")

        grid = Gtk.Grid()
        grid.add(label_name)
        grid.attach(self.name, 1, 0, 2, 1)
        grid.attach_next_to(label_payment_method, label_name, \
        Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(self.payment_method, label_payment_method, \
        Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(self.total_pay, label_payment_method, \
        Gtk.PositionType.BOTTOM, 2, 1)

        #self.add(grid)
        box = self.get_content_area()
        box.add(grid)
        #self.add(box)


    @property
    def get_name(self):
        return self.name.get_text()
    
    @property
    def get_payment_method(self):
        return self.payment_method.get_active_text()

    @property
    def get_order_cost(self):
        return self._total_cost
    
    @get_order_cost.setter
    def get_order_cost(self, cost):
        if isinstance(cost, int):
            self._total_burguer_cost = cost
        else:
            return False

    @property
    def total_drink_cost(self):
        return self.total_drink_cost
    
    @total_drink_cost.setter
    def total_burguer_cost(self, cost):
        if isinstance(cost, int):
            self._total_drink_cost = cost
        else:
            return False

    
    