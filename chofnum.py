#!/usr/bin/env phyton
#-*- coding: utf-8 -*-
mayor = 0
entretenido = True
while entretenido:
	num = int(raw_input('mete un numero positivo (si te aburres mete un negativo y terminas):'))
		if num < 0:
			entretenido = False
		elif num > mayor:
			mayor = num
			
print "el mayor del chorro números es" +str(mayor)
