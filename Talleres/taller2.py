#-----constantes-----#
PREGUNTA_numeroA = "cual es el numero A?  :  "
PREGUNTA_numeroB = "cual es el numero B?  :  "
MENSAJE_SUMA = "la suma de A+B es"
MENSAJE_RESTA = "la resta de A-B es"
MENSAJE_MULTIPLICACION = "la multiplicacion de A*B es"
MENSAJE_DIVISION = "la division de A/B es"
MENSAJE_EXPONENTE = "el exponente de A**B es"

#-----entrada al codigo-----#
#aca solo estan permitidos los numeros enteros
print("#"*15, "NUMERO ENTERO", "#"*15)
numeroA = int(input(PREGUNTA_numeroA))
numeroB = int(input(PREGUNTA_numeroB))
ismayorA = numeroA >= numeroB
print ("la ecuacion de A >= a B es", ismayorA)
print (MENSAJE_SUMA, numeroA + numeroB)
print (MENSAJE_RESTA, numeroA - numeroB)
print (MENSAJE_MULTIPLICACION, numeroA * numeroB)
print (MENSAJE_DIVISION, numeroA / numeroB)
print (MENSAJE_EXPONENTE, numeroA ** numeroB)

#aca solo estan permitidos los numeros decimales
print("#"*15, "NUMERO DECIMAL", "#"*15)
numeroA = float(input(PREGUNTA_numeroA))
numeroB = float(input(PREGUNTA_numeroB))
ismayorA = numeroA >= numeroB
print ("la ecuacion de A >= a B es", ismayorA)
print (MENSAJE_SUMA, numeroA + numeroB)
print (MENSAJE_RESTA, numeroA - numeroB)
print (MENSAJE_MULTIPLICACION, numeroA * numeroB)
print (MENSAJE_DIVISION, numeroA / numeroB)
print (MENSAJE_EXPONENTE, numeroA ** numeroB)
