#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

tr = 50
print tr * '='
print 'Informe a variável: (O padrão é x)'
variable = None
variable = raw_input()
if not variable:
	variable = 'x'
print 'Informe as constantes do polinômio na ordem decrescente de seu maior grau: (Por exemplo 2 5 4)'
s = raw_input()
coeficients = map(int, s.split())
function = np.poly1d(coeficients, 0, variable)
print 'Informe o intervalo [a, b]'
a, b = np.float32(input('a, b = '))
print tr * '-'
print 'Função informada:'
print(np.poly1d(function))
print tr * '-'

# h = 0.5
hs = [0.5, 0.2, 0.05]
N = 1000000
p = 0.0000000000001
p1 = ((b-a)/2)+a
y_p1 = function(p1)
X = np.linspace(a, b, N)
Y = function(X)
beta = (function(p1 + p) - function(p1)) / p
tangente = beta * (X - p1) + y_p1
plt.plot(X, Y, 'r-', label='f(' + variable + ')', color='blue')
plt.plot(X, tangente, 'r-', label='reta tangente', color='green')
plt.plot(p1, y_p1, 'bo', color='red')
colors = ['orange', 'pink', 'red']
i = 0
for h in hs:
	p2 = p1 + h
	y_p2 = function(p2)
	alpha = (y_p2 - y_p1)/(p2 - p1)
	secante = alpha * (X - p1) + y_p1
	plt.plot(p2, y_p2, 'bo', color=colors[i])
	plt.plot(X, secante, 'r-', label='reta secante, h = ' + str(h), color=colors[i])
	i = i + 1

plt.title('Aproximacao para a derivada')
plt.legend(loc='best')
plt.grid(True)
plt.show()
