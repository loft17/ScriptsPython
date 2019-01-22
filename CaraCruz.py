#!/usr/bin/python
#
#
# NAME: 	Cara-o-Cruz 
# VERSION:	2.1.1 
# --------------------------------------------------------------------
#
# email: web@joseromera.net
# url: https://www.joseromera.net
# copyright: All right reserved
#
# --------------------------------------------------------------------

# NOTAS:  
# Cara es 1
# Cruz es 0

from random import randrange

print ('')
print ('Para elegir CARA escriva una c')
print ('Para elegir CRUZ escriva una x')
print ('Para terminar escriba una e')
print ('')

ComandoSalida = 0
AciertosUsuario = 0
AciertosMaquina = 0

while ComandoSalida <= 1:
	
	# Generamos Cara-o-Cruz
	NumeroRandom = randrange(2)	
	if NumeroRandom == 1:
		CaraCruz = 'c'
	else:
		CaraCruz = 'x'

	# Preguntamos Cara-o-Cruz
	SeleccionMoneda = input('Cara o Cruz: ')
	
	#
	# Modificamos la entrada a minuscula
	SeleccionMoneda = SeleccionMoneda.lower()
	
	# Aqui viene la magia
	if SeleccionMoneda == 'c' and CaraCruz == 'c':
		print ('Acertaste')
		AciertosUsuario = AciertosUsuario + 1
		
	if SeleccionMoneda == 'c' and CaraCruz == 'x':
		print ('Perdiste')
		AciertosMaquina = AciertosMaquina + 1
		
	if SeleccionMoneda == 'x' and CaraCruz == 'x':
		print ('Acertaste')
		AciertosUsuario = AciertosUsuario + 1
		
	if SeleccionMoneda == 'x' and CaraCruz == 'c':
		print ('Perdiste')
		AciertosMaquina = AciertosMaquina + 1

	#
	# Salimos de la aplicacion
	elif SeleccionMoneda == 'e':
		print ('')
		print ('Acertaste:', AciertosUsuario, 'Fallaste:', AciertosMaquina)
		ComandoSalida = 2