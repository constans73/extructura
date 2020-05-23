

#############################    EJERCICIOS 1 Y 2       #############################

"""Dado un diccionario, el cual almacena las calificaciones de un alumno, 
siendo las llaves los nombres de las materia y los valores las calificación, 
mostrar en pantalla el promedio del alumno."""


#A partir del diccionario del ejercicio anterior, mostrar en pantalla la materia con mejor promedio.



calificaciones = {"matematicas":6.5,"ciencia":7.3, "lengua":5.4, "dibujo":6.3, "tecnologia":9.2, "taller":9.6}



promedio = (calificaciones.get("matematicas") + calificaciones.get("ciencia") + calificaciones.get("lengua") + calificaciones.get("dibujo") + calificaciones.get("tecnologia") + calificaciones.get("taller"))/6
print (round (promedio, 2))			#redondeo a dos decimales





####################################################################################################################

tupla_calificaciones = tuple(calificaciones.values())			#he convertido en diccionario en una tupla
resultado = 0

for lector in tupla_calificaciones:
	resultado = lector + resultado								#voy sumando los datos y lo incluyo en resultado
print (round(resultado/len(tupla_calificaciones),2))			#divido los datos entre la longuitud de la tupla y
																# a su vez lo redondeo a 2 decimales



######################			RESPUESTA DE OTRO ALUMNO      ##########################

calificaciones = { 'dibujo': 12, 'calculo': 10, "fisica":14} 
sumatoria = 0 

for valor in calificaciones.values():
    sumatoria += valor

promedio=sumatoria/len(calificaciones)
print("Promedio del alumno es =", promedio)

mejor_promedio=max(zip(calificaciones.values(),calificaciones.keys()))		#HA CREADO UNA MATRIZ
print ("Materia con el mejor promedio es:",mejor_promedio[1])




################################   LO HE INTENTADO MEJORA             ###############################

calificaciones = { 'dibujo': 12, 'calculo': 10, "fisica":14} 
sumatoria = 0 

for valor in calificaciones.values():
    sumatoria += valor

promedio=sumatoria/len(calificaciones)
print("Promedio del alumno es =", promedio)

mejor_promedio=max(calificaciones)									#HE QUITADO LA MATRIZ Y VO,SCA EL MAXIMO EN EL 
print ("Materia con el mejor promedio es:",mejor_promedio)			#DICCIONARIO
print ("y su puntuacion es de ",calificaciones.get(mejor_promedio))

