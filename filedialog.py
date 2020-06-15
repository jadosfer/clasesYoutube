from tkinter import *
from tkinter import filedialog

raiz=Tk()

def abrirArchivo():
    archivo = filedialog.askopenfilename(title="abrir", initialdir="C:/", filetypes=(("Archivos de Texto",
    "*.txt"),("Archivos pdf","*.pdf"),("Todos los Archivos","*.*")))
    print(archivo)

Button(raiz, text="Abrir Archivo",command=abrirArchivo).pack()

raiz.mainloop()