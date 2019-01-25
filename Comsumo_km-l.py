#!/usr/bin/python
#
#
# NAME: 	Consumo Km/h
# VERSION:	1.0.0 
# --------------------------------------------------------------------
#
# email: web@joseromera.net
# url: https://www.joseromera.net
# copyright: All right reserved
#
# --------------------------------------------------------------------
#

DistanciaRecorrida = float(input('Introduce los kilometros recorridos: '))
ConsumoCombustible = float(input('Introduce los litros usados: '))

ConsumoKilometroLitro =  ConsumoCombustible / DistanciaRecorrida
Consumo100km = ConsumoKilometroLitro * 100

print ('Cada kilometro gasto: ', '%.2f' % ConsumoKilometroLitro)
print ('Litros a los 100km: ', '%.2f' % Consumo100km)