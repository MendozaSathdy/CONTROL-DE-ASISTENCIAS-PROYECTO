import tkinter as tk
from tkinter import messagebox

class Empleado:
    def __init__(self, nombre, id_empleado, puesto, genero, edad, turno="Sin asignar", jornada="Sin asignar"):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.puesto = puesto
        self.genero = genero
        self.edad = edad
        self.turno = turno
        self.jornada = jornada
        self.vacaciones = []
        self.asistencias = []

    def asignar_vacacion(self, periodo):
        self.vacaciones.append(periodo)

    def registrar_asistencia(self, estado):
        self.asistencias.append(estado)

class ControlAsistenciaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bienvenido al Control de Asistencia - Hospital")
        self.root.geometry("600x600")
        self.empleados = []
        self.periodos_disponibles = self.generar_periodos()

        self.bg_color = "grey"
        self.menu_color = "blue"
        self.fg_color = "white"
        self.highlight = "blue"

        self.menu_frame = tk.Frame(self.root, bg=self.menu_color, width=200)
        self.menu_frame.pack(side="left", fill="y")

        self.content_frame = tk.Frame(self.root, bg=self.bg_color)
        self.content_frame.pack(side="right", expand=True, fill="both")

        self.crear_boton_menu("Bienvenid@", self.mostrar_inicio)
        self.crear_boton_menu("datos del trabajador", self.mostrar_registro)
        self.crear_boton_menu("Vacaciones", self.mostrar_vacaciones)
        self.crear_boton_menu("Registro de Asistencia", self.mostrar_asistencia)
        self.crear_boton_menu("Historial", self.mostrar_historial)

        self.seccion_actual = None
        self.mostrar_inicio()

    def generar_periodos(self):
        meses = [
            "Ene", "Feb", "Mar", "Abr", "May", "Jun",
            "Jul", "Ag", "Sep", "Oct", "Nov", "Dic"
        ]
        periodos = []
        for mes in meses:
            periodos.append(f"{mes} 1 - {mes} 15")
            periodos.append(f"{mes} 16 - {mes} 30-1")
        return periodos

    def crear_boton_menu(self, texto, comando):
        boton = tk.Button(self.menu_frame, text=texto, bg=self.menu_color,
                          fg=self.fg_color, activebackground=self.highlight,
                          font=("Arial", 12), relief="flat", command=comando)
        boton.pack(fill="x", pady=5, padx=10)

    def limpiar_seccion_actual(self):
        if self.seccion_actual:
            self.seccion_actual.destroy()

    def mostrar_inicio(self):
        self.limpiar_seccion_actual()
        self.seccion_actual = tk.Frame(self.content_frame, bg=self.bg_color)
        self.seccion_actual.pack(fill="both", expand=True)

        tk.Label(self.seccion_actual, text="Bienvenido al Registro de asistencias de un hospital",
                 font=("Arial", 24, "bold"), bg=self.bg_color).pack(pady=100)

    def mostrar_registro(self):
        self.limpiar_seccion_actual()
        self.seccion_actual = tk.Frame(self.content_frame, bg=self.bg_color)
        self.seccion_actual.pack(fill="both", expand=True)

        tk.Label(self.seccion_actual, text="Registrar Empleado", font=("Arial", 16, "bold"), bg=self.bg_color).pack(pady=20)

        campos = ["Nombre", "ID", "Edad"]
        entradas = {}
        for campo in campos:
            tk.Label(self.seccion_actual, text=f"{campo}:", bg=self.bg_color, font=("Arial", 12)).pack()
            entrada = tk.Entry(self.seccion_actual, font=("Arial", 12))
            entrada.pack(pady=5)
            entradas[campo] = entrada

        tk.Label(self.seccion_actual, text="Género:", bg=self.bg_color, font=("Arial", 12)).pack()
        genero_var = tk.StringVar(value="Masculino")
        tk.OptionMenu(self.seccion_actual, genero_var, "Masculino", "Femenino", "Otro").pack(pady=5)

        tk.Label(self.seccion_actual, text="Puesto:", bg=self.bg_color, font=("Arial", 12)).pack()
        puestos = ["Médico", "Enfermero(a)", "Administrativo", "Seguridad", "Personal de limpieza"]
        puesto_var = tk.StringVar(value=puestos[0])
        tk.OptionMenu(self.seccion_actual, puesto_var, *puestos).pack(pady=5)

        tk.Label(self.seccion_actual, text="Turno:", bg=self.bg_color, font=("Arial", 12)).pack()
        turnos = ["Matutino", "Vespertino", "Nocturno"]
        turno_var = tk.StringVar(value=turnos[0])
        tk.OptionMenu(self.seccion_actual, turno_var, *turnos).pack(pady=5)

        def guardar():
            nombre = entradas["Nombre"].get()
            id_empleado = entradas["ID"].get()
            edad = entradas["Edad"].get()
            genero = genero_var.get()
            puesto = puesto_var.get()
            turno = turno_var.get()
            if nombre and id_empleado and edad:
                self.empleados.append(Empleado(nombre, id_empleado, puesto, genero, edad, turno))
                messagebox.showinfo("Éxito", f"Empleado {nombre} registrado correctamente.")
                self.mostrar_registro()
            else:
                messagebox.showwarning("Error", "Por favor completa todos los espacios.")

        tk.Button(self.seccion_actual, text="Guardar", font=("Arial", 12),
                  bg=self.highlight, fg="white", command=guardar).pack(pady=15)

    def mostrar_vacaciones(self):
        self.limpiar_seccion_actual()
        self.seccion_actual = tk.Frame(self.content_frame, bg=self.bg_color)
        self.seccion_actual.pack(fill="both", expand=True)

        tk.Label(self.seccion_actual, text="Vacaciones", font=("Arial", 16, "bold"), bg=self.bg_color).pack(pady=20)

        if not self.empleados:
            tk.Label(self.seccion_actual, text="No hay empleados registrados.", font=("Arial", 12), bg=self.bg_color).pack()
            return

        seleccionado = tk.StringVar()
        periodo_var = tk.StringVar()

        tk.Label(self.seccion_actual, text="Selecciona empleado:", bg=self.bg_color, font=("Arial", 12)).pack()
        nombres = [emp.nombre for emp in self.empleados]
        seleccionado.set(nombres[0])
        tk.OptionMenu(self.seccion_actual, seleccionado, *nombres).pack(pady=5)

        tk.Label(self.seccion_actual, text="Selecciona periodo:", bg=self.bg_color, font=("Arial", 12)).pack()
        if self.periodos_disponibles:
            periodo_var.set(self.periodos_disponibles[0])
        tk.OptionMenu(self.seccion_actual, periodo_var, *self.periodos_disponibles).pack(pady=5)

        def asignar():
            nombre = seleccionado.get()
            periodo = periodo_var.get()
            for emp in self.empleados:
                if emp.nombre == nombre:
                    emp.asignar_vacacion(periodo)
                    self.periodos_disponibles.remove(periodo)
                    messagebox.showinfo("Éxito", f"Vacación asignada a {nombre}")
                    self.mostrar_vacaciones()
                    break

        tk.Button(self.seccion_actual, text="Asignar Vacación", font=("Arial", 12),
                  bg=self.highlight, fg="white", command=asignar).pack(pady=10)

    def mostrar_asistencia(self):
        self.limpiar_seccion_actual()
        self.seccion_actual = tk.Frame(self.content_frame, bg=self.bg_color)
        self.seccion_actual.pack(fill="both", expand=True)

        tk.Label(self.seccion_actual, text="Registro de Asistencia", font=("Arial", 16, "bold"), bg=self.bg_color).pack(pady=20)

        if not self.empleados:
            tk.Label(self.seccion_actual, text="No hay empleados registrados.", font=("Arial", 12), bg=self.bg_color).pack()
            return

        seleccionado = tk.StringVar()
        seleccionado.set(self.empleados[0].nombre)
        tk.OptionMenu(self.seccion_actual, seleccionado, *[e.nombre for e in self.empleados]).pack(pady=5)

        estados = ["Trabajó", "Faltó", "Permiso", "Día libre"]
        estado_var = tk.StringVar(value=estados[0])
        tk.OptionMenu(self.seccion_actual, estado_var, *estados).pack(pady=5)

        def registrar():
            nombre = seleccionado.get()
            estado = estado_var.get()
            for emp in self.empleados:
                if emp.nombre == nombre:
                    emp.registrar_asistencia(estado)
                    messagebox.showinfo("Éxito", f"Asistencia registrada para {nombre}: {estado}")
                    break

        tk.Button(self.seccion_actual, text="Registrar Asistencia", font=("Arial", 12),
                  bg=self.highlight, fg="white", command=registrar).pack(pady=10)

    def mostrar_historial(self):
        self.limpiar_seccion_actual()
        self.seccion_actual = tk.Frame(self.content_frame, bg=self.bg_color)
        self.seccion_actual.pack(fill="both", expand=True)

        tk.Label(self.seccion_actual, text="Historial de Empleados", font=("Arial", 16, "bold"), bg=self.bg_color).pack(pady=10)

        if not self.empleados:
            tk.Label(self.seccion_actual, text="No hay empleados registrados.", font=("Arial", 12), bg=self.bg_color).pack()
            return

        text_area = tk.Text(self.seccion_actual, font=("Arial", 11), wrap="word", height=30)
        text_area.pack(expand=True, fill="both", padx=10, pady=10)

        for emp in self.empleados:
            text_area.insert("end", f"Nombre: {emp.nombre}\n")
            text_area.insert("end", f"ID: {emp.id_empleado} | Edad: {emp.edad} | Género: {emp.genero} | Puesto: {emp.puesto} | Turno: {emp.turno}\n")
            text_area.insert("end", f"Vacaciones: {', '.join(emp.vacaciones) if emp.vacaciones else 'Ninguna'}\n")
            text_area.insert("end", f"Asistencias: {', '.join(emp.asistencias) if emp.asistencias else 'Sin registros'}\n")
            text_area.insert("end", "-" * 50 + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ControlAsistenciaApp(root)
    root.mainloop()