#listaPrueba = [["2", "Javier", "Fernandez", "7"], ["1", "Diego", "Maradona", "1"], ["3","Fede", "Vargas", "10"]]

#------------   ingresamos legajo y nota
listaLegajos = []
while True: 
    numeroLegajo = input("Ingrese Numero de Legajo: ")
    if numeroLegajo == '-1':
        break
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    nota = input("Ingrese nota: ")
    while True:
        if int(nota) >= 1 and int(nota) <=10:
            break
        else:
            nota = input("Error, nota ingresada incorrecta. Ingrese nota nuevamente: ")

    listaLegajos.append([numeroLegajo, nombre, apellido, nota])
 
print(listaLegajos)


def ordenaLegajos(lista):
    desordenado = True
    while desordenado:
        desordenado = False
        for i in range(len(lista)-1):
            if lista[i][0] > lista[i+1][0]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                desordenado = True
    return lista

def imprimeTodos(lista):
    for alumno in lista:
        print("Nro. Legajo: ", alumno[0])    
        print("Nombre: ", alumno[1])
        print("Apellido: ", alumno[2])
        print("Nota: ", alumno[3], "\n")

def imprimeNotaMax(lista):
    mayor = 0
    pos = 0
    for i in range(len(lista)):   
        if int(listaPrueba[i][3]) > int(mayor):        
            mayor =  lista[i][3]
            pos = i
    print(lista[pos])

def busquedaBinaria(lista, dato):
    izq = 0
    der = len(lista)-1
    pos = -1                                #dato = 2
    while pos == -1:         #izq = 0, 2     der = 2,
        centro = (izq + der)//2              #              centro = 1,
        if int(lista[centro][0]) == int(dato):      #listacentro 1,
            pos = centro
        elif int(lista[centro][0]) < int(dato):
            izq = centro + 1
        else:
            der = centro -1
    print(pos)        
    return pos

def buscaImprimeLegajo(lista, dato):
    pos = busquedaBinaria(lista, dato)
    print(lista[pos])

#imprimeNotaMax(listaPrueba)
#imprimeTodos(listaPrueba)
#legajosOrdenados = ordenaLegajos(listaPrueba)
#imprimeTodos(legajosOrdenados)
#buscaImprimeLegajo(listaPrueba, 2)

listaLegajosOrdenada = ordenaLegajos(listaLegajos)
imprimeTodos(listaLegajosOrdenada)

