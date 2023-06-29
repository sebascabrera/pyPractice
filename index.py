meses = {
    "Enero": 0,
    "Febrero":0,
    "Marzo":0,
    "Abril":0,
    "Mayo":0,
    "Juio":0,
    "Julio":0,
    "Agosto":0,
    "Septiembre":0,
    "Octubre":0,
    "Noviembre":0,
    "Diciembre":0
}

for key in meses.keys():
    meses[key] = int(input("Ingrese el sueldo correspondiente a " + key + ": "))
    print (meses)