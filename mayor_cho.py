#!/usr/bin/env phyton
#-*- coding: utf-8 -*-
num = int(raw_input("introduce un numero positivo para seguir(negativo para acabar): "))
mayor = num
while num >= 0:
	if num > mayor: 
		mayor = num 
	num = int(raw_input("introduce un numero positivo para seguir(negativo para acabar): "))
if mayor < 0:
	print "no valeee"
else:
	print "el mayor es:" +str(mayor)
