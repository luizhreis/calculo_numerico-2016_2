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

def equacao(temp, tempo):
	return -0.07 * (temp - 20)

i = 1
passo_t = a
passo_y = inicial
while passo_t <= b:
	passo_t += h
	i += 1

te = np.zeros(i)
ye = np.zeros(i)
i = 0
passo_t = a
te[i] = a
ye[i] = inicial
while passo_t <= b:
	passo_t += h
	passo_y += h * equacao(passo_y, passo_t)
	i += 1
	te[i] = passo_t
	ye[i] = passo_y


tempo = np.linspace(a, b, npontos)
y = integ.odeint(equacao, inicial, tempo)

plt.title('EDO e Euler')
plt.plot(tempo, y, 'r-', label='equacao', color='blue')
plt.plot(te, ye, 'r', label='aprox. euler', color='red')
plt.legend(loc='best')
plt.grid(True)
plt.show()
plt.close()
