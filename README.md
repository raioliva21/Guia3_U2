# Guia3_U2
Guia evaluada N°3 U2 modulo programacion avanzada 2022

# Finalidad de programa
Este pograma tiene por objetivo facilitar el registro de data asociada a pedidos de local de comida hipotetico mediante la manipulacion de widgets.

# Creacion de objetos
1. Main: Objeto clase Main que hereda de la clase Gtk.Window.
  - Atriubutos:
      (caracter publico)
  -   self.file = None #ruta de archivo habilitado a mostrar en treeview
    - self.burguer_price = 3500 #precio estandar de burguer
    - HB = Gtk.HeaderBar() #configura titlebar de self
    - self.button_open_file y self.button_about #se adhieren a atributo HB
      -signal "clicked" de boton self.button_open_file asocia a callback self.button_open_file_clicked
      -signal "clicked" de boton self.button_about asocia a callback self.button_about_clicked
    - self.listbox = Gtk.ListBox() #listbox mostrada en interfaz grafica al abrir archivo especifico 
      -objetos seran agregados a 'filas' de self.listbox
    - self.message = Gtk.Label() #label que sera mostrado en interfaz grafica mientras no se abra archivo especifico para habilitar operaciones
    
  - Metodos:
    - Metodos propios
      - open_dialog_confirm_order(self) #abre ventana de dialogo asociada a clase Dialog_confirm_order
      file:///home/raimundoosf/Im%C3%A1genes/Captura%20de%20pantalla%20de%202022-06-10%2011-13-59.png![imagen](https://user-images.githubusercontent.com/89752816/173096634-039b7640-be99-44d5-abad-6aa66145da40.png)

      - confirm_button_clicked(self) #ocurre cuando usuario confirma orden, tal que se agrega linea (orden) a archivo de data historica.
      file:///home/raimundoosf/Im%C3%A1genes/Captura%20de%20pantalla%20de%202022-06-10%2010-58-50.png![imagen](https://user-images.githubusercontent.com/89752816/173093760-cbe711e0-335b-47b5-a4ae-0d44a4ff097d.png)
      
    - Metodos (callbacks) asociados a objetos contenidos en clase Main
      - units_changed(self, scroll) #imprime cambio de objeto self.unidades clase Gtk.SpinButton
      - on_button_toggled(self, button, name) #ocurre al haber señal "toggled" en objeto de tipo Gtk.RadioButton
      - continue_button_clicked(self, widget) #ocurre si usuario aprieta boton continuar en GUI, tal que se verifica si todas las lineas han sido llenadas
      - delate_button_clicked(self, widget) #vuelve a opciones prefijadas al abrir programa
      - button_open_file_clicked(self, widget) #llama a objeto de clase heredada de clase Gtk.FileChooser, tal que se abre ventana para abrir archivo.
      - button_about_clicked(self, widget) #crea instancia de clase AboutDialog heredada de clase Gtk.AboutDialog
      
      

