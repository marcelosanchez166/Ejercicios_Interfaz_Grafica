from tkinter import *
from tkinter import font

"""TKinter solo acepta formatos de imagenes png y gif"""

raiz=Tk()
raiz.title("Primera Ventana") #Cambiar el nombre de la ventana 
#raiz.geometry("520x480") #Configurar tamaño, esta opcion se desactiva para cuando se meta un frame en la raiz y tomara la dimencion 
# del frame 
#raiz.iconbitmap("piton.ico") #Cambiar el icono 
raiz.config(bg="blue") #Cambiar color de fondo
#raiz.resizable(0,0)#Recibe dos parametros tipo bolean(cero=False ó uno=True), el primero es el ancho y el segundo el alto, 
# si se declaran en cero no se puede redimencionar en ninguna direccion 
raiz.config(bd=10)#Le pone un tamaño al borde de la raiz
raiz.config(relief="groove")#raised,sunken,groove,ridge,flat:Tipo de marco para la raiz
raiz.config(cursor="hand2")#Tipo de cursor

"""Frame que estara dentro de la raiz"""
Frame1=Frame()#Creo el frame que va dentro de la raiz para organizar los widgets
Frame1.pack()#Empaqueta el frame en la raiz
Frame1.config(bg="red")#color del frame
Frame1.config(width="520", height="480")#Tamaño del fram, para que este surja efecto el de la raiz debe estar desactivado
Frame1.config(bd=10)#tamaño al borde del frame
Frame1.config(relief="raised")#tipo de marco para el frame

"""Labels, opciones para las labels: Text=mostrar texto, Anchor=ancho, bg=color fondo,bd=grosor del borde, font=fuente letra,
fg=color de la fuente, widht=ancho del label en caracteres, height=alto del label en caracteres, image=muestra imagen en el label
justify=orientacion del texto"""
label1=Label(Frame1,text="Hola como estas",fg="black",font=15)
#label1.place(x=200,y=200)
label1.grid(row=0, column=0)#mejor forma para hacer uso de labels y cuadros de texto
#label1.pack()#Con esto muestra el lable, pero al empaquetarlo redimenciona el frame1, por lo que es mejor usar el metodo place
#tambien puedo hacer esto con las label solo si no voy a ocupar la label mas adelante
#Label(Frame1,text="Hola como estas").place(x=200,y=200)

"""Usar imagenes en los labels"""
Imagen=PhotoImage(file="piton.png")
label2=Label(raiz,image=Imagen).place(x=100,y=50)


"""Cuadros de texto para capturar texto"""
text1=Entry(Frame1)#En estos casos no funciona de mucho el metodo place dado que daria problemas al poner label y cuadros de texto seguidos
# o algun otro tipo de widget, por lo que es mejor usar el metodo grid
text1.grid(row=0,column=2)


raiz.mainloop() 