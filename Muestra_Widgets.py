#Juan de Jesus Tovar Reyes 09/03/2023
from tkinter import *
from tkinter import ttk

raiz = Tk()

raiz.title("Muestra de Widgets")

frame = ttk.Frame(raiz, padding="40 40 40 40", relief="raised")
frame.grid(column=0, row=0)
frame2 = ttk.Frame(frame, padding="15 15", relief="raised")
frame2.grid(column=0, row=0)
frame3 = ttk.Frame(frame, padding="15 15", relief="raised")
frame3.grid(column=0, row= 2, pady=30)
frame4 = ttk.Frame(frame, padding="15 15")
frame4.grid(column=1, row= 0)
frame5 = ttk.Frame(frame, padding="15 15")
frame5.grid(column=0,row=3)

ttk.Label(frame2, text="Nombre: ").grid(column=0, row=1, sticky=W)
ttk.Label(frame2, text="").grid(column= 0, row= 2, columnspan=2)
ttk.Label(frame2, text="").grid(column= 1, row= 2, columnspan=2)
ttk.Label(frame2, text="A. Paterno: ").grid(column=0, row=3, sticky=W)
ttk.Label(frame2, text="").grid(column= 0, row= 4, columnspan=2)
ttk.Label(frame2, text="").grid(column= 1, row= 4, columnspan=2)
ttk.Label(frame2, text="A. Materno: ").grid(column=0, row=5, sticky=W)
ttk.Label(frame2, text="").grid(column= 0, row= 6, columnspan=2)
ttk.Label(frame2, text="").grid(column= 1, row= 6, columnspan=2)
ttk.Label(frame2, text="Correo: ").grid(column=0, row=7, sticky=W)
ttk.Label(frame2, text="").grid(column= 0, row= 8, columnspan=2)
ttk.Label(frame2, text="").grid(column= 1, row= 8, columnspan=2)
ttk.Label(frame2, text="Movil: ").grid(column=0, row=9, sticky=W)

Nombre = StringVar()
A_Paterno = StringVar()
A_Materno = StringVar()
Correo = StringVar()
Movil = StringVar()

NombreEntry= ttk.Entry(frame2, width=30, textvariable=Nombre)
NombreEntry.grid( column= 1 , row= 1, columnspan=2)
A_PaternoEntry= ttk.Entry(frame2, width=30, textvariable=A_Paterno)
A_PaternoEntry.grid( column= 1 , row= 3, columnspan=2)
A_MaternoEntry= ttk.Entry(frame2, width=30, textvariable=A_Materno)
A_MaternoEntry.grid( column= 1 , row= 5, columnspan=2)
CorreoEntry= ttk.Entry(frame2, width=30, textvariable=Correo)
CorreoEntry.grid( column= 1 , row= 7, columnspan=2)
MovilEntry= ttk.Entry(frame2, width=30, textvariable=Movil)
MovilEntry.grid( column= 1 , row= 9, columnspan=2)

ttk.Label(frame3, text="Aficiones:").grid(column=1, row=0,sticky=W)
chkBoton = ttk.Checkbutton(frame3, text="Leer")
chkBoton.grid(column=1,row=1)
ttk.Label(frame3, text="    ").grid(column= 2, row= 1)
chkBoton = ttk.Checkbutton(frame3, text="Musica")
chkBoton.grid(column=3,row=1)
ttk.Label(frame3, text="    ").grid(column= 4, row= 1)
chkBoton = ttk.Checkbutton(frame3, text="Videojuegos")
chkBoton.grid(column=5,row=1)

Estado = StringVar()
Estudiante = ttk.Radiobutton(frame4,text='Estudiante',variable=Estado,value=Estado, compound="center").grid(column=0, row=1, sticky=W)
Empleado = ttk.Radiobutton(frame4,text='Empleado',variable=Estado,value=Estado,compound="center").grid(column=0, row=2, sticky=W)
Desempleado = ttk.Radiobutton(frame4,text='Desempleado',variable=Estado,value=Estado,compound="center").grid(column=0, row=3, sticky=W)

Estado = StringVar()

comboEstados = ttk.Combobox(frame, textvariable=Estado)
comboEstados.grid(column= 1, row=2)
comboEstados['values']=("Jalisco","Zacatecas","Colima","Tlaxcala")

button = ttk.Button(frame5, text="Guardar")
button.grid(column=0,row=0)
ttk.Label(frame5, text="                    ").grid(column= 1, row= 0)
button2 = ttk.Button(frame5, text="Cancelar")
button2.grid(column=2,row=0)

raiz.mainloop()