import tkinter as tk

from tkinter import messagebox




def union( conjunto_a, set_b):
    union = []
    for elmnt in conjunto_a:
        union.append(elmnt)
        for union_elmnt in union[:-1]:
            if union_elmnt == elmnt:
                union.pop()
                break

    for elmnt in set_b: 
        union.append(elmnt)
        for union_elmnt in union[:-1]:
            if union_elmnt == elmnt:
                union.pop()
                break

    return union


def interseccion( conjunto_a, set_b):
    interseccion = []
    for elmnt in conjunto_a:
        if elmnt in set_b:
            interseccion.append(elmnt)

    return interseccion


def subconjuntos( conjunto):
    if len(conjunto) == 0:
        return [[]]
    sub = subconjuntos(conjunto[:-1])
    return sub + [s + [conjunto[-1]] for s in sub]



def disjuntos( conjunto_a, conjunto2):
        for i in conjunto_a:
            for j in conjunto2:
                if i==j:
                    return False
        return True

def diferencia( conjunto_a, conjunto_b ):
    diferencia = []
    for i in conjunto_a:
        diferencia.append(i) 
        for j in conjunto_b[:-1]:
            if i == j:
                diferencia.pop()
                break

    return diferencia

class ConjuntosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Operaciones de Conjuntos")

        # Variables para almacenar los conjuntos
        self.conjunto_a = []
        self.conjunto_b = []

        # Etiqueta y entrada para el primer conjunto
        self.label_conjunto_a = tk.Label(root, text="Conjunto A:")
        self.entry_conjunto_a = tk.Entry(root)
        self.label_conjunto_a.grid(row=0, column=0, padx=5, pady=5)
        self.entry_conjunto_a.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y entrada para el segundo conjunto
        self.label_conjunto_b = tk.Label(root, text="Conjunto B:")
        self.entry_conjunto_b = tk.Entry(root)
        self.label_conjunto_b.grid(row=1, column=0, padx=5, pady=5)
        self.entry_conjunto_b.grid(row=1, column=1, padx=5, pady=5)

        # Menú desplegable para seleccionar la operación
        opciones_operaciones = ["Unión", "Intersección", "Diferencia A-B", "Diferencia B-A"]
        self.operacion_var = tk.StringVar(root)
        self.operacion_var.set(opciones_operaciones[0])  # Configurar la opción predeterminada
        self.menu_operacion = tk.OptionMenu(root, self.operacion_var, *opciones_operaciones)
        self.menu_operacion.grid(row=2, column=0, columnspan=2, pady=10)

        # Botón para realizar la operación
        self.btn_calcular = tk.Button(root, text="Calcular", command=self.realizar_operacion)
        self.btn_calcular.grid(row=3, column=0, columnspan=2, pady=10)

    
    def obtener_conjuntos_ingresados(self):
        try:
            conjunto_a = list(map(int, self.entry_conjunto_a.get().split(',') ))
            conjunto_b = list(map(int, self.entry_conjunto_b.get().split(',') ))
            return conjunto_a, conjunto_b
        except ValueError:
            messagebox.showerror("Error", "Ingrese conjuntos válidos (números separados por comas)")
            return None, None

    def realizar_operacion(self):
        conjunto_a, conjunto_b = self.obtener_conjuntos_ingresados()

        if conjunto_a is not None and conjunto_b is not None:
            operacion = self.operacion_var.get()

            if operacion == "Unión":
                resultado = union( conjunto_a, conjunto_b)
            elif operacion == "Intersección":
                resultado = interseccion( conjunto_a, conjunto_b)
            elif operacion == "Diferencia A-B":
                resultado = diferencia( conjunto_a, conjunto_b)
            elif operacion == "Diferencia B-A":
                resultado = diferencia(conjunto_a, conjunto_b)

            messagebox.showinfo("Resultado", f"Resultado de {operacion}: {resultado}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConjuntosApp(root)
    root.mainloop()



