from tkinter import *

raiz=Tk()
raiz.geometry("500x400+250+100")
raiz.title("Bienes Raíces")

miImagen=PhotoImage(file="bienes_raices.png")
Label(raiz, image=miImagen).pack()

miFrame = Frame(raiz)
miFrame.pack()

Label(miFrame, text="Elige tu búsqueda: ").pack()

Departamento=IntVar()
Casa=IntVar()
Local=IntVar()

def opcionElegida():
    miOpcion =""
    if Departamento.get()==1:
        miOpcion += "Departamento\n"
    if Casa.get()==1:
        miOpcion += "Casa\n"
    if Local.get()==1:
        miOpcion += "Local\n"

    etiqueta_abajo.config(text=miOpcion)

Checkbutton(miFrame, text="Departamento", variable=Departamento, onvalue=1, offvalue=0, command=opcionElegida).pack()
Checkbutton(miFrame, text="Casa", variable=Casa, onvalue=1, offvalue=0, command=opcionElegida).pack()
Checkbutton(miFrame, text="Local", variable=Local, onvalue=1, offvalue=0, command=opcionElegida).pack()

etiqueta_abajo=Label(miFrame)
etiqueta_abajo.pack()

raiz.mainloop()





