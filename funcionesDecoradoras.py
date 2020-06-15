"""Este modulo ejemplifica el uso de funciones decoradoras"""

def decorarConTexto(funcion):
    def funcionInterna(a, b):
        print("Primera parte de la decoración. El resultado de la función es: ")
        funcion(a,b)
        print("Última parte de la decoración. Me despido\n")
    return funcionInterna


@decorarConTexto
def suma(a,b):
    print(a+b)

@decorarConTexto
def resta(a,b):
    print(a-b)

suma(6,2)
resta(8,2)


