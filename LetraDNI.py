#!/usr/bin/python
#
#
# NAME: 	LetraDNI
# VERSION:	1.0.0 
# --------------------------------------------------------------------
#
# email: web@joseromera.net
# url: https://www.joseromera.net
# copyright: All right reserved
#
# --------------------------------------------------------------------

# TABLA LETRA-RESTO
letra = {0: "T", 1:"R", 2:"W", 3:"A", 4:"G", 5:"M", 6:"Y", 7:"F", 8:"P", 9:"D", 10:"X", 11:"B", 12:"N", 13:"J", 14:"Z", 15:"S", 16:"Q", 17:"V", 18:"H", 19:"L", 20:"C", 21:"K", 22:"E"}

# PREGUNTA
numero_input = int(input("Cual es su numero de dni: "))

# FUNCION
resto_dni = numero_input%23

# RESULTADO
print ('Su DNI completo es:', numero_input,(letra[resto_dni]))