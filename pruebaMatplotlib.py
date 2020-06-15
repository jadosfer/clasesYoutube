import numpy as np

r = np.array([[0, 1.55]], "float32").round(0)
a = int(r[0, 0])
b = int(r[0, 1])
print ('Valor a:', a)
print('Valor b:', b)
# Creando la ventana

from tkinter import *

window = Tk()
window.title("Visualizando Valores de un array")
window.geometry('300x100')
lbl1 = Label(window, text='Valor a: {}'.format(a))
lbl1.grid(column=0, row=0)
lbl2 = Label(window, text='Valor a: {}'.format(b))
lbl2.grid(column=1, row=1)
window.mainloop()
