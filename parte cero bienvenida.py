import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Control de Asistencia")

        #fondo principal de color gris y la creacion del marco 
        self.content_frame = tk.Frame(self.root, bg="grey")
        self.content_frame.pack(side="right", expand=True, fill="both")

        
        self.mostrar_inicio()

    def mostrar_inicio(self):
        tk.Label(self.content_frame, text="Bienvenido al Control de Asistencias de un Hospital", font=("Arial", 24, "bold"), bg="grey").pack(pady=100)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()