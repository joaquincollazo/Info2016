# d) Disene una funcion que permita el ingreso de dos numeros 
# naturales j y h e imprima jh utilizando solo la operacion 
# multiplicacion.

def numeros(j,h,acumulador=0,cont=1):
	acumulador=j
	while cont<h:
		cont=cont+1
		acumulador=acumulador*j
		print acumulador

numeros(2,5)