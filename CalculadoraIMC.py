#!/usr/bin/python

#
#
# NAME: 	MasaCorporal
# VERSION:	1.0.1 
# --------------------------------------------------------------------
#
# email: web@joseromera.net
# url: https:-www.joseromera.net
# copyright: All right reserved
#
# --------------------------------------------------------------------

# RECOGIDA DE DATOS
altura = int(input('Cuanto mides, en cm: '))
peso = float(input('Cuanto pesas, en kg: '))
print ('')
print ('')

# OPERACION
altura_m = (altura/100)
altura_cuadrado = (altura_m*altura_m)

imc = (peso/altura_cuadrado)

# RESULTADO
if imc < 16:
	print ('Tu IMC es de:', '%.2f' % imc, '- Infrapeso: Delgadez Severa')

if 16 <= imc <= 16.99:
	print ('Tu IMC es de:', '%.2f' % imc, '- Infrapeso: Delgadez moderada')

if 17 <= imc <= 18.49:
	print ('Tu IMC es de:', '%.2f' % imc, '- Infrapeso: Delgadez aceptable')

if 18.50 <= imc <= 24.99:	
	print ('Tu IMC es de:', '%.2f' % imc, '- Peso Normal')

if 25.00 <= imc <= 29.99:	
	print ('Tu IMC es de:', '%.2f' % imc, '- Sobrepeso')

if 30.00 <= imc <= 34.99:	
	print ('Tu IMC es de:', '%.2f' % imc, '- Obeso: Tipo I')

if 35.00 <= imc <= 40.00:
	print ('Tu IMC es de:', '%.2f' % imc, '- Obeso: Tipo II')

if imc > 40.00:
	print ('Tu IMC es de:', '%.2f' % imc, '- Obeso: Tipo III')