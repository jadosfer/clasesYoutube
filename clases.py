class humano:    
        
    def __init__(self, anios):
        self.piel = "morena"
        self.brazos = 2
        self.piernas = 2
        self.cabeza = 1
        self.torso = 1        
        self.anios_vida = anios
        self.salud="ok"      
        print("Usted ha nacido y vivirá ",anios," anios")

    def chequeo_salud(self):
        print("chequeando")
        if self.salud=="ok":            
            return True
        else:
            return False

    def vive_10_anios(self):
        chequeo = self.chequeo_salud()
        if self.anios_vida > 0 and chequeo:        
            self.anios_vida += -10
            print("usted vivirá", self.anios_vida, "anios más")
        else:
            print("ud muere")
    
    def estado(self):
        print("Estado: ")
        print("piel:", self.piel, " piernas:", self.piernas, " brazos:", self.brazos, "\ncabeza:", self.cabeza, " torso:", self.torso, " anios de vida:", self.anios_vida)

    

class mujer(humano):
    vagina = 1
    senos = 2

    def gestar_bebe(self):
        print("estás embazarada")

    def estado(self):
        print("piel:", self.piel, " piernas:", self.piernas, " brazos:", self.brazos, "\ncabeza:", self.cabeza, " torso:", self.torso, " anios de vida:", self.anios_vida, "vagina: ", self.vagina, "senos: ", self.senos)
        


class jefe:
    molestar="siempre"

    def estado(self):
        print("cuando molesto?: ", self.molestar)


class mujer_jefe(jefe,mujer):
    pass

mi_jefa = mujer_jefe(40)
mi_jefa.estado()
mi_jefa.gestar_bebe()

