#-----constantes-----#
PREGUNTA_NOMBRE = "como te llamas?  :  "
PREGUNTA_EDAD = "cuantos años tienes?  :  "
PREGUNTA_ESTATURA = "cuanto mides?  :  "
MENSAJE_SALUDO = "un gusto conocerte"

#-----entrada al codigo-----#
nombre = input (PREGUNTA_NOMBRE)
edad = int(input(PREGUNTA_EDAD))
print (MENSAJE_SALUDO, nombre)
estatura = float(input(PREGUNTA_ESTATURA))