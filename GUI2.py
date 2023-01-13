from tkinter import *

raiz=Tk()
raiz.title(" Labels y Cuadros de texto ")
raiz.geometry("520x480")


nombrelabel=Label( text="Nombre" )
nombrelabel.grid(row=0,column=0,sticky="w", pady=4, padx=4)

Passlabel=Label( text="Contraseña" )
Passlabel.grid(row=1,column=0,sticky="w", pady=4, padx=4)

apellidolabel=Label( text="Apellido" )
apellidolabel.grid(row=2,column=0,sticky="w", pady=4, padx=4)

Direccionlabel=Label( text="Direccion" )
Direccionlabel.grid(row=3,column=0,sticky="w",pady=4, padx=4 )

#Cuadros de texto
textoNombre=Entry(raiz)
textoNombre.grid(row=0,column=1 )

textopass=Entry(raiz)
textopass.grid(row=1,column=1 )
textopass.config(show="*")#Metodo para que no se muestre la password

textoApellido=Entry(raiz)
textoApellido.grid(row=2,column=1)

textoDireccion=Entry(raiz)
textoDireccion.grid(row=3,column=1)

"""Metodo stiky permite alinear el texto de los labels donde quiera, n=norte, s=sur, e=este, w=oeste y se coloca en el grid"""


raiz.mainloop() 


