nombres = []
print(type(nombres))
print (nombres)
nombres = ["santi", "samuel", "aleja", "elsa"]
print (nombres)
print (nombres[2])
nombres.append ("mauricio")
print (nombres)
print (nombres[2])
edades = [18,19,20,17,15,12,8,9]
estaturas = [1.62, 1.80, 1.67, 1.98]
#al ultimo
print (edades[-2])
print (edades[0:2])
print (edades[:3])
print (edades[2:])
edades.sort()
print(edades)
edades.sort(reverse=True)
print(edades)
mayor = max(edades)
print (mayor)
menor = min(edades)
print (menor)
#como contamos cuantos elementos hay
largolistaedades = len(edades)
print(largolistaedades)
#como sumamos elementos?
sumaEdades = sum(edades)
print(sumaEdades)
#como calculo el promedio
promedioEdades = sumaEdades/largolistaedades
print(promedioEdades)
#eliminar un elemento
edades.pop(2)
print(edades)

## ciclo for y las listas
largolistaedades = len(edades)
for indice in range (largolistaedades):
    print("estoy en la posicion",
    indice, "valgo",
    edades[indice])
largoListaNombres = len(nombres)
for indice in range (largoListaNombres):
    print(nombres[indice])

posicionesConValoresPares = []
largolistaedades = len(edades)
for posiciones in range (largolistaedades):
    if(edades[posiciones]%2 == 0):
        posicionesConValoresPares.append(posiciones)

print(edades)
print(posicionesConValoresPares)

#solo cuando les interese mostrar la lista
posicion = 0 
for edad in edades:
    print(edad)
for nombre in nombres:
    print(nombre)
    print(posicion)
    posicion+=1

posicion = 0
posicionesPares = []
for edad in edades:
    if (edad%2 == 0):
        posicionesPares.append(posicion)
    posicion+=1
print(posicionesPares)

