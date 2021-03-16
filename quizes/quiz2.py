#-----quiz #2

#-----preguntas

preguntaOpcion  = """ Ingrese su opcion de interes
    1. conversion de C a F o K
    2. clasificacion segun temperatura
    3. temperatura mas alta y baja de la lista y cada cuanto se tomo un dato
    4. Salir
"""

valorConversion  = """ LA RESPUESTA DEBE ESTAR EN MAYUSCULA
    C - dejar en celcius
    K - mostrar en Kelvin
    F - mostrar en Farenheit
"""

listaEstados = """ ##### ESTADO DEL PACIENTE SEGUN LA TEMPERATURA #####
menor a 36 grados es hipotermia
entre 36 y 37.5 grados es temperatura normal
mayor a 37.5 grados es fiebre
"""

preguntaTemperatura = " cual es la temperatura del paciente? : "

Temperatura_Corporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]

#-----conversion

listaKelvin = []
for elemento in Temperatura_Corporal :
    conversor = round(elemento + 273.15)
    listaKelvin.append (conversor)
listaFarenheit = []
for elemento in Temperatura_Corporal:
    conversor = round ((elemento * 1.8)+32)
    listaFarenheit.append (conversor)

#-----entradas
print("bienvenido")

opcionesEscogida = int(input(preguntaOpcion))
while (opcionesEscogida != 4):
    #-----opcion1
    if (opcionesEscogida == 1):
        opcionTemperatura = (input(valorConversion))
        if (opcionTemperatura == "C"):
            print("la lista ya se encuentra en Celsius")
            print(Temperatura_Corporal)
        elif(opcionTemperatura == "K"):
            print("se hizo la conversion a grados Kelvin")
            print(listaKelvin)
        elif(opcionTemperatura == "F"):
            print("se hizo la conversion a grados Farenheit")
            print(listaFarenheit)
        else:
            print("valor ingresado invalido, por favor escoga un valor valido")
    #-----opcion2
    elif (opcionesEscogida == 2):
        temperatura = float(input(preguntaTemperatura))
        if(temperatura < 36):
            print("positivo pa hipotermia")
            print(listaEstados)
        elif(temperatura >= 36 and temperatura < 37.5 ):
            print("temperatura normal")
            print(listaEstados)
        else:
            print("positivo pa fiebre")
            print(listaEstados)
    #------opcion3----#
    elif (opcionesEscogida == 3):
        print( "esta es la temperatura mayor de la lista : " , max ( Temperatura_Corporal ))
        print("esta es la temperatura menor de la lista : " , min ( Temperatura_Corporal ))
        print("la temperatura se toma cada : ", len (Temperatura_Corporal ) / 24, "horas")
    #------opcion4-----#
    else:
        print("opcion invalida, escoga una opcion valida")
    opcionesEscogida = int(input(preguntaOpcion))

print("un placer poderles servir")