import tkinter as tk
from tkinter import messagebox

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vacaciones = []

    def asignar_vacacion(self, periodo):
        self.vacaciones.append(periodo)

class VacacionesApp:
    def __init__(self, root, empleados):
        self.root = root
        self.empleados = empleados
        self.periodos = self.generar_periodos()

        tk.Label(root, text="Vacaciones", font=("Arial", 16)).pack(pady=10)

        self.emp_var = tk.StringVar(value=self.empleados[0].nombre)
        tk.OptionMenu(root, self.emp_var, *[e.nombre for e in empleados]).pack(pady=5)

        self.periodo_var = tk.StringVar(value=self.periodos[0])
        tk.OptionMenu(root, self.periodo_var, *self.periodos).pack(pady=5)

        tk.Button(root, text="Asignar", command=self.asignar).pack(pady=10)

    def generar_periodos(self):
        meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
                 "Jul", "Ag", "Sep", "Oct", "Nov", "Dic"]
        return [f"{mes} 01 - {mes} 15" for mes in meses] + [f"{mes} 16 - {mes} 30" for mes in meses]

    def asignar(self):
        nombre = self.emp_var.get()
        periodo = self.periodo_var.get()
        for emp in self.empleados:
            if emp.nombre == nombre:
                emp.asignar_vacacion(periodo)
                messagebox.showinfo("Asignado", f"{periodo} asignado a {nombre}")
                self.periodos.remove(periodo)
                break

if __name__ == "__main__":
    root = tk.Tk()
    empleados = [Empleado("sathdy"), Empleado("juan")]
    app = VacacionesApp(root, empleados)
    root.mainloop()