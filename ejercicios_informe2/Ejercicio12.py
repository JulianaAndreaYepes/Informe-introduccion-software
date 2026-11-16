#Fruver

dia = input("Ingrese el día de la semana: ").strip().lower()
producto = input("Ingrese el producto: ").strip().lower()
valor = float(input("Ingrese el valor del producto: "))

descuento = 0

if dia == "lunes":
    if producto == "fruver":
        descuento = 30
elif dia == "martes":
    if producto == "carnes":
        descuento = 30
elif dia == "miercoles":
    if producto == "carnes":
        descuento = 15
    elif producto == "fruver":
        descuento = 10
    elif producto == "vinos":
        descuento = 5
elif dia == "jueves":
    if producto == "vinos":
        descuento = 30
elif dia == "viernes":
    if producto == "vinos":
        descuento = 15
    elif producto == "fruver":
        descuento = 10
    elif producto == "carnes":
        descuento = 5

costoTotal = valor - valor * descuento / 100

if costoTotal == int(costoTotal):
    costoTotal = int(costoTotal)

print("Descuento: " + str(descuento) + "%")
print("Costo Total: " + str(costoTotal))
