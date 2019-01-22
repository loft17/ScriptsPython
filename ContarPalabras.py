#!/usr/bin/python
#
#
# NAME: 	Contar palabaras
# VERSION:	1.0.0 
# --------------------------------------------------------------------
#
# email: web@joseromera.net
# url: https://www.joseromera.net
# copyright: All right reserved
#
# --------------------------------------------------------------------

# Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por cuántas letras lo es.

palabra_insert_1 = input('Palabra 1: ')
palabra_insert_2 = input('Palabra 2: ')

palabra_cont_1 = len(palabra_insert_1)
palabra_cont_2 = len(palabra_insert_2)


if palabra_cont_1 > palabra_cont_2:
	resultado = (palabra_cont_1-palabra_cont_2)
	print ('La palabra', palabra_insert_1, 'tiene', resultado, 'letras mas que', palabra_insert_2, '.')
elif palabra_cont_2 > palabra_cont_1:
	resultado = (palabra_cont_2-palabra_cont_1)
	print ('La palabra', palabra_insert_2, 'tiene', resultado, 'letras mas que', palabra_insert_1,)
else:
	print ('La palabra', palabra_insert_1, 'tiene el mismo numero de letras que', palabra_insert_2)
