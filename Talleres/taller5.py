listaEdades = [18,21,30,23,40,67,50,24,18,38,74,25,44,72,63,85,27,51,99,83]

#----- punto 1

print("#"*15, "edades de la lista", "#"*15)
def lista ():
    for elemento in listaEdades:
        print(elemento)

lista()

#----- punto 2

print("#"*15, "edad mayor, menor y promedio", "#"*15)
def edades ():
    print ("la edad mas alta de la lista es : ", max(listaEdades))
    print ("la edad mas baja de la lista es : ", min(listaEdades))
    print ("el promedio de edades es : ", sum (listaEdades) / len (listaEdades))

edades()

#----- punto 3

print("#"*15, "cantidad de saludos", "#"*15)
def saludo (veces):
    for saludo in range (veces):
        print("que se dice")

veces = int(input("ingrese cuantas veces quiere ser saludado : "))

saludo(veces)

#----- punto 4
print("#"*15, "edades pares de la lista", "#"*15)
def numeroPares ():
    for numeros in listaEdades:
        if (numeros%2 == 0):
            print(numeros)

numeroPares()

#-----punto 5
print("#"*15, "edades mayores a 24", "#"*15)
def numeroMayores ():
    for mayores in listaEdades:
        if (mayores > 24):
            print(mayores)

numeroMayores()

#----- punto 6
print("#"*15, "IMC", "#"*15)
def IMC (peso, estatura):
    imc = peso/ (estatura**2)
    return imc

peso = float(input("ingrese su peso : "))
estatura = float(input("ingrese su estatura : "))

tu_imc = IMC(peso, estatura)
print("cuentas con un IMC de : ", tu_imc)

#----- punto 7

def despedida (nombre):
    print("que te vaya bien", nombre)

nombre = input("cual es tu nombre : ")

despedida(nombre)








