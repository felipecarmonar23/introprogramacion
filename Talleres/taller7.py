#----- Taller 7

#----- Punto 1
class Persona():
    def __init__(self, Edad, Nombre, ID):
        self.Edad = Edad
        self.Nombre = Nombre
        self.ID = ID
    def Hablar (self, Mensaje):
        print (Mensaje)
    def Caminar (self, NumeroPasos):
        for Pasos in range(NumeroPasos):
            if (Pasos == 0):
                veces = "paso"
            else :
                veces = "pasos"
            print (f"La persona {self.Nombre} ha caminado {Pasos+1} {veces}")

print ("#"*6, "Punto 1", "#"*6)
Persona1 = Persona (17, "esteban", 9887686)
Persona1.Hablar ("Hola, buenos días")
Persona1.Caminar (3)

#---Punto 2---#
class Doctor(Persona):
    def __init__(self,Edad, Nombre, ID, Especialidad):
        super().__init__(Edad, Nombre, ID)
        self.Especialidad = Especialidad
    def Curar (self, Enfermedad):
        print (f"Procedo a tratar la enfermedad {Enfermedad}")

print ("#"*6, "Punto 2", "#"*6)
Doctor1 = Doctor (45, "velez", 87878788, "Cardiologo")
Doctor1.Curar ("cardiopatia")

#---Punto 3---#
class Nutricionista(Persona):
    def __init__(self,Edad, Nombre, ID, UniversidadEgresado):
        super().__init__(Edad, Nombre, ID)
        self.UniversidadEgresado = UniversidadEgresado
    def IMC(self, peso, estatura): 
        imc = peso/(estatura**2)
        print(f"El IMC del paciente es {imc}")

print ("#"*6, "Punto 3", "#"*6)
Nutricionista1 = Nutricionista (25, "Miguel", 83387383783, "Universidad CES")
Nutricionista1.IMC (71, 1.80)

#---Punto 4---#
class Abogado(Persona):
    def __init__(self,Edad, Nombre, ID, Especialidad, UniversidadEgresado):
        super().__init__(Edad, Nombre, ID)
        self.UniversidadEgresado = UniversidadEgresado
        self.Especialidad = Especialidad
    def Representar (self, nombre, caso):
        print (f"Procedo a representar al cliente {nombre} en el caso de {caso}")

print ("#"*6, "Punto 4", "#"*6)
Abogado1 = Abogado (49, "Camilo", 456666, "Penal", "Universidad de Medellin")
Abogado1.Representar ("Pablo", "asesinato")