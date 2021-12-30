from tkinter import ttk
from tkinter import *
import webbrowser

class errors:
    def __init__(self, type_error):
        self.error = type_error
    def sort_out_error(self):
        if self.error == 'selection_error':
            self.error = 'Error de selección'
        if self.error == 'create_file_error':
            self.error = 'Error de tabla'
        return self.error       
        
class aplication:
    def __init__(self, window):
        
        self.wind = window
        self.wind.title('Stadistic creators')
        self.wind.resizable(0,0)
        #self.ico = r'C:UsersJESUS DAVID PEREZDocumentsPROYECTOS EN PYTHONGrandesProyectos.pyStadisticsAppIcon.ico'
        #self.wind.iconbitmap(self.ico)

        # Main frame
        self.main = LabelFrame(self.wind, text='Selecciona una opción')
        self.main.grid(row = 0, column = 0, pady = 5, padx = 5)
        # Main menu
        self.main_menu = Menu(self.wind)
        self.file_menu = Menu(self.main_menu, tearoff = 0)
        self.edit_menu = Menu(self.main_menu, tearoff = 0)
        self.help_menu = Menu(self.main_menu, tearoff = 0)

        self.file_menu.add_command(label = 'Nuevo', command = self.program_new)
        self.file_menu.add_command(label = 'Guardar')
        self.file_menu.add_separator()
        self.file_menu.add_command(label = 'Salir', command = self.wind.destroy)
        
        self.edit_menu.add_command(label = 'Cortar')
        self.edit_menu.add_command(label = 'Copiar')
        self.edit_menu.add_command(label = 'Pegar')
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label = 'Moda')
        self.edit_menu.add_command(label = 'Mediana')
        self.edit_menu.add_command(label = 'Media aritmetica')
        
        self.help_menu.add_command(label = 'Bienvenido', command = self.help_window)
        self.help_menu.add_separator()
        self.help_menu.add_command(label = 'Como se usa', command = self.help_window)
        self.help_menu.add_command(label = 'Redes sociales', command = self.execute_web)
        self.help_menu.add_separator()
        self.help_menu.add_command(label = 'Acerca de...', command = self.help_window)
        self.help_menu.add_command(label = 'Licencia', command = self.help_window)

        # Cascades
        self.main_menu.add_cascade(label = 'Archivo', menu = self.file_menu)
        self.main_menu.add_cascade(label = 'Editar', menu = self.edit_menu)
        self.main_menu.add_cascade(label = 'Ayuda', menu = self.help_menu)
        self.wind['menu'] = self.main_menu

        # Select class button
        Button(self.wind, text = 'Crear tabla', relief = GROOVE, command = self.create_table).grid(sticky = W + E, columnspan = 2, padx = 5)
        # Table in a tree view
        self.table = ttk.Treeview(self.main, height = 6)
        self.table.heading('#0' ,text = 'Clases de tablas')
        self.table.insert('', 0, text = 'Ingreso manual')
        self.table.insert('', 0, text = 'Ingreso de intervalos')
        self.table.grid()

        # Message updater
        self.message_screen = Label(self.wind, text = 'Selecciona una opción', foreground = 'red')
        self.message_screen.grid(row = 2, sticky = W + E)

    # MENU OPTIONS/FILE
    # Create a new program using recursion
    def program_new(self): 
        self.new = Tk()
        self.new_app = aplication(self.new)
        self.new.mainloop()
    # MENU OPTIONS/HELP
    def help_window(self):
        self.help_wind = Toplevel(self.wind)
        self.help_wind.title('Help')
        self.help_wind.geometry('320x415')
        self.help_wind.resizable(0,0)
        # Help label frame
        self.help_label_frame = LabelFrame(self.help_wind, text = 'Ayuda')
        self.help_label_frame.grid(padx = 5, pady = 5)
        # Content 
        Label(self.help_label_frame, text = 'Bienvenido:', justify = LEFT).grid(row = 0, columnspan = 15, padx = 5, pady = 5)
        Message(self.help_label_frame, width = 300,text = (
            'Este programa te será útil para crear tablas estadisticas en cuestión de segundos, solamente debes tener los conceptos claros '
        )).grid(row = 1)
        Label(self.help_label_frame, text = 'Como se usa:', justify = LEFT).grid(row = 2, padx = 5, pady = 5)
        Message(self.help_label_frame, width = 300, text = (
            'Iniclamente selecciona una de las opciones de tabla (Que clase de datos manejas, y de que forma los vas a ingresar). Luego ingresa los datos de la forma en como escogiste'
        )).grid(row = 3)
        Label(self.help_label_frame, text = 'Acerca de:', justify = LEFT).grid(row = 4, padx = 5, pady = 5)
        Message(self.help_label_frame, width = 300, justify = LEFT, text = (
            'Programa desarollado en Python importing Tkinter libraries')).grid(row = 5, column = 0)
        Label(self.help_label_frame, text = 'Licencia:', justify = LEFT).grid(row = 6, padx = 5, pady = 5)
        Message(self.help_label_frame, width = 300, justify = LEFT, text = (
            'La distribucionn de este programa debe ser concedida bajo la autorización del desarollador'
        )).grid(row = 7, padx = 5, pady = 5)
        Label(self.help_label_frame, justify = LEFT, text = 'CORREO DE CONTACTO ').grid(row = 8, padx = 5, pady = 5)
        Entry(self.help_label_frame, state = 'readonly', textvariable = StringVar(value = 'expresspiano57@gmail.com')).grid(row = 9, padx = 5, pady = 5)
    # Open page web        
    def execute_web(self):
        webbrowser.open('https://www.youtube.com/channel/UC120Xrak1Ccx32K12nElL7w')
    

    # Validation about class of table
    def validate_type_input(self):
        print(self.table.selection())
        print(self.table.item(self.table.selection()))
        input_class = (self.table.item(self.table.selection())['text'])
        if input_class == 'Ingreso manual' :
            self.message_screen['text'] = ''
            return 'manual'
        elif input_class == 'Ingreso de intervalos':
            self.message_screen['text'] = ''
            return 'interv'
        else:
            #self.select_table.destroy()
            self.content_message = errors('selection_error')
            self.message_screen['text'] = self.content_message.sort_out_error()      
            return 'error' # There's any error
    def create_table(self):  
        self.select_table = Toplevel(self.wind)
        self.select_table.title('Select table')
        self.select_table.resizable(0,0)
        self.select_table.iconbitmap(self.ico)

        if self.validate_type_input() == 'error':
            print(self.content_message)
            return
        # Frame container
        self.label_frame_select = LabelFrame(self.select_table, text = 'Selecciona una clase de tabla') 
        self.label_frame_select.grid(padx = 5, pady = 5)
        # Tree view of options
        self.tree_select = ttk.Treeview(self.label_frame_select, height = 3)
        self.tree_select.heading('#0', text = 'Tipos de datos')
        self.tree_select.insert('', 0, text = 'Cuantitativos')
        self.tree_select.insert('', 0, text = 'Cualitativos')
        self.tree_select.grid()
        # Continue button
        Button(self.select_table, relief = GROOVE, text = 'Continuar', command = self.table_total).grid(row = 1,padx = 5, sticky = W + E)
        
    # Validating creation of table
    def validate_creation(self):
        #input_data = (self.tree_select.item(self.tree_select.selection())['text'])
        input_data = (self.tree_select.item(self.tree_select.selection())['text'])
        if input_data == 'Cuantitativos':
            self.message_screen['text'] = ''
            return 'cuant'
        elif input_data == 'Cualitativos':
            self.message_screen['text'] = ''
            return 'cuali'
        else:
            #self.table_wind.destroy()
            self.content_message = errors('selection_error')
            self.message_screen['text'] = self.content_message.sort_out_error()
            return 'error'
    # keeping up with table data    
    def table_total(self):
        self.table_wind = Toplevel(self.wind)
        self.table_wind.title('Tabla estadistica')
        self.table_wind.iconbitmap(self.ico)
        self.table_wind.resizable(0,0)
        if self.validate_creation() == 'error':
            print(self.content_message)
            return

        # Frame table
        self.frame_table = LabelFrame(self.table_wind, text = 'Tabla')
        self.frame_table.grid(padx = 10, pady = 5)
        # Tree view about all table
        self.table = ttk.Treeview(self.frame_table, height = 3, columns = ('fi', 'Fi', 'xi'))
        self.table.grid(padx = 5)
        self.table.heading('#0', text = 'Intervalos' )
        self.table.heading('fi', text = 'fi')
        self.table.heading('Fi', text = 'Fi')
        self.table.heading('xi', text = 'xi')
        
        

if __name__ == '__main__':
    window = Tk()
    app = aplication(window)

    window.mainloop()
