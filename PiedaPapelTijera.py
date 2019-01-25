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
##
## Piedra:
## Papel:
## Tijera: 

from random import randrange

print ('')
#print ('Para elegir PIEDRA escriva una z')
#print ('Para elegir PAPEL escriva una x')
#print ('Para elegir TIJERA escriva una c')
print ('Para terminar escriba una e')
print ('')

ComandoSalida = 0
AciertosUsuario = 0
AciertosMaquina = 0
EmpatesJugada = 0

while ComandoSalida <= 1:
	
	# Generamos Cara-o-Cruz
	NumeroRandom = randrange(3)	
	
	if NumeroRandom == 0:
		SeleccionMaquina = 'z'
	elif NumeroRandom == 1:
		SeleccionMaquina = 'x'
	elif NumeroRandom == 2:
		SeleccionMaquina = 'c'

	# Preguntamos Cara-o-Cruz
	SeleccionMano = input('Piedra (z), Papel (x), Tijera (c): ')
	
	#
	# Modificamos la entrada a minuscula
	SeleccionMano = SeleccionMano.lower()
	
	
	#
	# Usuario Selecciono PIEDRA
	if SeleccionMano == 'z' and SeleccionMaquina == 'z':
		print ('Empate')
		EmpatesJugada = EmpatesJugada + 1
	
	if SeleccionMano == 'z' and SeleccionMaquina == 'x': 
		print ('Perdiste')
		AciertosMaquina = AciertosMaquina + 1
		
	if SeleccionMano == 'z' and SeleccionMaquina == 'c': 
		print ('Ganaste')
		AciertosUsuario = AciertosUsuario + 1
		
	#
	# Usuario Selecciono PAPEL
	if SeleccionMano == 'x' and SeleccionMaquina == 'z':
		print ('Ganaste')
		AciertosUsuario = AciertosUsuario + 1
	
	if SeleccionMano == 'x' and SeleccionMaquina == 'x': 
		print ('Empate')
		EmpatesJugada = EmpatesJugada + 1
		
	if SeleccionMano == 'x' and SeleccionMaquina == 'c': 
		print ('Perdiste')
		AciertosMaquina = AciertosMaquina + 1
		
	#
	# Usuario Selecciono TIJERA
	if SeleccionMano == 'c' and SeleccionMaquina == 'z':
		print ('Perdiste')
		AciertosMaquina = AciertosMaquina + 1
	
	if SeleccionMano == 'c' and SeleccionMaquina == 'x': 
		print ('Ganaste')
		AciertosUsuario = AciertosUsuario + 1
		
	if SeleccionMano == 'c' and SeleccionMaquina == 'c': 
		print ('Empate')
		EmpatesJugada = EmpatesJugada + 1
		
	#
	# Salimos de la aplicacion y mostramos resultado
	elif SeleccionMano == 'e':
		print ('')
		print ('Acertaste:', AciertosUsuario, '- Perdiste:', AciertosMaquina, '- Empates:', EmpatesJugada)
		ComandoSalida = 2