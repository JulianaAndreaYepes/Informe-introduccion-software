Proceso postulantes
	
    Definir sexo Como Cadena
    Definir edad Como Entero
    Definir categoria Como Cadena
	
    Escribir "Ingrese el sexo del postulante"
    Leer sexo
	
    Escribir "Ingrese la edad del postulante"
    Leer edad
	
    Si sexo = "Femenino" Entonces
		
        Si edad < 23 Entonces
            categoria <- "FA"
        SiNo
            categoria <- "FB"
        FinSi
		
    SiNo
		
        Si edad < 25 Entonces
            categoria <- "MA"
        SiNo
            categoria <- "MB"
        FinSi
		
    FinSi
	
    Escribir "La categoria del postulante es: ", categoria
	
FinProceso