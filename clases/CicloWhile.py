MENSAJE_SALUDO = "Bienvenido, estoy para servirte"
MENSAJE_AHORRO = "Llevas ahorrando..."
PREGUNTAR_VALOR_CPU = "Cuánto vale el pc que deseas? :"
PREGUNTAR_CUANTO_TIENE = "Cuanto llevas ahorrando? :"

#---Entrada de código---#
print(MENSAJE_SALUDO)
valor = float (input(PREGUNTAR_VALOR_CPU))
ahorrado = float (input(PREGUNTAR_CUANTO_TIENE))

while (valor > ahorrado) :
    print(MENSAJE_AHORRO, ahorrado, "te faltan...", valor - ahorrado)
    ahorrado = ahorrado + 1000
print (valor == ahorrado)