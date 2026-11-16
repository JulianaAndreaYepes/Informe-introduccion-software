##Votos

votosValidos = int(input("Ingrese votos validos: "))
votosPartido = int(input("Ingrese votos de su partido: "))

umbral = (votosValidos*0.03)

if(votosPartido  > umbral):
    print("Tu partido tendra curules")
else:
    print("input(Se quemaron")
