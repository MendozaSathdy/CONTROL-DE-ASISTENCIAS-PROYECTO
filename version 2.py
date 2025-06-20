import tkinter as tk
from tkinter import messagebox


class Empleado:
    def __init__(self, nombre, id_empleado, puesto, turno="Sin asignar", jornada="Sin asignar"):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.puesto = puesto
        self.turno = turno
        self.jornada = jornada
        self.vacaciones = []

    def asignar_vacacion(self, periodo):
        self.vacaciones.append(periodo)



class ControlAsistenciaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Control de Asistencia - Hospital")
        self.root.geometry("1000x600")
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

        
        self.crear_boton_menu("Registrar Empleado", self.mostrar_registro)
        self.crear_boton_menu("Vacaciones", self.mostrar_vacaciones)

        self.seccion_actual = None
        self.mostrar_registro()

    def generar_periodos(self):
        meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        periodos = []
        for mes in meses:
            periodos.append(f"{mes} 1 - {mes} 15")
            periodos.append(f"{mes} 16 - {mes} 30")
        return periodos

    def crear_boton_menu(self, texto, comando):
        boton = tk.Button(self.menu_frame, text=texto, bg=self.menu_color,
                          fg=self.fg_color, activebackground=self.highlight,
                          font=("Arial", 12), relief="flat", command=comando)
        boton.pack(fill="x", pady=5, padx=10)

    def limpiar_seccion_actual(self):
        if self.seccion_actual:
            self.seccion_actual.destroy()

    def mostrar_registro(self):
        self.limpiar_seccion_actual()
        self.seccion_actual = tk.Frame(self.content_frame, bg=self.bg_color)
        self.seccion_actual.pack(fill="both", expand=True)

        tk.Label(self.seccion_actual, text="Registrar Empleado", font=("Arial", 16, "bold"), bg=self.bg_color).pack(pady=20)

       
        tk.Label(self.seccion_actual, text="Nombre:", bg=self.bg_color, font=("Arial", 12)).pack()
        entrada_nombre = tk.Entry(self.seccion_actual, font=("Arial", 12))
        entrada_nombre.pack(pady=5)

      
        tk.Label(self.seccion_actual, text="ID:", bg=self.bg_color, font=("Arial", 12)).pack()
        entrada_id = tk.Entry(self.seccion_actual, font=("Arial", 12))
        entrada_id.pack(pady=5)

       
        tk.Label(self.seccion_actual, text="Puesto:", bg=self.bg_color, font=("Arial", 12)).pack()
        puestos = [
            "Médico",
            "Enfermero(a)",
            "Administrativo",
            "Seguridad",
            "Personal de limpieza"
        ]
        puesto_var = tk.StringVar()
        puesto_var.set(puestos[0])
        menu_puestos = tk.OptionMenu(self.seccion_actual, puesto_var, *puestos)
        menu_puestos.config(font=("Arial", 12))
        menu_puestos.pack(pady=5)

        def guardar():
            nombre = entrada_nombre.get()
            id_empleado = entrada_id.get()
            puesto = puesto_var.get()
            if nombre and id_empleado and puesto:
                self.empleados.append(Empleado(nombre, id_empleado, puesto))
                messagebox.showinfo("Éxito", f"Empleado {nombre} registrado correctamente.")
                self.mostrar_registro()
            else:
                messagebox.showwarning("Error", "Por favor completa todos los campos.")

        tk.Button(self.seccion_actual, text="Guardar", font=("Arial", 12),
                  bg=self.highlight, fg="white", command=guardar).pack(pady=15)

    def mostrar_vacaciones(self):
        self.limpiar_seccion_actual()
        self.seccion_actual = tk.Frame(self.content_frame, bg=self.bg_color)
        self.seccion_actual.pack(fill="both", expand=True)

        tk.Label(self.seccion_actual, text="Asignar Vacaciones", font=("Arial", 16, "bold"), bg=self.bg_color).pack(pady=20)

        if not self.empleados:
            tk.Label(self.seccion_actual, text="No hay empleados registrados.", font=("Arial", 12), bg=self.bg_color).pack()
            return

       
        tk.Label(self.seccion_actual, text="Selecciona empleado:", bg=self.bg_color, font=("Arial", 12)).pack()
        nombres = [emp.nombre for emp in self.empleados]
        seleccionado = tk.StringVar()
        seleccionado.set(nombres[0])
        menu_emp = tk.OptionMenu(self.seccion_actual, seleccionado, *nombres)
        menu_emp.config(font=("Arial", 12))
        menu_emp.pack(pady=5)

     
        tk.Label(self.seccion_actual, text="Selecciona periodo de vacaciones:", bg=self.bg_color, font=("Arial", 12)).pack()
        periodo_var = tk.StringVar()
        if self.periodos_disponibles:
            periodo_var.set(self.periodos_disponibles[0])
        menu_periodo = tk.OptionMenu(self.seccion_actual, periodo_var, *self.periodos_disponibles)
        menu_periodo.config(font=("Arial", 12))
        menu_periodo.pack(pady=5)

        historial_texto = tk.Text(self.seccion_actual, height=10, width=60, font=("Arial", 11))
        historial_texto.pack(pady=10)

        def asignar_vacacion():
            nombre = seleccionado.get()
            periodo = periodo_var.get()

            if periodo not in self.periodos_disponibles:
                messagebox.showerror("Error", "Periodo no disponible.")
                return

            for emp in self.empleados:
                if emp.nombre == nombre:
                    emp.asignar_vacacion(periodo)
                    self.periodos_disponibles.remove(periodo)
                    mostrar_historial()
                    messagebox.showinfo("Éxito", f"{periodo} asignado a {nombre}.")
                    self.mostrar_vacaciones()
                    break

        tk.Button(self.seccion_actual, text="Asignar Vacación", font=("Arial", 12),
                  bg=self.highlight, fg="white", command=asignar_vacacion).pack(pady=10)

        def mostrar_historial():
            historial_texto.delete(1.0, tk.END)
            for emp in self.empleados:
                if emp.vacaciones:
                    historial_texto.insert(tk.END, f"{emp.nombre}:\n")
                    for vac in emp.vacaciones:
                        historial_texto.insert(tk.END, f"  - {vac}\n")
                    historial_texto.insert(tk.END, "\n")

        mostrar_historial()



if __name__ == "__main__":
    root = tk.Tk()
    app = ControlAsistenciaApp(root)
    root.mainloop()