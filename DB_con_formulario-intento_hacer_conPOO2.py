#------------------ importo paquetes

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3


#------------------ creo mi clase ventana

class window(tk.Tk):

    def __init__(self):           
        self.app = Tk()
        self.app.title("Formulario de mi Base de Datos")
        #self.app.miFrame = Frame(self)
        

    def creoEntries(self):
        self.varCodigoID = StringVar()
        self.varNombre = StringVar() 
        self.EntryCodigoID = Entry(self.app, textvariable=self.varCodigoID)
        self.EntryNombre = Entry(self.app, textvariable=self.varNombre)    

    def creoBotones(self):
        def codigobotonGuardar():              
            print("ok")
            conexion1 = sqlite3.connect("base")
            miCursor = conexion1.cursor()
            try:
                miCursor.execute("""
                CREATE TABLE USUARIOS2 (
                CODIGOID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50))
                """)
            except sqlite3.OperationalError:         
                pass
            finally:
                datos = (self.varNombre.get(), NULL)
                miCursor.execute('INSERT INTO USUARIOS2 VALUES (NULL, ?)', datos)
                #deleteEntries()        
            conexion1.commit()
            conexion1.close()
        
        def codigobotonBuscar():
            conexion1 = sqlite3.connect("base")
            miCursor = conexion1.cursor()    
            dicDatos = {"CODIGOID": self.EntryCodigoID.get(), "NOMBRE" : self.EntryNombre.get()}
            #print(dicDatos)
            for CAMPOS, VALORES in dicDatos.items():         
                if VALORES!='':   
                    try:  
                        print(CAMPOS, VALORES)                  
                        miCursor.execute("SELECT * FROM USUARIOS2 WHERE {}=(?)".format(CAMPOS), (VALORES,))
                        verRegistro = miCursor.fetchall()            
                        varCodigoID.set(verRegistro[0][0])
                        varNombre.set(verRegistro[0][1])                        
                        break
                    except IndexError:
                        deleteEntries()                
                        break      
            conexion1.commit()
            conexion1.close()

        self.botonGuardar = Button(self.app, text = "Guardar Registro", command = codigobotonGuardar)
        self.botonBuscar = Button(self.app, text = "Buscar Registro", command = codigobotonBuscar) 



    def creoLabels(self):
        self.labelCodigoID = Label(self.app, text = "CÓDIGOID:")                    
        self.labelNombre = Label(self.app, text = "NOMBRE:")
                        
    def gridder(self):
        self.EntryCodigoID.grid(row=1, column=1, sticky=W, padx=10, pady=10)        
        self.EntryNombre.grid(row=2, column=1, sticky=W, padx=10, pady=10)
        self.labelCodigoID.grid(row=1, column=0, sticky=W)
        self.labelNombre.grid(row=2, column=0, sticky=W)
        self.botonGuardar.grid(row=1, column=2, sticky=W)
        self.botonBuscar.grid(row=2, column=2, sticky=W)   

    #def packer(self):
        #self.ent.pack(anchor = W)
        #self.but.pack(anchor = W)

    def App_Runner(self):
        self.app.mainloop()

raiz = window()
raiz.creoEntries()
raiz.creoBotones()
raiz.creoLabels()
raiz.gridder()
#raiz.packer()
raiz.App_Runner()