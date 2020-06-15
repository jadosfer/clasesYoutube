import requests
import pandas as pd
from matplotlib import pyplot as plt
from pylab import *

def descargaCreaCsv(miUrl):    
    response = requests.get(miUrl)
    response.raise_for_status()   
    with open("miCsv.csv", "wb") as f:
        f.write(response.content)

def creaDataFrame():      
    miDataFrameT = pd.read_csv("API_ARG_DS2_es_csv_v2_1125810.csv")
    miDataFrame = miDataFrameT.T
    #miDataFrame.columns = miDataFrame[:,5]
    print(miDataFrame.shape)
    #print(miDataFrame.head)


    return miDataFrame

def ubicaPlot():
    ubicadorDePantalla = get_current_fig_manager()
    ubicadorDePantalla.window.wm_geometry("+50+75")

#Gráfica usando plot o barras segun caracteristica
def plotDataframe(titulo, filas, columnas, miUrl):  
    #descargaCreaCsv(miUrl)
    dataFrame = creaDataFrame()    
    caracteristicas = dataFrame[:,5]
    """
    miFigura = plt.figure(constrained_layout=True, figsize = [10.92, 5.6])  
    miFigura.canvas.set_window_title(titulo)  
    Grilla = miFigura.add_gridspec(filas, columnas)
    miIndex = 0
    for i in range(filas):
        for j in range(columnas):            
            if miIndex == len(caracteristicas):
                break
            elif len(dataFrame[caracteristicas[miIndex]].value_counts().index)<17:
                subPlot = miFigura.add_subplot(Grilla[i, j], title="{}".format(caracteristicas[miIndex]))
                ejeX = dataFrame[caracteristicas[miIndex]].value_counts().index
                ejeY = dataFrame[caracteristicas[miIndex]].value_counts().values                
                subPlot.bar(ejeX, ejeY) 
                miIndex +=1
            else:
                ejeY = dataFrame[caracteristicas[miIndex]]
                subPlot = miFigura.add_subplot(Grilla[i, j], title="{}".format(caracteristicas[miIndex]))                
                subPlot.plot(ejeY) 
                miIndex +=1
      





    ubicaPlot() 
    plt.show()
    """
#---------------------    setups
#Autos
"""
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data"
caracteristicas = ["Precio", "Costo Manten", "N. Puertas", "Capacidad Personas",
    "Capacidad Equip", "Seguridad", "Evaluación"] #caracteristicas de los autos
miTitulo = "Cantidad de Autos según Caracteristicas"
"""
#Enfermedades corazón
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"
caracteristicas = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang",
"oldpeak", "slope", "ca", "thal", "num"]
miTitulo = "Muertes cardíacas según Caracteristicas"

#--------------------- llamado a funciones
plotDataframe(miTitulo, 4, 3, url)