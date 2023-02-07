from tkinter import *

raiz = Tk()
raiz.title("Calculadora")


miframe = Frame()

miframe.pack()
miframe.config(background="gold")

operacion = ""
resultado = 0
resetear_pantalla = False
num1 = 0
# -------------------Pantalla---------------------------

numpantalla = StringVar()


pantalla = Entry(miframe, textvariable=numpantalla)
pantalla.grid(row=0, column=0, padx=4, pady=4, columnspan=4)
pantalla.config(background="gray", fg="#ffd700", justify="center")

# ------------Fila 1 de Botones-------------------------
boton7 = Button(miframe, text="7", width=4, pady=8,
                command=lambda: pulsarnum("7"))
boton7.grid(row=1, column=0)
boton8 = Button(miframe, text="8", width=4, pady=8,
                command=lambda: pulsarnum("8"))
boton8.grid(row=1, column=1)
boton9 = Button(miframe, text="9", width=4, pady=8,
                command=lambda: pulsarnum("9"))
boton9.grid(row=1, column=2)
botonDiv = Button(miframe, text="/", width=4, pady=8,command=lambda: divide(numpantalla.get()))
botonDiv.grid(row=1, column=3)

# ------------Fila 2 de Botones-------------------------
boton4 = Button(miframe, text="4", width=4, pady=8,
                command=lambda: pulsarnum("4"))
boton4.grid(row=2, column=0)
boton5 = Button(miframe, text="5", width=4, pady=8,
                command=lambda: pulsarnum("5"))
boton5.grid(row=2, column=1)
boton6 = Button(miframe, text="6", width=4, pady=8,
                command=lambda: pulsarnum("6"))
boton6.grid(row=2, column=2)
botonMulti = Button(miframe, text="X", width=4, pady=8,
                    command=lambda: multi(numpantalla.get()))
botonMulti.grid(row=2, column=3)


# ------------Fila 3 de Botones-------------------------
boton1 = Button(miframe, text="1", width=4, pady=8,
                command=lambda: pulsarnum("1"))
boton1.grid(row=3, column=0)
boton2 = Button(miframe, text="2", width=4, pady=8,
                command=lambda: pulsarnum("2"))
boton2.grid(row=3, column=1)
boton3 = Button(miframe, text="3", width=4, pady=8,
                command=lambda: pulsarnum("3"))
boton3.grid(row=3, column=2)
botonRest = Button(miframe, text="-", width=4, pady=8,command=lambda: resta(numpantalla.get()))
botonRest.grid(row=3, column=3)

# ------------Fila 4 de Botones-------------------------
boton0 = Button(miframe, text="0", width=4, pady=8,
                command=lambda: pulsarnum("0"))
boton0.grid(row=4, column=0)
botonpunto = Button(miframe, text=".", width=4, pady=8,
                    command=lambda: pulsarnum("."))
botonpunto.grid(row=4, column=1)
botonporcentaje = Button(miframe, text="%", width=4,pady=8, command=lambda: pulsarnum("%"))
botonporcentaje.grid(row=4, column=2)
botonsuma = Button(miframe, text="+", width=4, pady=8,command=lambda: suma(numpantalla.get()))
botonsuma.grid(row=4, column=3)


# ------------Fila 5 de Botones-------------------------
botoncoma = Button(miframe, text=",", width=4, pady=8,command=lambda: pulsarnum(","))
botoncoma.grid(row=5, column=0)
botonpotencia = Button(miframe, text="χ²", width=4,pady=8, command=lambda: pulsarnum("^"))
botonpotencia.grid(row=5, column=1)
botondelete = Button(miframe, text="AC", width=4,pady=8, command=lambda: Borrar())
botondelete.grid(row=5, column=2)
botonigual = Button(miframe, text="=", width=4, pady=8,
                    command=lambda: el_resultado())
botonigual.grid(row=5, column=3)


# -------------------------------Funcion Borrar -------------------------------------

def Borrar():
    pantalla.delete(0, END)


# ---------------------Pulsaciones de teclado--------------------------------------
"""Funcion para mostrar datos en el campo texto"""


def pulsarnum(numero):
    global operacion
    global resetear_pantalla
    if resetear_pantalla != False:
        numpantalla.set(numero)
        resetear_pantalla = False
    else:
        # setea la variable y la pasa al cuadro numpantalla y concatena el numero
        numpantalla.set(numpantalla.get()+numero)

# --------------------------------Funciones de operaciones suma resta, Multiplicar y dividir-------------------------


def suma(numero):
    global operacion
    global resultado
    global resetear_pantalla

    resultado += float(numero)
    operacion = "suma"
    resetear_pantalla = True
    numpantalla.set(resultado)


# ----------------------Funcion Resta-------------------------

contador_resta = 0


def resta(numero):
    global operacion
    global resultado
    global num1
    global contador_resta
    global resetear_pantalla

    if contador_resta == 0:
        num1 = int(numero)
        resultado = num1
    else:
        if contador_resta == 1:
            resultado = num1-int(numero)
        else:
            resultado = float(numero)-float(resultado)
        numpantalla.set(resultado)
        resultado = numpantalla.get()
    contador_resta = contador_resta+1
    operacion = "resta"
    resetear_pantalla = True


# ------------------Funcion Multiplicar----------------------------
contador_multi = 0


def multi(numero):
    global operacion
    global resultado
    global num1
    global contador_multi
    global resetear_pantalla

    if contador_multi == 0:
        num1 = int(numero)
        resultado = num1
    else:
        if contador_multi == 1:
            resultado = num1*int(numero)
        else:
            resultado = int(resultado)*int(numero)
        numpantalla.set(resultado)
        resultado = numpantalla.get()
    contador_multi = contador_multi+1
    operacion = "multiplicacion"
    resetear_pantalla = True


# ------------------------Funcion Dividir-------------------------
contador_divi = 0


def divide(num):
    global operacion
    global resultado
    global num1
    global contador_divi
    global resetear_pantalla

    if contador_divi == 0:
        num1 = float(num)
        resultado = num1
    else:
        if contador_divi == 1:
            resultado = num1/float(num)
        else:
            resultado = float(resultado)/float(num)
        numpantalla.set(resultado)
        resultado = numpantalla.get()
    contador_divi = contador_divi+1
    operacion = "division"
    resetear_pantalla = True


# --------------------------El resultado con boton de igual (=) ----------------------------
def el_resultado():
    global resultado
    global operacion
    global contador_resta
    global contador_multi
    global contador_divi

    if operacion == "suma":
        numpantalla.set(resultado+int(numpantalla.get()))
        resultado = 0
    elif operacion == "resta":
        numpantalla.set(int(resultado)-int(numpantalla.get()))
        resultado = 0
        contador_resta = 0
    elif operacion == "multiplicacion":
        numpantalla.set(int(resultado)*int(numpantalla.get()))
        resultado = 0
        contador_multi = 0
    elif operacion == "division":
        numpantalla.set(int(resultado)/int(numpantalla.get()))
        resultado = 0
        contador_divi = 0


"""Con la funcion (eval) ya no habria necesidad de hacer cada funcion de suma resta etc, esa funcion le dice a python que evalue
el string que se esta pasando
Ej: 
ecuacion="9+2*3" 
resultado=eval(ecuacion)
print(resultado)
"""


raiz.mainloop()
