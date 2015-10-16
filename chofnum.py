#!/usr/bin/env python
#-*- coding: utf-8 -*-
mayor = 0
num = int(raw_input("introduce un numero positivo para seguir(negativo para acabar): "))
while num >= 0:
	if num > mayor: 
		mayor = num 
	num = int(raw_input("introduce un numero positivo para seguir(negativo para acabar): "))
if mayor == 0:
	print "game over" 
else:
	print "el mayor es: " + str(mayor) #el_mayor
