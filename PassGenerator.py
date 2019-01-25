#!/usr/bin/python
#
#
# NAME: 	PassGenerator
# VERSION:	1.0.1 
# --------------------------------------------------------------------
#
# email: web@joseromera.net
# url: https://www.joseromera.net
# copyright: All right reserved
#
# --------------------------------------------------------------------
#

import random 

LetrasHabiles = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?+-/"


NumeroCaracteres = int(input('Cuantos caracteres quiere que tenga: '))
NuevaPassword = ''.join(random.sample(LetrasHabiles,NumeroCaracteres))

print (NuevaPassword)

