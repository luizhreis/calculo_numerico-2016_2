#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as spi

print 'Entre com o intervalo [a, b]:'
a, b = np.float32(input('a, b = '))
print 'Entre com o numero de pontos para interpolar:'
n_ptos = np.int(input('n = '))
ptos = np.linspace(a, b, n_ptos)
L = 2*np.pi
def x(t):
	return 1-np.cos(L*t)
def y(t):
	return np.sin(2*L*t)
N = 500
T = np.linspace(a, b, N)
X = x(T)
Y = y(T)
m_x = np.amin(X)
M_x = np.amax(X)
f_x = (M_x - m_x)/20.
m_y = np.amin(Y)
M_y = np.amax(Y)
f_y = (M_y - m_y)/20.
ptos_x = x(ptos)
ptos_y = y(ptos)
tck,u = spi.splprep([ptos_x, ptos_y], s=0)
Spl = spi.splev(T, tck)
plt.title('Grafico da funcao e da spline cubica parametrica')
plt.plot(x(T), y(T), 'b-', label='curva parametrica')
plt.plot(ptos_x, ptos_y, 'bo', label=str(n_ptos)+' Pontos na curva')
plt.plot(Spl[0], Spl[1], 'r--', label='spline parametrica')
plt.legend(loc='best')
plt.grid(True)
plt.xticks(np.around([m_x, M_x]))
plt.yticks(np.around([m_y, M_y]))
plt.axis([m_x - f_x, M_x + f_x, 1.6*m_y - f_y, M_y + f_y])
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.show()
plt.close()
