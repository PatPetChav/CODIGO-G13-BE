#podemos hacer una abstraccion con la clase persona
class Persona:
    def __init__(self, nom,ema):
        self.nombre = nom
        self.email = ema
    
    def mostrar(self):
        print("Nombre : " + self.nombre + " Email :" + self.email)


class Alumno(Persona):
    pass


class Profesor(Persona):
    def __init__(self,nom,ema,mod):
        super().__init__(nom,ema)
        self.modulo = mod

    #sobre escribimos mostrar
    def mostrar(self):
        super().mostrar()
        print("dicta el modulo de : " + self.modulo)


   
alu1 = Alumno("carlos tello","ctello@gmail.com")
alu1.mostrar()

profe1 = Profesor("cesar mayta","cesar@gmail.com","BackEnd")
profe1.mostrar()


