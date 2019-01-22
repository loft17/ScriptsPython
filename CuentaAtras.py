#!/usr/bin/python
#
#
# NAME: 	CuentraAtras
# VERSION:	1.0.0 
# --------------------------------------------------------------------
#
# email: web@joseromera.net
# url: https://www.joseromera.net
# copyright: All right reserved
#
# --------------------------------------------------------------------
#

from datetime import datetime, time
import time


def FechaDiferenciaEnSegundos(Fecha1, Fecha2):
	CuentaAtras = Fecha2 - Fecha1
	return CuentaAtras.days * 24 * 3600 + CuentaAtras.seconds
	
	
def DiasHorasMinutosSegundosDesdeSegundos(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)


FechaSalida = datetime.strptime('2019-03-15 21:30:00', '%Y-%m-%d %H:%M:%S')
Ahora = datetime.now()

print ("Quedan: %d dias, %d horas, %d minutos, %d segundos" % DiasHorasMinutosSegundosDesdeSegundos(FechaDiferenciaEnSegundos(Ahora, FechaSalida)))

