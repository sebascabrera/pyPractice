meses = {
    "Enero": 0,
    "Febrero": 0,
    "Marzo": 0,
    "Abril": 0,
    "Mayo": 0,
    "Junio": 0,
    "Julio": 0,
    "Agosto": 0,
    "Septiembre": 0,
    "Octubre": 0,
    "Noviembre": 0,
    "Diciembre": 0
}

for key in meses.keys():
    meses[key] = int(input("Ingrese el sueldo correspondiente a " + key + ": "))

aux = sum(meses.values())
cantidad_meses = len(meses)
promedio = aux / cantidad_meses

print("El promedio de los sueldos es:", promedio)


def tipo_de_sueldo(promedio):
    if promedio <= 300:
        print('El sueldo promedio de Juan corresponde a un "sueldo bajo"')
    elif 300 < promedio <= 900:
        print('El sueldo promedio de Juan corresponde a un "sueldo normal"')
    else:
        print('El sueldo promedio de Juan corresponde a un "sueldo mejor de lo normal"')

tipo_de_sueldo(promedio)
