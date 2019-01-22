#!/usr/bin/python

#
# NAME: 	Celsius2Fahrenheit
# VERSION:	1.1.0 
# --------------------------------------------------------------------
#
# email: web@joseromera.net
# url: https://www.joseromera.net
# copyright: All right reserved
#
# --------------------------------------------------------------------

celsius = float(input('Introduce los grados celsius: '))

resultado = (celsius*1.8+32)

print ('---> ', celsius, 'grados Celsius son:', '%.2f' % resultado, 'grados Fahrenheit')