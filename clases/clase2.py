pruebaV = True
pruebaF = False
print(pruebaF)
print(pruebaV)
edad = 20
estatura = 1.76
peso = 84
apellido = "Carmona"
NOMBRE = "Felipe Carmona Rios"
print("#"*15, "Mayor Edad", "#"*15)
isMayorEdad = edad >= 20
print(isMayorEdad)
print("#"*15, "Bajo La Estatura Promedio", "#"*15)
isMayorEstatura = estatura < 1.70
print(isMayorEstatura)
print("#"*15, "Peso Diferente 84", "#"*15)
isPesoDiferente = peso != 84
print(isPesoDiferente)
print("#"*15, "apellido In Nombre", "#"*15)
isApellido = apellido in NOMBRE
print(isApellido)         
