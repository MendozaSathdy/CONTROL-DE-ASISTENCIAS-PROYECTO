import tkinter as tk
from tkinter import messagebox
#Detalles del empleado en su registro 
class Empleado:
    def __init__(self, nombre, id_empleado, puesto, genero, edad, fecha_nacimiento, grado_estudio, cedula, domicilio, telefono, correo, fecha_ingreso, tipo_contratacion):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.puesto = puesto
        self.genero = genero
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.grado_estudio = grado_estudio
        self.cedula = cedula
        self.domicilio = domicilio
        self.telefono = telefono
        self.correo = correo
        self.fecha_ingreso = fecha_ingreso
        self.tipo_contratacion = tipo_contratacion
#se configura la ventana principal con título y dimensiones tambien entra color en la pantalla 
class ControlAsistenciaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Control de Asistencia - Hospital")
        self.root.geometry("800x600")
        self.empleados = []

        self.bg_color = "grey"
        self.menu_color = "blue"
        self.fg_color = "white"
        self.highlight = "brown"

        self.menu_frame = tk.Frame(self.root, bg=self.menu_color, width=200)
        self.menu_frame.pack(side="left", fill="y")

        self.content_frame = tk.Frame(self.root, bg=self.bg_color)
        self.content_frame.pack(side="right", expand=True, fill="both")

        # Menú lateral
        self.crear_boton_menu("Bienvenid@", self.mostrar_inicio)
        self.crear_boton_menu("Datos del Trabajador", self.mostrar_registro)
        self.crear_boton_menu("Historial", self.mostrar_historial)

        self.seccion_actual = None
        self.mostrar_inicio()
    #limpia la pantalla y da los botones en el menu lateral 
    def crear_boton_menu(self, texto, comando):
        boton = tk.Button(self.menu_frame, text=texto, bg=self.menu_color,
                          fg=self.fg_color, activebackground=self.highlight,
                          font=("Arial", 12), relief="flat", command=comando)
        boton.pack(fill="x", pady=5, padx=10)

    def limpiar_seccion_actual(self):
        if self.seccion_actual:
            self.seccion_actual.destroy()

    #Bienvenida
    def mostrar_inicio(self):
        self.limpiar_seccion_actual()
        self.seccion_actual = tk.Frame(self.content_frame, bg=self.bg_color)
        self.seccion_actual.pack(fill="both", expand=True)

        tk.Label(self.seccion_actual, text="Bienvenido al Control de Asistencias de un Hospital",
                 font=("Arial", 24, "bold"), bg=self.bg_color).pack(pady=100)

    #Sección de los Datos del Trabajador 
    def mostrar_registro(self):
        self.limpiar_seccion_actual()
        self.seccion_actual = tk.Frame(self.content_frame, bg=self.bg_color)
        self.seccion_actual.pack(fill="both", expand=True)

        tk.Label(self.seccion_actual, text="Registrar Empleado", font=("Arial", 16, "bold"), bg=self.bg_color).grid(row=0, column=0, columnspan=2, pady=10)

        campos = ["Nombre", "ID", "Edad", "Fecha de Nacimiento", "Cédula Profesional", "Domicilio", "Teléfono", "Correo Electrónico", "Fecha de Ingreso"]
        entradas = {}
        for i, campo in enumerate(campos):
            tk.Label(self.seccion_actual, text=f"{campo}:", bg=self.bg_color, font=("Arial", 12)).grid(row=i+1, column=0, sticky="e", padx=5, pady=5)
            entrada = tk.Entry(self.seccion_actual, font=("Arial", 12))
            entrada.grid(row=i+1, column=1, padx=5, pady=5)
            entradas[campo] = entrada

        tk.Label(self.seccion_actual, text="Género:", bg=self.bg_color, font=("Arial", 12)).grid(row=10, column=0, sticky="e", padx=5, pady=5)
        genero_var = tk.StringVar(value="Masculino")
        tk.OptionMenu(self.seccion_actual, genero_var, "Masculino", "Femenino", "Otro").grid(row=10, column=1, padx=5, pady=5)

        tk.Label(self.seccion_actual, text="Puesto:", bg=self.bg_color, font=("Arial", 12)).grid(row=11, column=0, sticky="e", padx=5, pady=5)
        puestos = ["Médico", "Enfermero(a)", "Administrativo", "Seguridad", "Personal de limpieza"]
        puesto_var = tk.StringVar(value=puestos[0])
        tk.OptionMenu(self.seccion_actual, puesto_var, *puestos).grid(row=11, column=1, padx=5, pady=5)

        tk.Label(self.seccion_actual, text="Último Grado de Estudio:", bg=self.bg_color, font=("Arial", 12)).grid(row=12, column=0, sticky="e", padx=5, pady=5)
        grados = ["Secundaria", "Preparatoria", "Licenciatura", "Maestría", "Doctorado"]
        grado_var = tk.StringVar(value=grados[0])
        tk.OptionMenu(self.seccion_actual, grado_var, *grados).grid(row=12, column=1, padx=5, pady=5)

        tk.Label(self.seccion_actual, text="Tipo de Contratación:", bg=self.bg_color, font=("Arial", 12)).grid(row=13, column=0, sticky="e", padx=5, pady=5)
        tipos_contratacion = ["Basificados", "Homologados", "Regularizados"]
        tipo_contratacion_var = tk.StringVar(value=tipos_contratacion[0])
        tk.OptionMenu(self.seccion_actual, tipo_contratacion_var, *tipos_contratacion).grid(row=13, column=1, padx=5, pady=5)

        def guardar():
            datos = {campo: entradas[campo].get() for campo in campos}
            genero = genero_var.get()
            puesto = puesto_var.get()
            grado_estudio = grado_var.get()
            tipo_contratacion = tipo_contratacion_var.get()

            if all(datos.values()):
                # crea un nuevo empleado 
                self.empleados.append(Empleado(
                    datos["Nombre"], datos["ID"], puesto, genero,
                    datos["Edad"], datos["Fecha de Nacimiento"], grado_estudio,
                    datos["Cédula Profesional"], datos["Domicilio"], datos["Teléfono"],
                    datos["Correo Electrónico"], datos["Fecha de Ingreso"], tipo_contratacion
                ))
                messagebox.showinfo("Éxito", f"Empleado {datos['Nombre']} registrado correctamente.")

                # Limpia para poder agregar otro 
                for campo in campos:
                    entradas[campo].delete(0, tk.END)
                genero_var.set("Masculino")
                puesto_var.set(puestos[0])
                grado_var.set(grados[0])
                tipo_contratacion_var.set(tipos_contratacion[0])

            else:
                messagebox.showwarning("Error", "Por favor completa todos los espacios.")

        #Guarda la informacion 
        tk.Button(self.seccion_actual, text="Guardar", font=("Arial", 12),
                  bg=self.highlight, fg="white", command=guardar).grid(row=14, column=0, columnspan=2, pady=15)

    # Da el historial de los empleados que ingresaron 
    def mostrar_historial(self):
        self.limpiar_seccion_actual()
        self.seccion_actual = tk.Frame(self.content_frame, bg=self.bg_color)
        self.seccion_actual.pack(fill="both", expand=True)

        tk.Label(self.seccion_actual, text="Historial de Empleados", font=("Arial", 16, "bold"), bg=self.bg_color).pack(pady=10)

        if not self.empleados:
            tk.Label(self.seccion_actual, text="No hay empleados registrados.", font=("Arial", 12), bg=self.bg_color).pack()
            return

        tk.Label(self.seccion_actual, text="Introduce el ID del empleado para ver su historial:", font=("Arial", 12), bg=self.bg_color).pack(pady=10)

        id_empleado_var = tk.StringVar()

        id_entry = tk.Entry(self.seccion_actual, textvariable=id_empleado_var, font=("Arial", 12))
        id_entry.pack(pady=10)

        def mostrar_datos():
            id_empleado = id_empleado_var.get()
            empleado_encontrado = None
            for emp in self.empleados:
                if emp.id_empleado == id_empleado:
                    empleado_encontrado = emp
                    break

            if empleado_encontrado:
                # Muestra los datos 
                text_area = tk.Text(self.seccion_actual, font=("Arial", 11), wrap="word", height=20)
                text_area.pack(expand=True, fill="both", padx=10, pady=10)

                text_area.insert("end", f"Nombre: {empleado_encontrado.nombre}\n")
                text_area.insert("end", f"ID: {empleado_encontrado.id_empleado} | Edad: {empleado_encontrado.edad} | Género: {empleado_encontrado.genero} | Puesto: {empleado_encontrado.puesto} | Fecha de Nacimiento: {empleado_encontrado.fecha_nacimiento} | Grado de Estudio: {empleado_encontrado.grado_estudio} | Cédula: {empleado_encontrado.cedula} | Domicilio: {empleado_encontrado.domicilio} | Teléfono: {empleado_encontrado.telefono} | Correo: {empleado_encontrado.correo} | Fecha de Ingreso: {empleado_encontrado.fecha_ingreso} | Tipo de Contratación: {empleado_encontrado.tipo_contratacion}\n")
                text_area.insert("end", "-" * 50 + "\n")
            else:
                messagebox.showwarning("Error", "Empleado no encontrado con ese ID.")

        tk.Button(self.seccion_actual, text="Buscar", font=("Arial", 12),
                  bg=self.highlight, fg="white", command=mostrar_datos).pack(pady=15)

if __name__ == "__main__":
    root = tk.Tk()
    app = ControlAsistenciaApp(root)
    root.mainloop()

