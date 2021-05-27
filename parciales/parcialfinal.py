#----- Parcial final
#----- primer punto

import matplotlib.pyplot as plt
import pandas as pd
import sys

print ("#"*10, "Punto 1", "#"*10)
pregunta_alimentos = "di un alimento que te guste  :"
pregunta_valor = "que vale ese alimento  :"
alimentos = []
n = 8
while (n>0):
    alimento = input(pregunta_alimentos)
    alimentos.append(alimento)
    n=n-1

valores = []
n = 8
while (n>0):
    valor = int(input(pregunta_valor))
    valores.append(valor)
    n = n-1
plt.bar (alimentos, valores, width = 0.7, color = "r")

plt.title ("alimentos favoritos y su precio")
plt.xlabel ("nombre del alimento")
plt.ylabel ("precio del alimento")
plt.savefig ("graficosSnacksyPrecio.png")

#----- punto dos

print ("#"*10, "Punto 2", "#"*10)
class Humano():
    def _init_(self, Nombre, Sexo, Edad):
        self.Nombre = Nombre
        self.Sexo = Sexo
        self.Edad = Edad
    def Hablar (self, Mensaje):
        print (Mensaje)

Humano1 = Humano ("Felipe", "Masculino", 20)
Humano1.Hablar ("sin conocerlo, lo vamos a extrañar mucho profe")

class Doctor(Humano):
    def _init_(self, Nombre, Sexo, Edad):
        self.Nombre = Nombre
        self.Sexo = Sexo
        self.Edad = Edad
    def IMC(self, peso, estatura): 
        imc = peso/(estatura**2)
        print(f"El IMC del dotor uribe es: {imc}")

Doctor1 = Doctor ("Uribe", "Masculino", 68)
Doctor1.IMC (70, 1.73)

#----- punto tres

repciclos = 1

while (repciclos == 1):
    try:
        nombre = str(input("ingresa tu nombre: "))
        assert (nombre.isalpha())
        repciclos = 2
    except AssertionError:
        print ("ingresaste un dato invalido, por favor, compruebe nuevamente")

while (repciclos == 2):
    try:
        dinero_dolares = int(input("cuanto dnero tienes en dolares"))
        repciclos = 3
    except ValueError:
        print ("dato invalido, compruebe nuevamente")

print(f"el señor : " [nombre], "cuenta con : " [dinero_dolares], "dolares" )




#----- punto cuatro

print ("#"*10, "Punto 4", "#"*10)

nombre = input("ingrese su nombre : ")
enfermedad = input("ingrese su enfermedad : ")
precio = int(input("cual fue el precio de la consulta : "))

nombre_archivo = "pacientes.txt"
try:
    archivo = open(nombre_archivo)
    print("1")
except FileNotFoundError:
    archivo = open (nombre_archivo, "w", encoding= "UTF-8")
    descripcion = "archivo de pacientes neurologicos"
    print("2")
    archivo.writelines(descripcion)
    sys.exit(1)

archivo = open (nombre_archivo, "a")
linea = " \nombre: " + nombre + "enfermedad: " + str(enfermedad) + "precio:" + str(precio)
archivo.writelines(linea)
archivo.close()

"profe gracias por todo"