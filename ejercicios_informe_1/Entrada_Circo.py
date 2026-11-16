Algoritmo entradacirco
	
    Definir p Como Real
    Definir edad Como Entero
	
    Escribir "Ingrese el precio de la entrada"
    Leer p
    Escribir "Ingrese la edad del cliente"
    Leer edad
	
    Si edad < 10 Entonces
        p <- p - (p * 0.25)
    FinSi
	
    Escribir "El monto final a pagar es: ", p
	
FinAlgoritmo