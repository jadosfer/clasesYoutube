class humano:
    def __init__(self, nombre, edad):
        self.nombre =nombre
        self.edad = edad

    def __str__(self):
        return "{} tiene {} años".format(self.nombre, self.edad)

humanos = [
    humano("Diego", 33),
    humano("Martin", 23),
    humano("Javier", 39)
    ]

humamos = list(map(lambda Persona: humano(Persona.nombre, Persona.edad + 1), humanos))
for i in humamos:
    print(i)