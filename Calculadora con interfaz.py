from tkinter import *

raiz=Tk()

miMenu = Menu(raiz)
raiz.config(menu=miMenu)

miFile = Menu(miMenu)
miEdit = Menu(miMenu)
miHelp = Menu(miMenu)

miMenu.add_cascade(label="File", menu=miMenu)


raiz.mainloop()