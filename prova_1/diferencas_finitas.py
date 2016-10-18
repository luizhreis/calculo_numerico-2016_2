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
hs = [0.5, 0.2, 0.05]
for h in hs:
	print function(h)
h = 0.5
N = 1000000
X,h = np.linspace(a, b, N+1, retstep=True);
Y = function(X)
f_h = (b-a)/20.
M = np.amax(Y)
m = np.amin(Y)
f_v = (M-m)/20.
plt.plot(X, Y, 'r-', label='f(' + variable + ')', color='blue')
plt.plot([a,a], [0.,Y[0]], 'k--')
plt.plot([b,b], [0.,Y[-1]], 'k--')
plt.title('Grafico de f(' + variable + ')')
plt.legend(loc='best')
plt.xlabel(variable)
plt.ylabel('f(' + variable + ')')
y_eixo_x = 0.
x_eixo_y = 0.
A = min(0. , a)-f_h
B = max(0. , b)+f_h
Ym = min(0. , m)-f_v
YM = max(0. , M)+f_v
plt.grid(True)
plt.axhline(y=y_eixo_x, xmin=A, xmax=B, c='k')
plt.axvline(x=x_eixo_y, ymin=Ym, ymax=YM, c='k')
plt.axis([A, B, Ym, YM])
plt.show()