import requests
import pandas as pd
from matplotlib import pyplot as plt
from pylab import *

def descargaCreaCsv(miUrl, nombreCsv):
    target_csv_path = nombreCsv
    response = requests.get(miUrl)
    response.raise_for_status()
    with open(target_csv_path, "wb") as f:
        f.write(response.content)

def creaDataFrame(nombreCsv, caracteristicas):
    miDataFrame = pd.read_csv(nombreCsv)
    miDataFrame.columns = caracteristicas
    print(miDataFrame.shape)
    print(miDataFrame.head)

    return miDataFrame

def ubicaPlot():
    ubicadorDePantalla = get_current_fig_manager()
    ubicadorDePantalla.window.wm_geometry("+50+75")

def plotBar(caracteristicas, dataFrame, titulo): # Grafica definiendo ubicacion una por una con bar
    miFigura = plt.figure(constrained_layout=True, figsize = [10.92, 5.6])
    miFigura.canvas.set_window_title(titulo)
    Grilla = miFigura.add_gridspec(3, 3)

    subPlot1 = miFigura.add_subplot(Grilla[0, 0], title="N. Autos por {}".format(caracteristicas[0]))
    ejeX = dataFrame[caracteristicas[0]].value_counts().index
    ejeY = dataFrame[caracteristicas[0]].value_counts().values
    subPlot1.bar(ejeX, ejeY)

    subPlot2 = miFigura.add_subplot(Grilla[0, 1], title="N. Autos por {}".format(caracteristicas[1]))
    ejeX = dataFrame[caracteristicas[1]].value_counts().index
    ejeY = dataFrame[caracteristicas[1]].value_counts().values
    subPlot2.pie(ejeY, labels=ejeX, shadow=True, explode=[0.3, 0.05, 0.05, 0.05])
    ubicaPlot()
    plt.show()

def plotsBarFor(caracteristicas, dataFrame, titulo, filas, columnas): # Grafica usando for con bar
    miFigura = plt.figure(constrained_layout=True, figsize = [10.92, 5.6])
    miFigura.canvas.set_window_title(titulo) 
    Grilla = miFigura.add_gridspec(filas, columnas)
    miIndex = 0
    for i in range(filas):
        for j in range(columnas):
            if miIndex == len(caracteristicas):
                break
            else:
                subPlot = miFigura.add_subplot(Grilla[i, j], title="N. Autos por {}".format(caracteristicas[miIndex]))
                ejeX = dataFrame[caracteristicas[miIndex]].value_counts().index
                ejeY = dataFrame[caracteristicas[miIndex]].value_counts().values
                subPlot.bar(ejeX, ejeY)            
                miIndex +=1
    ubicaPlot()
    plt.show()


def plotsPieFor(caracteristicas, dataFrame, titulo, filas, columnas):  #Gráfica usando for con Pie
    miFigura = plt.figure(constrained_layout=True, figsize = [10.92, 5.6])  
    miFigura.canvas.set_window_title(titulo)  
    Grilla = miFigura.add_gridspec(filas, columnas)
    miIndex = 0
    for i in range(filas):
        for j in range(columnas):
            miExplode = []
            if miIndex == len(caracteristicas):
                break
            else:

                subPlot = miFigura.add_subplot(Grilla[i, j], title="N. Autos por {}".format(caracteristicas[miIndex]))
                ejeX = dataFrame[caracteristicas[miIndex]].value_counts().index
                ejeY = dataFrame[caracteristicas[miIndex]].value_counts().values            
                for k in range(len(dataFrame[caracteristicas[miIndex]].value_counts().index)):
                    miExplode.append(0.1)
                subPlot.pie(ejeY, labels=ejeX, shadow=True, explode = miExplode)
                miIndex +=1
        
    ubicaPlot() 
    plt.show()

#---------------------    setups
nombreCsv = "Autos.csv"
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data"
caracteristicas = ["Precio", "Costo Manten", "N. Puertas", "Capacidad Personas",
    "Capacidad Equip", "Seguridad", "Evaluación"] #caracteristicas de los autos
miTitulo = "Cantidad de Autos según Caracteristicas"

#--------------------- llamado a funciones
descargaCreaCsv(url, nombreCsv)
dfAutos = creaDataFrame(nombreCsv, caracteristicas)
#plotBar(caracteristicas, dfAutos, miTitulo)
#plotsBarFor(caracteristicas, dfAutos, miTitulo, 3, 3)
plotsPieFor(caracteristicas, dfAutos, miTitulo, 2, 4)