#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as int

N = 500
X = [1, 1, 3, 4, 3, 1]
Y = [1, 3, 4, 2, 0, 1]

xmin = np.amin(X)
xmax = np.amax(X)
ymin = np.amin(Y)
ymax = np.amax(Y)

T = np.linspace(0, 5, N)

tck,u = int.splprep([X, Y], s=0)
spline = int.splev(T, tck)

plt.title('Teste')
plt.plot(X, Y, 'bo', label=' Pontos conhecidos')
plt.plot(spline[0], spline[1], 'r-', label='spline obtida')
plt.legend(loc='best')
plt.grid(True)
plt.axis([xmin - 2, xmax + 2, ymin - 2, ymax + 2])
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.show()
plt.close()
