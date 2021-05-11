#----- quiz #3
import matplotlib.pyplot as plt
import pandas as pd

#----- punto numero 1

pregunta_snack = "diga un snack que te guste  :"
pregunta_precio = "cuanto vale ese snack  :"
snacks = []
n = 5
while (n>0):
    snack = input(pregunta_snack)
    snacks.append(snack)
    n=n-1

precios = []
n = 5
while (n>0):
    precio = int(input(pregunta_precio))
    precios.append(precio)
    n = n-1
plt.bar (snacks, precios, width = 0.7, color = "r")

plt.title ("snack favorito y su precio")
plt.xlabel ("nombre del snack")
plt.ylabel ("precio del snack")
plt.savefig ("graficosSnacksyPrecio.png")

#----- punto numero 2

pregunta_ciudad = "ingrese su ciudad favorita  :"
pregunta_poblacion = "ingrese la poblacion de la ciudad  :"
ciudades = []
n = 5
while (n>0):
    ciudad = input(pregunta_ciudad)
    ciudades.append(ciudad)
    n = n-1

habitantes = []
n = 5
while (n>0):
    poblacion = int(input(pregunta_poblacion))
    habitantes.append(poblacion)
    n = n-1
plt.bar (ciudad, poblacion, width = 0.7, color = "r")

plt.title ("ciudades favoritas y su poblacion")
plt.xlabel ("nombre de la ciudad")
plt.ylabel ("poblacion de la ciudad")
plt.savefig ("graficosCiudadyPoblacion.png")

#----- punto numero 3

print ("el electrocardiograma es la representacion visual de la actividad electrica del corazon en funcion del tiempo")

ecgData = pd.readcsv ("ecg.csv", encoding = "UTF-8" , header=0,delimiter=";").to_dict()
muestras = list(ecgData["muestra"].values())
voltajes = list(ecgData["valor"].values())
plt.plot(muestras, voltajes)

plt.title ("EKG")
plt.xlabel ("tiempo (Ms)")
plt.ylabel ("voltaje (microvoltios)")
plt.savefig ("cc.png")

plt.show
