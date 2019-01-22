#!/usr/bin/python
#
#
# NAME: 	TiempoViaje
# VERSION:	1.2.0 
# --------------------------------------------------------------------
#
# email: web@joseromera.net
# url: https://www.joseromera.net
# copyright: All right reserved
#
# --------------------------------------------------------------------

TramosTotales = []

# Recogida de datos
Tramo = int(input('Duracion tramo: '))
while Tramo > 0:
	TramosTotales.append(Tramo)
	Tramo = int(input('Duracion tramo: '))


# 
SumaTramos = sum(TramosTotales)
HorasTotales =  int(SumaTramos / 60)
Horas2Minutos = (60 * HorasTotales)
MinutosTotales = (SumaTramos - Horas2Minutos)

print ("Tiempo total de viaje: ",HorasTotales,":",MinutosTotales," horas",sep="")


