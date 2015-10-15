#!/usr/bin/env phyton
#-*- coding: utf-8 -*-
mayor = 0
aburrido = False
while not aburrido >0:
	num= int(raw_input('mete un numero positivo (si te aburres mete un negativo)'))
		if num < 0:
			aburrido = True
		elif num > mayor:
			mayor = num
			
print "el mayor del chorro números es" +str(mayor)
