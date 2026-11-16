#Velocidades

velocidad = float(input("Ingrese la velocidad X (km/h): "))

if velocidad <= 30:
    grupo = "zonas escolares (30 km/h)"
    infringe = "Ninguna zona"
elif velocidad <= 60:
    grupo = "vías urbanas (60 km/h)"
    infringe = "Zonas escolares"
elif velocidad <= 80:
    grupo = "vías rurales (80 km/h)"
    infringe = "Zonas escolares y vías urbanas"
elif velocidad <= 100:
    grupo = "rutas nacionales (100 km/h)"
    infringe = "Zonas escolares, vías urbanas y vías rurales"
else:
    grupo = None
    infringe = "Todas las zonas"

if grupo is None:
    print("Tu velocidad supera todos los límites (máximo 100 km/h)")
else:
    print("Tu velocidad cabe en el grupo de: " + grupo)

if infringe == "Ninguna zona":
    print("No estás infringiendo ningún límite")
else:
    print("Estás infringiendo el límite en: " + infringe)
