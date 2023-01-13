from tkinter import *

raiz=Tk()

raiz.title("Botones y widgets de texto amplio")
raiz.geometry("720x720")

minombre=StringVar()#Especifica que se trata de una cadena de caracteres y se pasa al entry del nombre en este caso

minombre2=StringVar()

nombrelabel=Label( text="Nombre" )
nombrelabel.grid(row=0,column=0,sticky="w", pady=4, padx=4)

Passlabel=Label( text="Contraseña" )
Passlabel.grid(row=1,column=0,sticky="w", pady=4, padx=4)

apellidolabel=Label( text="Apellido" )
apellidolabel.grid(row=2,column=0,sticky="w", pady=4, padx=4)

Direccionlabel=Label( text="Direccion" )
Direccionlabel.grid(row=3,column=0,sticky="w",pady=4, padx=4 )

"""Label o etiqueta para el cuadro de texto amplio"""
comentariolable=Label(raiz, text="Comentario: ")
comentariolable.grid(row=4,column=0, pady=4, padx=4)

#Cuadros de texto
textoNombre=Entry(raiz, textvariable=minombre)#Con textvariable consigo que el cuadro este asociado al valor de la variable
textoNombre.grid(row=0,column=1 )

textopass=Entry(raiz)
textopass.grid(row=1,column=1 )
textopass.config(show="#")#Metodo para que no se muestre la password

textoApellido=Entry(raiz)
textoApellido.grid(row=2,column=1)

textoDireccion=Entry(raiz)
textoDireccion.grid(row=3,column=1)


"""Cuadro de texto amplio"""
comentarioText=Text(raiz,width=15, height=5 )
comentarioText.grid(row=4,column=1, pady=4, padx=4)


"""Barra de scroll para cuadros de texto amplio"""
barradescroll=Scrollbar(raiz, command=comentarioText.yview)#Crear la barra de scroll
barradescroll.grid(row=4,column=2, sticky="nsew")#posicion y hacer que se mueva la barra con los botones
comentarioText.config( yscrollcommand=barradescroll.set )#Hace que se posicione la barra dependiendo donde se encuentre el cursor


"""Funcion para pasar datos """
def obtenernombre():
          minombre2.get()
lista=[]
lista.append(minombre2)

print(lista)




"""Funcion para mostrar datos en el campo texto"""
def boton1():
          minombre.set("marcelo")#setea la variable y la pasa al cuadro nombre



"""Botones"""
botonenviar=Button(raiz,width=5, height=1, text="Mostrar", command=boton1)#crea un boton con texto dentro y se le pasa la funcion boton1
botonenviar.grid(row=5,column=3)#le da orientacion 


botonobtener=Button(raiz,width=5, height=1, text="Enviar",command=obtenernombre)
botonobtener.grid(column=4)

raiz.mainloop()