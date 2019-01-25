#!/usr/bin/python
#
#
# NAME: 	CLEAN
# VERSION:	1.0.0 
# --------------------------------------------------------------------
#
# email: web@joseromera.net
# url: https://www.joseromera.net
# copyright: All right reserved
#
# --------------------------------------------------------------------
#


#Cree un proyecto en Python de una bola mágica 8, que es un juguete utilizado para adivinar o buscar consejo.

#Permitir al usuario introducir su pregunta.
#Mostrar un mensaje en progreso.
#Crea 10/20 respuestas y muestra una respuesta aleatoria.
#Permitir al usuario hacer otra pregunta / consejo o abandonar el juego.

ListaRespuestas = {0:'En mi opinión, sí', 1:'Es cierto', 2:'Es decididamente así', 3:'Probablemente', 4:'Buen pronóstico', 5:'Todo apunta a que sí', 6:'Sin duda', 7:'Sí', 8:'Sí - definitivamente', 9:'Debes confiar en ello', 10:'Respuesta vaga, vuelve a intentarlo', 11:'Pregunta en otro momento', 12:'Será mejor que no te lo diga ahora', 13:'No puedo predecirlo ahora', 14:'Concéntrate y vuelve a preguntar', 15:'No cuentes con ello', 16:'Mi respuesta es no', 17:'Mis fuentes me dicen que no', 18:'Las perspectivas no son buenas', 19:'Muy dudoso'}

from random import randrange

ComandoSalida = 0

while ComandoSalida <= 1:
	
	# Generamos respuesta aleatoria
	NumeroRandom = randrange(21)	

	# Preguntamos usuario
	print ('')
	print ('---------- MENU ---------')
	print ('1.- Realizar una pregunta')
	print ('2.- Salir del programa')
	PreguntaMenu = int(input('Que desea hacer: '))
	print ('')
	
	if PreguntaMenu == 1: # Realiza pregunta
		PreguntaUsuario = input('Formula tu pregunta: ')
		print ('')
		
		print (ListaRespuestas[NumeroRandom])
		
		
		
		
		
		
		
		
		ComandoSalida = 0
		
	if PreguntaMenu == 2: # Respuesta incorrecta
		print ('--> Salimos del programa')
		ComandoSalida = 3
		
	if PreguntaMenu >= 3: 
		print ('--> Respuesta erroena')
		ComandoSalida = 0
	
	
	
	
	
	
	
	