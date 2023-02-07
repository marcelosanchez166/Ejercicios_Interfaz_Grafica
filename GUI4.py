from tkinter import *

raiz = Tk()
raiz.title("Radiobutton")
raiz.geometry("450x720")

varOpcion = IntVar()


def imprimirOpcion():
    if varOpcion.get() == 1:
        etiqueta.config(text="Masculino")
    else:
        etiqueta.config(text="Femenino")


masculino = Radiobutton(raiz, text="Masculino",
                        variable=varOpcion, value=1, command=imprimirOpcion).pack()
femenino = Radiobutton(raiz, text="Femenino", variable=varOpcion,value=2, command=imprimirOpcion).pack()

etiqueta = Label(raiz)  # Una etiqueta no se puede empaquetar de una vez
etiqueta.pack()


##################################################################################################

Futbol = IntVar()
Boxeo = IntVar()
Tenis = IntVar()
Pin_Pon = IntVar()


def opcionesDeportes():
    opcionescogida = ""
    if Futbol.get() == 1:
        opcionescogida += "  Futbol"
    if Boxeo.get() == 1:
        opcionescogida += "  Boxeo"
    if Tenis.get() == 1:
        opcionescogida += "  Tenis"
    if Pin_Pon.get() == 1:
        opcionescogida += "  Pin Pon"

    # Se le pasa al label la opcion escogida
    opciones = Message.config(text=opcionescogida)


Label(raiz, text="Checkbuttons").pack()


# Con la opcion variable=Futbol o cualquier otra opcion se le esta pasando al checkbox la variable con valor entero ya sea cero o uno
# el metodo command se le pasa la funcion al boton en este caso al checkbox
Button1 = Checkbutton(raiz, text="Futbol", variable=Futbol,onvalue=1, offvalue=0, command=opcionesDeportes).pack()
Button2 = Checkbutton(raiz, text="Boxeo", variable=Boxeo,onvalue=1, offvalue=0, command=opcionesDeportes).pack()
Button3 = Checkbutton(raiz, text="Tenis", variable=Tenis,onvalue=1, offvalue=0, command=opcionesDeportes).pack()
Button4 = Checkbutton(raiz, text="Pin Pon", variable=Pin_Pon,onvalue=1, offvalue=0, command=opcionesDeportes).pack()
# La opcion onvalue=1 le dice al checkbox que esta marcada, y la opcion offvalue=0 le dice que no esta seleccionado, y cuando llega al if
# Hace la validacion si el checkbox esta seleccionado

Message = Label(raiz)  # Label para mostrar lo que el usuario ha seleccionado
Message.pack()

raiz.mainloop()
