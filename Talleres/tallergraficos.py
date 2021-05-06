#-----ingresos 2020 mes a mes de una persona
import matplotlib.pyplot as plt
mes = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sept", "oct", "nov", "dic"]
dineroGanado = [850.000, 900.000, 780.000, 820.500, 990.000, 630.000, 880.500, 700.000, 860.900, 500.800]
plt.bar(mes, dineroGanado, width=0.6, color= "r")

plt.title("salarios colombianos mes a mes año 2020")
plt.xlabel("mes del año 2020")
plt.ylabel("ingresos mensuales en COP")

plt.show()
