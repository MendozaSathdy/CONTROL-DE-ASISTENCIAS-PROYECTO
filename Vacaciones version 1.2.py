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
        self.root.title("Vacaciones")
        self.root.geometry("450x400")
        self.root.configure(bg="olive")

        self.empleados = empleados
        self.periodos = self.generar_periodos()

        tk.Label(root, text="Asignar Vacaciones", font=("Arial", 18, "bold"), bg="fuchsia", fg="purple").pack(pady=10)

        self.emp_var = tk.StringVar(value=self.empleados[0].nombre)
        tk.OptionMenu(root, self.emp_var, *[e.nombre for e in empleados]).pack(pady=5)

        self.periodo_var = tk.StringVar(value=self.periodos[0])
        self.periodo_menu = tk.OptionMenu(root, self.periodo_var, *self.periodos)
        self.periodo_menu.pack(pady=5)

        tk.Button(root, text="Asignar", font=("Arial", 12), bg="yellow", fg="white", command=self.asignar).pack(pady=10)

        tk.Label(root, text="Vacaciones Asignadas:", font=("Arial", 14), bg="white", fg="blue").pack(pady=5)
        self.lista_vacaciones = tk.Listbox(root, width=50, height=10)
        self.lista_vacaciones.pack(pady=5)

    def generar_periodos(self):
        meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
                 "Jul", "Ag", "Sep", "Oct", "Nov", "Dic"]
        return [f"{mes} 01 - {mes} 15" for mes in meses] + [f"{mes} 16 - {mes} 30" for mes in meses]

    def actualizar_menu_periodos(self):
        self.periodo_menu['menu'].delete(0, 'end')
        for periodo in self.periodos:
            self.periodo_menu['menu'].add_command(label=periodo, command=lambda p=periodo: self.periodo_var.set(p))
        if self.periodos:
            self.periodo_var.set(self.periodos[0])
        else:
            self.periodo_var.set("")

    def asignar(self):
        nombre = self.emp_var.get()
        periodo = self.periodo_var.get()

        if not periodo:
            messagebox.showwarning("Vacío", "No hay más periodos disponibles.")
            return

        for emp in self.empleados:
            if emp.nombre == nombre:
                emp.asignar_vacacion(periodo)
                self.lista_vacaciones.insert(tk.END, f"{nombre} - {periodo}")
                messagebox.showinfo("Asignado", f"{periodo} asignado a {nombre}")
                if periodo in self.periodos:
                    self.periodos.remove(periodo)
                    self.actualizar_menu_periodos()
                break

if __name__ == "__main__":
    root = tk.Tk()
    empleados = [Empleado("Sathdy"), Empleado("Juan")]
    app = VacacionesApp(root, empleados)
    root.mainloop()