Algoritmo Cambiodemoneda
	
    Definir nombre Como Cadena
    Definir monto, cambio Como Real
    Definir moneda Como Entero
    Definir simbolo Como Caracter
	
    Escribir "Ingrese el nombre cliente"
    Leer nombre
	
    Escribir "Ingrese el monto a cambiar en soles"
    Leer monto
	
    Escribir "Seleccione moneda de cambio"
    Escribir "[1] Dolares [2] Euros"
    Leer moneda
	
    Si moneda = 1 Entonces
        cambio <- monto / 2.35
        simbolo <- '$'
    SiNo
        cambio <- monto / 3.58
        simbolo <- '?'
    FinSi
	
    Escribir "Se cambio en ", simbolo, cambio
	
FinAlgoritmo