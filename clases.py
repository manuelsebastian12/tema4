"""En este archivo se realizan las clases"""

class Persona():
    def __init__(self, nombre):
        self.nombre = nombre
        self.__estatura = "1.85 m"

    def trabajar(self):
        pass

    def getEstatura(self):
        return print("Su estatura es de ", self.__estatura)

class Empresa():
    def __init__(self):
        pass
    def NombreEmpresa(self):
        print("En la empresa multinacional M&MTechnologies")

class Gerente(Persona, Empresa):
    def __init__(self, nombre):
        super().__init__(nombre)
        pass

    def entrevistar(self):
        b = self.nombre
        print("El gerente se llama ", b, ", en este momento está entrevistando a un candidato para una vacante")

    def trabajar(self):
        print("Más tarde el gerente realizará una supervisión a las diferentes áreas")

    def vestir(self):
        print("El gerente viste un traje de color azul y una corbata roja")

class Empleado(Persona, Empresa):
    def __init__(self, nombre):
        super().__init__(nombre)
        pass

    def trabajar(self):
        print("El empleado está realizando sus actividades correspondientes")