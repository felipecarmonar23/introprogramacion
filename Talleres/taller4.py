listaDolares = [20000,30000,4000,2500,1000,7600]

#-----preguntas

preguntaOpcion  = """Ingrese una opcion
    1.convertir dolares en pesos o euros
    2.mostar lista clasificacion de ingresos
    3.Mostrar valor más alto, más bajo y promedio
    4.Salir
"""

preguntaDivisa  = """
    D - permanecer en dolares
    C - Mostrar en pesos
    E - Mostrar en Euros
"""
preguntaIngreso = " cual es tu ingreso mensual en dolares? : "

#-----conversion

listaPesos = []
for elemento in listaDolares :
    conversor = round( elemento * 3.700)
    listaPesos.append (conversor)
listaEuros = []
for elemento in listaDolares:
    conversor = round (elemento * 0.84)
    listaEuros.append (conversor)

listaClasificacion = """
######## CLASIFICACION DEPENDIENDO DE LOS INGRESOS #########
ingresos mensuales bajos menor a 1000 dolares
ingresos mensuales medios mayor a 1000 pero menor a 7000 dolares
ingresos mensuales altos mayor a 7000 pero menor a 20000 dolares
ingresos mensuales elevados mayor a 20000 dolares
"""

#-----entradas
print("bienvenido")

opcionesEscogida = int(input(preguntaOpcion))
while (opcionesEscogida != 4):
    #-----opcion1
    if (opcionesEscogida == 1):
        opcionMoneda = (input(preguntaDivisa))
        if (opcionMoneda == "D"):
            print("no es necesaria la convercion, ya su lista esta en dolares")
            print(listaDolares)
        elif(opcionMoneda == "C"):
            print("mostrando lista en COP")
            print(listaPesos)
        elif(opcionMoneda == "E"):
            print("mostrando lista en euros")
            print(listaEuros)
        else:
            print("el valor ingresado no es valido")
    #-----opcion2
    elif (opcionesEscogida == 2):
        ingresos = float(input(preguntaIngreso))
        if(ingresos <= 1000):
            print("cada mes tienes ingresos bajos")
            print(listaClasificacion)
        elif(ingresos > 1000 and ingresos < 7000 ):
            print("cada mes tienes ingresos medios")
            print(listaClasificacion)
        elif(ingresos >= 7000 and ingresos < 20000):
            print("cada mes tienes ingresos altos")
            print(listaClasificacion)
        else:
            print("cada mes tienes ingresos elevados")
            print(listaClasificacion)
    #-----opcion3
    elif (opcionesEscogida == 3):
        print( "este es el ingreso mayor de la lista : " , max ( listaDolares ))
        print("este es el ingreso menor de la lista : " , min ( listaDolares ))
        print("este es el promedio de lista : " , sum ( listaDolares ) / len ( listaDolares ))
    #-----opcion4
    else:
        print("opcion inexistente")
    opcionesEscogida = int(input(preguntaOpcion))

print("gracias por usar el codigo")

