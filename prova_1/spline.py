#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as spi

from numpy.random import rand

L = 2*np.pi
print 'Entre com o intervalo [a, b]:'
a, b = np.float32(input('a, b = '))
print 'Entre com o numero de pontos para interpolar:'
n = np.int(input('n = '))
U = np.linspace(a, b, n)
f_h = (b - a)/20.
A = a - f_h
B = b + f_h
def f(t):
	return np.sin(2*np.pi*t)
N = 300
X = np.linspace(a, b, N)
fX = f(X)
fU = f(U)
tck = spi.splrep(U, fU)
spl3X = spi.splev(X, tck)
R = np.append(fX, spl3X)
m_y = np.amin(R)
M_y = np.amax(R)
f_v = (M_y - m_y)/20.
u = 2*m_y - f_v
v = M_y + f_v
Lbl = 'n = ' + str(n) + ' pontos sobre f(x)'
plt.plot(X, fX, 'b-',  label='f(X)')
plt.plot(U, fU, 'bo', label=Lbl)
plt.plot(X, spl3X, 'r--', label='spline cubica')
plt.title('Grafico da funcao e da spline cubica')
plt.legend(loc='best')
plt.grid(True)
plt.xticks((a, b))
plt.axis([A,B,u,v])
plt.axhline(y=0.,color='k')
plt.axvline(x=0.,color='k')
plt.show()
plt.close()

