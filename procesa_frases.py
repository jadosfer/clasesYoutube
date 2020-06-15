frase = input("Por favor ingrese una frase: ")
for i in range(len(frase)):
    if i%2 == 0:
        print(frase[i], end="")
print("")
 
print("Las vocales contenidas en la frase son: ", end="")
for i in range(len(frase)):
    if frase[i] == "a" or frase[i] == "e" or frase[i] == "i" or frase[i] == "o" or frase[i] == "u":
        print(frase[i], end=" ")



   