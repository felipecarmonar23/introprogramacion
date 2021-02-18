#-----condicionales------#
MENSAJE_BIENVENIDA = "hola, espero estes bien"
MENSAJE_MAYOR = "El numero A es mayor que B"
MENSAJE_MENOR = "El numero A es menor que B"
MENSAJE_IGUAL = "A y B son iguales"
PREGUNTA_NUMERO_A = "ingrese un numero A  :  "
PREGUNTA_NUMERO_B = "ingrese un numero B  :  "

#-----entrada al codigo-----#
print (MENSAJE_BIENVENIDA)
numeroA = int (input(PREGUNTA_NUMERO_A))
numeroB = int (input(PREGUNTA_NUMERO_B))
isMayor = numeroA > numeroB
isMenor = numeroA < numeroB

if(isMayor):
    print(MENSAJE_MAYOR)
elif(isMenor):
    print(MENSAJE_MENOR)
else:
    print(MENSAJE_IGUAL)
