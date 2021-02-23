# quiz numero 1
#-----constantes-----#
MENSAJE_BIENVENIDA = "buen dia dr y dra"
PREGUNTA_TRIGLICERIDOS = "cual es el nivel exacto de trigliceridos del paciente?  :"

#-----entradas al codigo
print(MENSAJE_BIENVENIDA)
print("#"*15, "test trigliceridos", "#"*15)
trigliceridos = float(input(PREGUNTA_TRIGLICERIDOS))
isOptimoTrigliceridos = trigliceridos < 150
IsSobreElNivelOptimoTrigliceridos = trigliceridos >= 150 and trigliceridos < 200
IsAltoTrigliceridos = trigliceridos >= 200 and trigliceridos < 500
IsMuyAltoTrigliceridos = trigliceridos >= 500

resultado = ""

if(isOptimoTrigliceridos):
    print("el nivel de trigliceceridos indica un resultado optimo")
elif(IsSobreElNivelOptimoTrigliceridos):
    print("el nivel de trigliceridos indica que el resultado esta sobre el nivel optimo")
elif(IsAltoTrigliceridos):
    print("el nivel de trigliceridos indica un resultado alto")
else:
    print("el nivel de trigliceridos indica un resultado muy alto")

print(resultado)

#test de homocisteina
print("#"*15, "test homocisteina", "#"*15)

#-----constante
PREGUNTA_HOMOCISTEINA = "cual es el nivel exacto de homocisteina del paciente?  :"
MENSAJE_DESPEDIDA = "gracias por tu labor"

#-----entradas al codigo
homocisteina = float(input(PREGUNTA_HOMOCISTEINA))
isOptimoHomocisteina = homocisteina >= 2 and homocisteina <= 15
isSobreElNivelOptimoHomocisteina = homocisteina > 15 and homocisteina <= 30
isAltoHomocisteina = homocisteina > 30 and homocisteina <= 100
isMuyAltoHomocisteina = homocisteina > 100

resultado = ""

if(isOptimoHomocisteina):
    print("el nivel de Homocisteina indica un resultado optimo")
elif(isSobreElNivelOptimoHomocisteina):
    print("el nivel de Homocisteina indica un resultado sobre el nivel optimo")
elif(isAltoHomocisteina):
    print("el nivel de Homocisteina indica un resultado alto")
else:
    print("el nivel de Homocisteina indica un resultado muy alto")

print(resultado)

print(MENSAJE_DESPEDIDA)