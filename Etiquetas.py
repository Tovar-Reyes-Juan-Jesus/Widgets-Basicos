#Receta
from tkinter import *
from tkinter import ttk

raiz = Tk()
etqTexto = ttk.Label(raiz, text="Etqueta solo texto")
etqTexto.grid()

imagen = PhotoImage(file="pacman.PNG")  #creamos un objeto de tipo imagen.

etqImagen = ttk.Label(raiz)
etqImagen.grid()
etqImagen['image'] = imagen #image es como la propiedad para asignar la imagen a la etiqueta. sin necesidad del constructor. 

etqCombinada = ttk.Label(raiz, text="Naci de una pizza :3", compound="right") #compound es una propiedad donde la etiqueta es una compuesta donde se alinee donde se va a ubicar la etiqueta. 
etqCombinada.grid()
etqCombinada['image'] = imagen #Se asigna la imagen a la etiqueta

raiz.mainloop()# siempre se pone al final, donde lo que este arriba del loop se mostrara en la ventana o se ejecutara.