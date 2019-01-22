#!/usr/bin/python
#
#
# NAME: 	VendingMachine
# VERSION:	1.0.4 
# --------------------------------------------------------------------
#
# email: web@joseromera.net
# url: https://www.joseromera.net
# copyright: All right reserved
#
# --------------------------------------------------------------------

NumeroDeMoneda, DineroInsertado = 1, 0
Moneda10, Moneda20, Moneda50, Moneda100, Moneda200 = 10, 20, 50, 100, 200


# --------------------------------------------------------------------
# SELECCION PRODUCTO
# --------------------------------------------------------------------
print ('')
print ('############################')
print ('#                          #')
print ('# A - CocaCola:     160€   #')
print ('# B - Agua:          50€   #')
print ('# C - Sandwich:     240€   #')
print ('#                          #')
print ('############################')
print ('')

ProductoSeleccionado = input('Elija producto: ')

if ProductoSeleccionado in 'abc':
	if ProductoSeleccionado in 'a':
		PrecioSeleccion = 160
	if ProductoSeleccionado in 'b':
		PrecioSeleccion = 50
	if ProductoSeleccionado in 'c':
		PrecioSeleccion = 240



# --------------------------------------------------------------------
# INSERTAR MONDEAS
# --------------------------------------------------------------------	
	print ('')
	print ('############################')
	print ('#                          #')
	print ('#    MONEDAS COMPATIBLES   #')
	print ('#      200, 100, 50, 10    #')
	print ('#                          #')
	print ('############################')
	print ('')
	
	print ('::: Ingrese sus monedas:')
	
	PrecioSeleccionWhile = PrecioSeleccion - 1	
	
	while DineroInsertado <=  PrecioSeleccionWhile:	
		MonedaInsertada = int(input(f'Moneda {NumeroDeMoneda}: '))
		if MonedaInsertada == 10:
			DineroInsertado = MonedaInsertada + DineroInsertado
			NumeroDeMoneda = NumeroDeMoneda + 1
		elif MonedaInsertada == 5:
			DineroInsertado = MonedaInsertada + DineroInsertado
			NumeroDeMoneda = NumeroDeMoneda + 1
		elif MonedaInsertada == 20:
			DineroInsertado = MonedaInsertada + DineroInsertado
			NumeroDeMoneda = NumeroDeMoneda + 1
		elif MonedaInsertada == 50:
			DineroInsertado = MonedaInsertada + DineroInsertado
			NumeroDeMoneda = NumeroDeMoneda + 1
		elif MonedaInsertada == 100:
			DineroInsertado = MonedaInsertada + DineroInsertado
			NumeroDeMoneda = NumeroDeMoneda + 1
		elif MonedaInsertada == 200:
			DineroInsertado = MonedaInsertada + DineroInsertado
			NumeroDeMoneda = NumeroDeMoneda + 1
		else:
			print ('Moneda no reconocida')
		
	DineroDevolver = DineroInsertado - PrecioSeleccion



# --------------------------------------------------------------------
# DEVOLUCION CAMBIO
# --------------------------------------------------------------------
	print ()
	print ('::: Dinero a devolver:', DineroDevolver)
	while 0 <= DineroDevolver:
	
		if DineroDevolver >= Moneda200:
			print ('Moneda devuelta: ', Moneda200, '€')
			DineroDevolver = (DineroDevolver - Moneda200)
	
		if DineroDevolver >= Moneda100:
			print ('Moneda devuelta: ', Moneda100, '€')
			DineroDevolver = (DineroDevolver - Moneda100)
	
		if DineroDevolver >= Moneda50:
			print ('Moneda devuelta: ', Moneda50, '€')
			DineroDevolver = (DineroDevolver - Moneda50)

		elif DineroDevolver >= Moneda20:
			print ('Moneda devuelta: ', Moneda20, '€')
			DineroDevolver = (DineroDevolver - Moneda20)
	
		elif DineroDevolver >= Moneda10:
			print ('Moneda devuelta: ', Moneda10, '€')
			DineroDevolver = (DineroDevolver - Moneda10)	
			
		elif DineroDevolver <= 0:
			break


else:
	print ('El producto seleccionado no se encuentra disponible')


