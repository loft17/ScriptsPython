#!/usr/bin/python
#
#
# NAME: 	AciertaElNumero
# VERSION:	1.0.0 
# --------------------------------------------------------------------
#
# email: web@joseromera.net
# url: https://www.joseromera.net
# copyright: All right reserved
#
# --------------------------------------------------------------------

RangoRandom = int(input('Rango para adivinar: '))	


from random import randrange
NumeroRandom = randrange(RangoRandom)
NumeroIntento = 1

print ('Adivine el numero.')
print ('')

NumeroApuesta = int(input(f'Intento {NumeroIntento}: '))	

while NumeroApuesta != NumeroRandom:
	if NumeroRandom > NumeroApuesta:
		print ('Es mayor que:', NumeroApuesta)
	else:
		print ('Es menor que:', NumeroApuesta)
	
	NumeroIntento = NumeroIntento + 1
	NumeroApuesta = int(input(f'Intento {NumeroIntento}: '))

print (f'Correcto. Adivinaste en {NumeroIntento} intentos.')