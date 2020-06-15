contador = 0
carga = 1
SumaPositivos = 0
ContadorPositivos = 0

carga = int(input("Ingrese números enteros, la carga finaliza con un multiplo de 3 :\n"))

while carga%3 != 0:   
    
    
    if carga > 50:  
        for i in range(10):
            print(carga -10 +i, end=" ") #imprime los últimos 10    
        print("\n")

    if carga > 0: #encuentro los dividores si el numero de entrada es positivo
        for i in range(1,carga):
            if carga%i == 0:
                print("El número ", carga, " es divisible por ", i, "y por ", carga, "\n")
    
        SumaPositivos = SumaPositivos + carga
        ContadorPositivos = ContadorPositivos + 1
    
    contador = contador + 1
    carga = int(input("Ingrese números enteros, la carga finaliza con un multiplo de 3 :\n"))

PromedioPositivos = SumaPositivos/ContadorPositivos
print("El promedio de los números Positivos ingresado es = ",PromedioPositivos)







