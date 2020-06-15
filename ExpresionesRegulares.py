import re

listaNombres = ["Javier Fernandez", "1Diego Torrez", "Luisa Torrez", 
"Claudio Martinez", "Manuel Ibanez", "3Manuel Ibanez", "Luisa Torrez"]

for nombre in listaNombres:
    if re.match("\d", nombre):
        print(nombre)

        REGEX
