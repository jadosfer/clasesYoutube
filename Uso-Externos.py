from io import open

MiArchivo = open("MiArchivo.txt", "r+" ) #lectura-escritura
MiArchivoCopia = open("MiArchivoCopia.txt", "w+")

TextoLista = MiArchivo.readlines()
TextoLista[2] = "Inserto Linea\n"
MiArchivoCopia.writelines(TextoLista)
MiArchivoCopia.seek(0)
print(MiArchivoCopia.read())













