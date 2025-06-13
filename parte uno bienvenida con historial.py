import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Control de Asistencia")
        self.empleados = []

        #creacion de el menu del lado izquierdo con botones y tambien color,tamano, etc.
        self.menu_frame = tk.Frame(self.root, width=200, bg="blue")
        self.menu_frame.pack(side="left", fill="y")
        self.content_frame = tk.Frame(self.root, bg="grey")
        self.content_frame.pack(side="right", expand=True, fill="both")

       
        self.crear_boton_menu("Bienvenid@", self.mostrar_inicio)
        self.crear_boton_menu("Historial", self.mostrar_historial)
        self.seccion_actual = None
        self.mostrar_inicio()
    # color de letra y del menu este indica que funcion se ejecutara 
    def crear_boton_menu(self, texto, comando):
        tk.Button(self.menu_frame, text=texto, bg="blue", fg="white", font=("Arial", 12), command=comando).pack(fill="x", pady=5)

    def limpiar_seccion_actual(self):
        if self.seccion_actual:
            self.seccion_actual.destroy()

    
    def mostrar_inicio(self):
        self.limpiar_seccion_actual()
        tk.Label(self.content_frame, text="Bienvenido al Control de Asistencias de un Hospital", font=("Arial", 24, "bold"), bg="grey").pack(pady=100)

    #Muestra si hay empleados registrados 
    def mostrar_historial(self):
        self.limpiar_seccion_actual()
        if not self.empleados:
            tk.Label(self.content_frame, text="No hay empleados registrados.", font=("Arial", 12), bg="grey").pack()
            return
        text_area = tk.Text(self.content_frame, font=("Arial", 11), height=10)
        text_area.pack(expand=True, fill="both", padx=10, pady=10)
        for emp in self.empleados:
            text_area.insert("end", f"{emp['nombre']} | {emp['id_empleado']} | {emp['edad']} | {emp['puesto']}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()