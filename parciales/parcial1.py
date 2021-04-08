#-----parcial 1

#-----punto 1

print ("#"*10, "punto 1", "#"*10)

def sumar (a=0, b=0, c=0):
    suma = a+b+c
    return suma

def restar (a=0, b=0, c=0):
    resta = a-b-c
    return resta

def multiplicar (a=0, b=0, c=0):
    multiplicacion = a*b*c
    return multiplicacion

def dividir (a=0, b=1, c=1):
    division = a/b/c
    return division

def potencia (base=0, a=1, b=1):
    potenciacion = base ** a ** b
    return potenciacion

def operaciones (operacion, a, b, c):
    print(operacion(a, b, c))

operaciones (sumar, 2,4,6)
operaciones (restar, 5,7,2)
operaciones (multiplicar, 4,5,6)
operaciones (dividir, 31,2,3)
operaciones (potencia, 3,2,3)

#-----punto 2

print ("#"*10, "punto 2", "#"*10)

listaPaises = ["colombia","peru","china","canada","chile","argentina"]
listaCarros = ["subaru","toyota","mazda","porsche","ferrari","chevrolet","renault"]
ListaCelulares = ["huawei","iphone","samsung","alcatel","nokia","blackberry"]

print ("#"*10, "paises", "#"*10)

def lista1 ():
    for elemento in listaPaises:
        print (elemento)


lista1 ()

print ("#"*10, "carros", "#"*10)

def lista2 ():
    for elemento in listaCarros:
        print (elemento)


lista2 ()

print ("#"*10, "celulares", "#"*10)

def lista3 ():
    for elemento in ListaCelulares:
        print (elemento)

lista3 ()

#-----punto 3

print ("#"*10, "punto 3", "#"*10)

def area (base, alura):
    area = (base * altura)/2
    return area


base = float(input("ingrese la base : "))
altura = float(input("ingrese la altura : "))



el_area = area (base,altura)

print("el area es : ",el_area)


#----- punto 4

print ("#"*10, "punto 4", "#"*10)

listaNumeros = [1,535,3,26,8,2467,8,2,7,26,8,253,17,26,37]

def lista():
    print("el numero mayor de la lista es el : ", max(listaNumeros))
    print("el numero menor de la lista es el : ", min(listaNumeros))
    print("el promedio de la lista es : ", sum(listaNumeros) / len (listaNumeros))

lista()

#-----punto 5

print ("#"*10, "punto 5", "#"*10)

listaFibonacci = [0,1,1,2,3,5,8,13,21,34,55,89,144]

def mostrarListaFibonacci (valor):
    valor1 = 0
    valor2 = 1
    for elemento in range (valor-1):
        secuencia = valor1+valor2
        valor1 = valor2
        valor2 = secuencia
    return(valor1)
posicion = mostrarListaFibonacci(5)

print("el numero de la lista fibonacci es el : ",posicion)

