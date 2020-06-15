from io import open

archivo_text = open("mi_fila.txt", "w")
mi_texto = "Esta es mi primera oración"
archivo_text.write(mi_texto)
archivo_text.close()

archivo_text = open("mi_fila.txt", "r")
mi_texto = archivo_text.read()
archivo_text.close()
print(mi_texto)


