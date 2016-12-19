#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integ

print 'Informe o intervalo [a, b]'
a, b = np.float32(input('a, b = '))
print 'Informe o numero de pontos'
npontos = np.int32(input('n = '))
print 'Informe o valor inicial'
inicial = np.float32(input('f(t0) = '))
print 'Informe o passo para a aproximacao de euler'
h = np.float32(input('h = '))

def equacao(vc, t):
	v = 12
	r = 0.5
	c = 2
	return (v-vc)/(r*c)
	# return (vc**2)+(t**2)

tempo = np.linspace(a, b, npontos)
y = integ.odeint(equacao, inicial, tempo)
e = np.zeros(len(tempo))
e[0] = inicial
for i in range(1, len(tempo)):
	e[i] = e[i-1] + equacao(e[i-1], 0)*h

plt.title('Teste')
plt.plot(tempo, y, 'r-', label='valor', color='blue')
plt.plot(tempo, e, 'r', label='aprox. euler', color='red')
plt.legend(loc='best')
plt.grid(True)
plt.show()
plt.close()
