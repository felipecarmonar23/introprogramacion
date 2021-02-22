#punto numero 1
#-----constantes
print ("#"*15, "punto numero 1", "#"*15)
MENSAJE_BIENVENIDA = "bienvenido al taller 3"
MENSAJE_MAYOR_A = "el numero A es mayor"
MENSAJE_MAYOR_B = "el numero B es mayor"
MENSAJE_IGUAL = "el numero A es igual al numero B"
numeroA = 8
numeroB = 11

#-----entradas al codigo
print (MENSAJE_BIENVENIDA)
IsMayorA = numeroA > numeroB
isMayorB = numeroA < numeroB

if(IsMayorA): 
    print (MENSAJE_MAYOR_A)
elif(isMayorB):
    print (MENSAJE_MAYOR_B)
else: 
    print (MENSAJE_IGUAL)


#punto numero 2
print ("#"*15, "punto numero 2", "#"*15)
#-----constantes
PREGUNTA_EDAD = "cuantos años tienes?  :"
MENSAJE_MENOR_EDAD = "aun estas muy chiquito"
MENSAJE_JOVEN = "tus desiciones definen tu futuro"
MENSAJE_ADULTO = "ya estas viejito"
MENSAJE_ADULTO_MAYOR = "paila"

#-----entradas al codigo
edad = int(input(PREGUNTA_EDAD))
isMenorEdad = edad < 18
IsJoven = edad >= 18 and edad <= 26
IsAdulto = edad >= 27 and edad <= 55
IsAdultoMayor = edad >= 55
resultado = ""

if(isMenorEdad):
    print (MENSAJE_MENOR_EDAD)
elif(IsJoven):
    print(MENSAJE_JOVEN)
elif(IsAdulto):
    print(MENSAJE_ADULTO)
else:
    print(MENSAJE_ADULTO_MAYOR)

print(resultado)

#punto numero 3
print ("#"*15, "punto numero 3", "#"*15)
#-----constantes
PREGUNTA_AÑO_NACIMIENTO = "en que año naciste?  :"
PREGUNTA_AÑO_ACTUAL = "en que año estamos?  :"
PREGUNTA_AÑO_MUERTE = "hasta que año quieres vivir?  :"

#-----entradas al codigo
Año = int(input(PREGUNTA_AÑO_ACTUAL))
AñoNacimiento = int(input(PREGUNTA_AÑO_NACIMIENTO))
AñoMuerte = int(input(PREGUNTA_AÑO_MUERTE))
IsAñosQueLlevasVivo = Año - AñoNacimiento
IsAñosQueFaltanParaMorirte = AñoMuerte - Año

if(IsAñosQueLlevasVivo):
    print("llevas", Año - AñoNacimiento,"años vivo")

if(IsAñosQueFaltanParaMorirte):
    print("te faltan", AñoMuerte - Año, "años para morirte")


#punto numero 4
print ("#"*15, "punto numero 4", "#"*15)
#-----constantes
PREGUNTA_DISTANCIA = "coloca una distancia en centimetros  :"

#-----entradas al codigo
distancia = float(input(PREGUNTA_DISTANCIA))
IsKilometros = distancia * 10**-5
IsMetros = distancia * 10**-2

if(IsMetros):
    print ("la distancia en metros es", IsMetros)

if(IsKilometros):
    print("la distancia en kilometros es", IsKilometros)



