# c) Disene una funcion que dado un numero natural m,
# si es par imprima los m primeros naturales pares
# y si es impar a la inversa.
def numero(n):
	if(n%2==0):
		while n>1:
			n=n-1
			if(n%2==0):
				print n
	elif(n%2!=0):
		while n>1:
			n=n-1
			if(n%2!=0):
				print n
			
numero(15)