#importacion de librerias
import tkinter as tk
from tkinter import messagebox
from matplotlib_venn import venn2, venn2_circles
import matplotlib.pyplot as plt
from sympy import FiniteSet


#funcion para hallar la union de 2 conjuntos
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

#metodo que calcula el complemento de cada conjunto
def complemento( conjunto_a, conjunto_b):
    mensaje = "El complemento de A es: " + str(conjunto_b) + " y el complemento de B es: " + str(conjunto_a)
    return mensaje

#metodo que calcula la combinacion de cada conjunto
def combinacion( conjunto_a, conjunto_b):
    combinacion = []
    for i in conjunto_a:
        for j in conjunto_b:
            combinacion.append((i,j))
    return combinacion


#metodo que calcula la interseccion entre conjuntos
def interseccion( conjunto_a, set_b):
    interseccion = []
    for elmnt in conjunto_a:
        if elmnt in set_b:
            interseccion.append(elmnt)

    return interseccion

#metodos que halla todos los posibles subconjuntos de cada conjunto
def subconjunto( conjunto_a, conjunto_b ):
    subconjuntos_a = subconjuntos(conjunto_a)
    subconjuntos_b = subconjuntos(conjunto_b)
    return "Los subconjuntos de A son: " + str(subconjuntos_a) + " y los subconjuntos de B son: " + str(subconjuntos_b)

#metodo que halla los subconjuntos de un conjunto determinado
def subconjuntos(conjunto):
    if len(conjunto) == 0:
        return [[]]
    sub = subconjuntos(conjunto[:-1])
    return sub + [s + [conjunto[-1]] for s in sub]   


#determina si dos conjuntos son disjuntos
def disjuntos( conjunto_a, conjunto2):
        for i in conjunto_a:
            for j in conjunto2:
                if i==j:
                    return "Los conjuntos no son disjuntos"
        return "Los conjuntos son disjuntos"

#halla la diferencia entre conjuntos
def diferencia( conjunto_a, conjunto_b ):
    diferencia = []
    for i in conjunto_a:
        diferencia.append(i) 
        for j in conjunto_b[:-1]:
            if i == j:
                diferencia.pop()
                break

    return diferencia

#halla la cardinalidad ( tamaño ) de un conjunto
def cardinalidad( conjunto_a, conjunto_b):
    return "La cardinalidad del conjunto A es: " + str(len(conjunto_a)) + " y la cardinalidad del conjunto B es: " + str(len(conjunto_b)) 


#crea el digrama de venn
def dibujar_venn(conjunto_a, conjunto_b):
    #agregar los conjuntos a un objeto de tipo FiniteSet

    A = FiniteSet(*conjunto_a)
    B = FiniteSet(*conjunto_b)


    plt.figure(figsize=(6, 8))
    v = venn2(subsets=[A, B], set_labels=('A', 'B'))
    v.get_label_by_id('10').set_text(A - B)
    try:
        v.get_label_by_id('11').set_text( A.intersection(B) )
    except:
        pass
    v.get_label_by_id('01').set_text(B - A)
    c = venn2_circles(subsets=[A, B], linestyle='dashed')
    c[0].set_ls('solid')
    plt.show()

#clase utilizada para inicializar la aplicacion
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
        opciones_operaciones = ["Unión", "Intersección", "Diferencia A-B", "Diferencia B-A", "subconjuntos", "disjuntos", "cardinalidad", "complemento", "combinacion" ,"Ver como diagrama de venn"]
        self.operacion_var = tk.StringVar(root)
        self.operacion_var.set(opciones_operaciones[0])  # Configurar la opción predeterminada
        self.menu_operacion = tk.OptionMenu(root, self.operacion_var, *opciones_operaciones)
        self.menu_operacion.grid(row=2, column=0, columnspan=2, pady=10)

        # Botón para realizar la operación
        self.btn_calcular = tk.Button(root, text="Calcular", command=self.realizar_operacion)
        self.btn_calcular.grid(row=3, column=0, columnspan=2, pady=10)

    
    #procesa los conjuntos ingresados
    def obtener_conjuntos_ingresados(self):
        try:
            conjunto_a = list(map(int, self.entry_conjunto_a.get().split(',') ))
            conjunto_b = list(map(int, self.entry_conjunto_b.get().split(',') ))
            return conjunto_a, conjunto_b
        except ValueError:
            messagebox.showerror("Error", "Ingrese conjuntos válidos (números separados por comas)")
            return None, None


    #realiza la operacion especificada por el usuario, descritas en los
    #bloques if else
    def realizar_operacion(self):
        conjunto_a, conjunto_b = self.obtener_conjuntos_ingresados()

        resultado = None
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
            elif operacion == "subconjuntos":
                resultado = subconjunto(conjunto_a, conjunto_b)
            elif operacion == "disjuntos":
                resultado = disjuntos(conjunto_a, conjunto_b)
            elif operacion == "cardinalidad":
                resultado = cardinalidad(conjunto_a, conjunto_b)
            elif operacion == "complemento":
                resultado = complemento(conjunto_a, conjunto_b)
            elif operacion == "combinacion":
                resultado = combinacion(conjunto_a, conjunto_b)
            elif operacion == "Ver como diagrama de venn":
                dibujar_venn(conjunto_a, conjunto_b)

            if resultado != None:
                messagebox.showinfo("Resultado", f"Resultado de {operacion}: {resultado}")


#punto de entrada de la app
if __name__ == "__main__":
    root = tk.Tk()
    app = ConjuntosApp(root)
    root.mainloop()



