#!/usr/bin/python
#
#
# NAME: 	Fibonacci
# VERSION:	1.1.0 
# --------------------------------------------------------------------
#
# email: web@joseromera.net
# url: https://www.joseromera.net
# copyright: All right reserved
#
# --------------------------------------------------------------------

a, b = 0, 1
repeticiones = int(input("Hasta donde quiere contabilizar: "))

while b < repeticiones:
	print (b)
	a, b = b, a+b