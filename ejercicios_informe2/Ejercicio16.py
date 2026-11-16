# Ejercicio 16 - For: números pares entre 0 y n, 10 por renglón.
n = int(input("Ingrese un número n: "))

contador = 0  # cuántos números van en el renglón actual

for i in range(0, n + 1, 2):
    print(i, end=" ")
    contador += 1

    if contador == 10:
        print()          # salto de línea
        contador = 0

print()  # cierra el último renglón si quedó incompleto
