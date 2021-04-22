#----- Taller 6

#----- Punto 1
class Torta():
    def __init__ (self,FormaEntrada, SaborEntrada, AlturaEntrada):
        self.Forma = FormaEntrada
        self.Sabor = SaborEntrada
        self.Altura = AlturaEntrada
        print(f""" 
        Mi forma es {self.Forma}
        Mi sabor es {self.Sabor}
        Mi altura es {self.Altura} centimetros
        """)

print ("#"*6, "Mi torta", "#"*6)
Mi_Torta = Torta(f"Con niveles","Tres leches",50)

#----- Punto 2
class Estudiante():
    def __init__(self, Edad, Nombre, ID, Carrera, Semestre):
        self.Edad = Edad
        self.Nombre = Nombre
        self.ID = ID
        self.Carrera = Carrera
        self.Semestre = Semestre
    def TiempoEstudio (self, Materia, Tiempo):
        print (f"Voy a estudiar {Materia} por {Tiempo} horas")


print ("#"*6, "Horas de estudio", "#"*6)
Estudiante1 = Estudiante (19, "Felipe", 1000646371, "Biomédica", "quinto semestre")
Estudiante1.TiempoEstudio ("Programación", 2)

#----- Punto 3
class Nutricionista():
    def __init__(self, Edad, Nombre, Universidad):
        self.Edad = Edad
        self.Nombre = Nombre
        self.Universidad = Universidad
    def IMC(self, peso, estatura): 
        imc = peso/(estatura**2)
        print(f"El IMC del paciente es {imc}")

print ("#"*6, "IMC", "#"*6)
Nutricionista1 = Nutricionista (20, "andres", "Universidad CES")
Nutricionista1.IMC (95, 1.80)

#----- Punto 4
class Canguro():
    def __init__(self, Edad, ID, Nombre):
        self.Edad = Edad
        self.ID = ID
        self.Nombre = Nombre
    def SaltosCanguro (self, NumeroSaltos):
        for Salto in range(NumeroSaltos):
            if (Salto == 0):
                veces = "vez"
            else :
                veces = "veces"
            print (f"El canguro {self.Nombre} ha saltado {Salto+1} {veces}")

print ("#"*6, "Saltos del Canguro", "#"*6)
Canguro1 = Canguro (30, 76765456, "fernando")
Canguro1.SaltosCanguro (2)

#----- Punto 5
class Instrumento():
    def __init__(self, Nombre, Color, Años):
        self.Nombre = Nombre
        self.Color = Color 
        self.Años = Años
    def Interpretar (self, melodia):
        print(f"Se está interpretando la melodia {melodia} en el {self.Nombre}, el cual es de color {self.Color} y tiene {self.Años} años de uso")

print ("#"*6, "Instrumento", "#"*6)
Instrumento1 = Instrumento ("Piano", "negro", 8)
Instrumento1.Interpretar ("spring waltz")