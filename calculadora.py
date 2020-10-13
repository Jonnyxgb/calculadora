from tkinter import *

raiz=Tk()

miframe=Frame(raiz)
miframe.pack()

operacion=""

resultado=0

#-----------------pantalla------------------

numeropantalla=StringVar()

pantalla=Entry(miframe, textvariable=numeropantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="black", fg="red",justify="right")

#----------------pulsar teclado--------------------

def numeropulsado(num):

	global operacion

	if operacion!="":

		numeropantalla.set(num)

		operacion=""

	else:

		numeropantalla.set(numeropantalla.get() + num)



#-------------------funcion suma---------------

def suma(num):

	global operacion

	global resultado

	resultado+=int(num)

	operacion="suma"

	numeropantalla.set(resultado)

#-------------------funcion resultado---------------

def el_resultado():

	global resultado

	numeropantalla.set(resultado+int(numeropantalla.get))

	resultado=0



#----------------fila 1-------------------------

boton7=Button(miframe, text="7", width=3, command=lambda:numeropulsado("7"))
boton7.grid(row=2, column=0)
boton8=Button(miframe, text="8", width=3, command=lambda:numeropulsado("8"))
boton8.grid(row=2, column=1)
boton9=Button(miframe, text="9", width=3, command=lambda:numeropulsado("9"))
boton9.grid(row=2, column=2)
botonD=Button(miframe, text="/", width=3)
botonD.grid(row=2, column=3)

#----------------fila 2-------------------------

boton4=Button(miframe, text="4", width=3, command=lambda:numeropulsado("4"))
boton4.grid(row=3, column=0)
boton5=Button(miframe, text="5", width=3, command=lambda:numeropulsado("5"))
boton5.grid(row=3, column=1)
boton6=Button(miframe, text="6", width=3, command=lambda:numeropulsado("6"))
boton6.grid(row=3, column=2)
botonx=Button(miframe, text="x", width=3)
botonx.grid(row=3, column=3)

#----------------fila 3-------------------------

boton1=Button(miframe, text="1", width=3, command=lambda:numeropulsado("1"))
boton1.grid(row=4, column=0)
boton2=Button(miframe, text="2", width=3, command=lambda:numeropulsado("2"))
boton2.grid(row=4, column=1)
boton3=Button(miframe, text="3", width=3, command=lambda:numeropulsado("3"))
boton3.grid(row=4, column=2)
botonR=Button(miframe, text="-", width=3)
botonR.grid(row=4, column=3)

#----------------fila 4-------------------------

boton0=Button(miframe, text="0", width=3, command=lambda:numeropulsado("0"))
boton0.grid(row=5, column=0)
botonC=Button(miframe, text=",", width=3)
botonC.grid(row=5, column=1)
botonI=Button(miframe, text="=", width=3, command=lambda:el_resultado())
botonI.grid(row=5, column=2)
botonM=Button(miframe, text="+", width=3, command=lambda:suma(numeropantalla.get()))
botonM.grid(row=5, column=3)


raiz.mainloop()