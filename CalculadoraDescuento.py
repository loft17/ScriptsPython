#!/usr/bin/python
#
#
# NAME: 	CalculadoraDescuento
# VERSION:	1.1.5
# --------------------------------------------------------------------
#
# email: web@joseromera.net
# url: https://www.joseromera.net
# copyright: All right reserved
#
# --------------------------------------------------------------------

# CUESTIONARIO
precio = float(input("Cual es el precio: "))
descuento = float(input("Porcentaje de descuento: "))
print ("-----------------------------")

# FUNCION
var01 = descuento/100
var02 = precio*var01
resultado = precio-var02

# RESULTADO
print ("El precio final es: ", '%.2f' % resultado)
