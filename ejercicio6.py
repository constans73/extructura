

"""
Remplazar cada letra de una frase dada por el usuario por la posición que le corresponde en el 
abecedario y mostrar el nuevo string en pantalla. (Los espacios no se remplazan) .
 Ejemplo: frase : 'Hola' salida : 815121 H(8) o(15) l(12) a(1)
 """

abecedario = "abcdefghijklmnopqrstuvwxyz"

frase = input ("Introduce una frase\n")
frase = frase.lower()

tupla = frase.split()

matriz = []

for i in range(len(tupla)):

	palabra = tupla[i]					#sacamos una palabra de una tupla de palbras
	tupla_numeros = []

	for i2 in palabra:
		letra = abecedario.index(i2) + 1		#convertimos la palabra en una tupla en numeros
		tupla_numeros.append(letra)
				
	matriz.append(tupla_numeros)

print (matriz)

						################		VAMOS A QUITAR CORCHETES DE LA TUPLA DE TUPLAS   Y PONER 
						################		ESPACIOS ENTRE LAS PALABRAS CONVERTIDAS A NUMEROS.		

for i3 in range(len(matriz)):

	numeros = matriz[i3]				#   dividimos la tupla de tuplas en una tupla llamada numeros		
	for numero in numeros:				#  elegimos el numero de nuestra tupla y abajo lo imprimimos
		print (numero, end="")			#  con   end=""   no hay saltos de carro
	print(end=" ")						#dejo espacio en blanco entre las palabras convertidas a numeros.
