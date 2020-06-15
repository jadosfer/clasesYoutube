from tkinter import *
from tkinter import messagebox

raiz=Tk()

miMenu = Menu(raiz)
raiz.config(menu=miMenu)

def info():
    messagebox.showinfo("V.S.C.", "Version 1.44\nDate:2020-04-16") 

def aviso():
    messagebox.showwarning("Advertencia", "Este archivo no fue guardado")

def avisoSalir():
    respuesta=messagebox.askquestion("Cuidado", "¿Está seguro de que quiere salir?")
    if respuesta=="yes":
        raiz.destroy()

def nuevoArchivo():
    respuestaNuevo=messagebox.askokcancel("New File", "¿Desea abrir un nuevo archivo?")
    if respuestaNuevo==True:
        raiz.destroy()

miFile=Menu(miMenu, tearoff=0)
miFile.add_command(label="New File", command=nuevoArchivo)
miFile.add_command(label="New Window")
miFile.add_separator()
miFile.add_command(label="Open File...")
miFile.add_command(label="Close Editor", command=aviso)
miFile.add_command(label="Exit", command=avisoSalir)

miEdit=Menu(miMenu, tearoff=0)
miEdit.add_command(label="Undo")
miEdit.add_command(label="Redo")
miEdit.add_separator()
miEdit.add_command(label="Cut")
miEdit.add_command(label="Copy")
miEdit.add_command(label="Paste")

miHelp=Menu(miMenu, tearoff=0)
miHelp.add_command(label="Welcome")
miHelp.add_command(label="About", command=info)


miMenu.add_cascade(label="File", menu=miFile)
miMenu.add_cascade(label="Edit", menu=miEdit)
miMenu.add_cascade(label="Help", menu=miHelp)


raiz.mainloop()
