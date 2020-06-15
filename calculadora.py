from tkinter import *

raiz=Tk()
raiz.title("Calculadora")

miFrame=Frame(raiz)
miFrame.pack()


#-------------------------------------------  visor

varVisor = StringVar()
visor = Entry(miFrame, textvariable=varVisor)
visor.grid(row="0", column="0", columnspan="4")
visor.config(bg="gray", fg="white", justify="right")

#-------------------------------------------- botones

#-------------------------------------------- Funcion Botones
borrar = False

def codigoBoton1():
    global borrar
    if borrar == True:
        varVisor.set("1")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "1")
    
def codigoBoton2():
    global borrar
    if borrar == True:
        varVisor.set("2")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "2")
    
def codigoBoton3():
    global borrar
    if borrar == True:
        varVisor.set("3")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "3")
    
def codigoBoton4():
    global borrar
    if borrar == True:
        varVisor.set("4")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "4")
    
def codigoBoton5():
    global borrar
    if borrar == True:
        varVisor.set("5")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "5")
    
def codigoBoton6():
    global borrar
    if borrar == True:
        varVisor.set("6")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "6")
    
def codigoBoton7():
    global borrar
    if borrar == True:
        varVisor.set("7")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "7")
    
def codigoBoton8():
    global borrar
    if borrar == True:
        varVisor.set("8")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "8")
    
def codigoBoton9():
    global borrar
    if borrar == True:
        varVisor.set("9")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "9")
    
def codigoBoton0():
    global borrar
    if borrar == True:
        varVisor.set("0")
        borra = False
    else:
        varVisor.set(varVisor.get() + "0")
    
def codigoBotonDiv():
    varVisor.set(varVisor.get() + "/")
    
def codigoBotonMult():
    varVisor.set(varVisor.get() + "*")
    
def codigoBotonRest():
    varVisor.set(varVisor.get() + "-")
    
def codigoBotonSum():
    varVisor.set(varVisor.get() + "+")
    
def codigoBotonPunto():
    varVisor.set(varVisor.get() + ".")

def codigoBotonIgual():
    global borrar
    try:
        varVisor.set(eval(varVisor.get()))
    except ZeroDivisionError:
        varVisor.set("Error div zero")
    finally:
        borrar = True



#--------------- Row 1   ---------------------

boton7 = Button(miFrame, text="7", command=codigoBoton7, width="4")
boton7.grid(row=1, column=0)

boton8 = Button(miFrame, text="8", command=codigoBoton8, width="4")
boton8.grid(row=1, column=1)

boton9 = Button(miFrame, text="9", command=codigoBoton9, width="4")
boton9.grid(row=1, column=2)

botonDiv = Button(miFrame, text="/", command=codigoBotonDiv, width="4")
botonDiv.grid(row=1, column=3)


#--------------- Row 2   ---------------------

boton4 = Button(miFrame, text="4", command=codigoBoton4, width="4")
boton4.grid(row=2, column=0)

boton5 = Button(miFrame, text="5", command=codigoBoton5, width="4")
boton5.grid(row=2, column=1)

boton6 = Button(miFrame, text="6", command=codigoBoton6, width="4")
boton6.grid(row=2, column=2)

botonMult = Button(miFrame, text="*", command=codigoBotonMult, width="4")
botonMult.grid(row=2, column=3)

#--------------- Row 3   ---------------------

boton1 = Button(miFrame, text="1", command=codigoBoton1, width="4")
boton1.grid(row=3, column=0)

boton2 = Button(miFrame, text="2", command=codigoBoton2, width="4")
boton2.grid(row=3, column=1)

boton3 = Button(miFrame, text="3", command=codigoBoton3, width="4")
boton3.grid(row=3, column=2)

botonRest = Button(miFrame, text="-", command=codigoBotonRest, width="4")
botonRest.grid(row=3, column=3)

#--------------- Row 4   ---------------------

botonPunto = Button(miFrame, text=".", command=codigoBotonPunto, width="4")
botonPunto.grid(row=4, column=0)

boton0 = Button(miFrame, text="0", command=codigoBoton0, width="4")
boton0.grid(row=4, column=1)

botonSum = Button(miFrame, text="+", command=codigoBotonSum, width="4")
botonSum.grid(row=4, column=3)

botonIgual = Button(miFrame, text="=", command=codigoBotonIgual, width="4")
botonIgual.grid(row=4, column=2)

raiz.mainloop()