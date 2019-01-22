#!/usr/bin/python
#
#
# NAME: 	TablaMultiplicar
# VERSION:	1.0.0 
# --------------------------------------------------------------------
#
# email: web@joseromera.net
# url: https://www.joseromera.net
# copyright: All right reserved
#
# --------------------------------------------------------------------

numero = int(input('Ingrese un numero: '))
repeticion = 1

while repeticion < 11:
	resultado = (numero*repeticion)
	print (numero, 'x', repeticion, '=', resultado)
	repeticion = (repeticion+1)
