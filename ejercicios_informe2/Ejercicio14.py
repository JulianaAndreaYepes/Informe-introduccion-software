# Ejercicio 14 - While: menú de 5 productos y precio del producto solicitado.
# Precios de ejemplo (el enunciado no los da).
opcion = 0

while opcion != 6:
    print("\n--- MENÚ DE PRODUCTOS ---")
    print("1. Arroz")
    print("2. Leche")
    print("3. Huevos")
    print("4. Pan")
    print("5. Café")
    print("6. Salir")

    opcion = int(input("Seleccione un producto: "))

    if opcion == 1:
        print("Arroz: $4500")
    elif opcion == 2:
        print("Leche: $3800")
    elif opcion == 3:
        print("Huevos: $12000")
    elif opcion == 4:
        print("Pan: $2500")
    elif opcion == 5:
        print("Café: $9000")
    elif opcion == 6:
        print("Hasta luego")
    else:
        print("Opción no válida")
