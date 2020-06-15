#------------------ importo paquetes

from tkinter import *
from tkinter import messagebox
import sqlite3


#------------------ creo mi clase ventana

class window(object):

    def __init__(self):           
        self.app = Tk()
        self.app.title("Formulario de mi Base de Datos")

    def creoMisEntries(self):
        self.EntryCodigoID = Entry(self.app)
        self.EntryNombre = Entry(self.app)
        self.EntryApellido = Entry(self.app)
        self.EntryDireccion = Entry(self.app)
        self.EntryTelefono = Entry(self.app)
        self.EntryEmail = Entry(self.app)
        self.TextComentarios = Text(self.app)

    def creoMisBotones(self):

        def codigobotonGuardar(self):  
            conexion1 = sqlite3.connect("base1")
            miCursor = conexion1.cursor()
            try:
                miCursor.execute("""
                CREATE TABLE USUARIOS (
                CODIGOID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50),
                APELLIDO VARCHAR(50),
                DIRECCION VARCHAR(50),
                TELEFONO VARCHAR(50),
                EMAIL VARCHAR(50),
                COMENTARIOS VARCHAR(500))
            """)
            except sqlite3.OperationalError:         
                pass
            finally:
                datos = (varNombre.get(), varApellido.get(), varDireccion.get(), varTelefono.get(),
                varEmail.get(), TextComentarios.get(1.0, END))
                miCursor.execute('INSERT INTO USUARIOS VALUES (NULL, ?,?,?,?,?,?)', datos)
                deleteEntries()
        
            conexion1.commit()
            conexion1.close()  
    
        def codigobotonBuscar():
            conexion1 = sqlite3.connect("base1")
            miCursor = conexion1.cursor()    
            dicDatos = {"CODIGOID": EntryCodigoID.get(), "NOMBRE" : EntryNombre.get(), "APELLIDO" : varApellido.get(),
            "DIRECCION" : varDireccion.get(), "TELEFONO" : varTelefono.get(), "EMAIL" : varEmail.get()}
            #print(dicDatos)
            for CAMPOS, VALORES in dicDatos.items():         
                if VALORES!='':   
                    try:  
                        print(CAMPOS, VALORES)                  
                        miCursor.execute("SELECT * FROM USUARIOS WHERE {}=(?)".format(CAMPOS), (VALORES,))
                        verRegistro = miCursor.fetchall()            
                        varCodigoID.set(verRegistro[0][0])
                        varNombre.set(verRegistro[0][1])
                        varApellido.set(verRegistro[0][2])
                        varDireccion.set(verRegistro[0][3])
                        varTelefono.set(verRegistro[0][4])
                        varEmail.set(verRegistro[0][5])
                        TextComentarios.delete(1.0, END)
                        TextComentarios.insert(END, verRegistro[0][6])
                        break
                    except IndexError:
                        deleteEntries()                
                        break      
            conexion1.commit()
            conexion1.close()  

        def codigobotonModificar():
            conexion1 = sqlite3.connect("base1")
            miCursor = conexion1.cursor()    
            listaDatos = [EntryNombre.get(), varApellido.get(), varDireccion.get(), varTelefono.get(), varEmail.get(), TextComentarios.get(1.0, END)]    
            miCursor.execute("""UPDATE USUARIOS SET NOMBRE = ?, APELLIDO = ?, DIRECCION = ?, TELEFONO = ?, 
            EMAIL = ?, COMENTARIOS = ? WHERE CODIGOID={}""".format(EntryCodigoID.get()), listaDatos)               
            deleteEntries()
            conexion1.commit()
            conexion1.close()


        def codigobotonEliminar():
            conexion1 = sqlite3.connect("base1")
            miCursor = conexion1.cursor()    
            listaDatos = [EntryNombre.get(), varApellido.get(), varDireccion.get(), varTelefono.get(), varEmail.get(), TextComentarios.get(1.0, END)]    
            miCursor.execute("DELETE FROM USUARIOS WHERE CODIGOID={}".format(EntryCodigoID.get()))  
            deleteEntries()
            conexion1.commit()
            conexion1.close()

        def codigobotonLimpiar():
            deleteEntries()
    
        def codigobotonCerrar():
            raiz.destroy()
        
        self.botonGuardar = Button(self.app, text = "Guardar Registro", command = codigobotonGuardar)
        self.botonBuscar = Button(self.app, text = "Buscar Registro", command = codigobotonBuscar)
        self.botonModificar = Button(self.app, text = "Modificar Registro", command = codigobotonModificar)
        self.botonEliminar = Button(self.app, text = "Eliminar Registro", command = codigobotonEliminar)
        self.botonLimpiar = Button(self.app, text = "Limpiar Campos", command = codigobotonLimpiar)
        self.botonCerrar = Button(self.app, text = "Cerrar", command = codigobotonCerrar)
        
                
    def gridder(self):
        EntryCodigoID.grid(row=1, column=1, sticky=W, padx=10, pady=10)
        EntryNombre.grid(row=2, column=1, sticky=W, padx=10, pady=10)
        EntryApellido.grid(row=3, column=1, padx=10, pady=10, sticky=W)
        EntryDireccion.grid(row=4, column=1, padx=10, pady=10, sticky=W)
        EntryTelefono.grid(row=5, column=1, padx=10, pady=10, sticky=W)
        EntryEmail.grid(row=6, column=1, padx=10, pady=10, sticky=W)
        TextComentarios.grid(row=7, column=1, padx=10, pady=10, sticky=W, ipadx=30,ipady=60)    

        labelCodigoID.grid(row=1, column=0, sticky=W)
        labelNombre.grid(row=2, column=0, sticky=W)
        labelApellido.grid(row=3, column=0, sticky=W)
        labelDireccion.grid(row=4, column=0, sticky=W)
        labelTelefono.grid(row=5, column=0, sticky=W)
        labelTelefono.grid(row=5, column=0, sticky=W)
        labelTelefono.grid(row=5, column=0, sticky=W)

        botonGuardar.grid(row=1, column=2, sticky=W)
        botonBuscar.grid(row=2, column=2, sticky=W)
        botonModificar.grid(row=3, column=2, sticky=W)
        botonEliminar.grid(row=4, column=2, sticky=W)
        botonLimpiar.grid(row=5, column=2, sticky=W)
        botonCerrar.grid(row=6, column=2, sticky=W)
        ScrollbarComentarios.grid(row=7, column=2, sticky=W)    

    def get_string(self):
        return self.ent.get()

    #def packer(self):
        #self.ent.pack(anchor = W)
        #self.but.pack(anchor = W)

    def App_Runner(self):
        self.app.mainloop()