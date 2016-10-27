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
coeficients = map(float, s.split())
function = np.poly1d(coeficients, 0, variable)
print 'Informe o ponto x0:'
x0 = np.float32(input())
print tr * '-'
print 'Função informada:'
print(np.poly1d(function))
print tr * '-'

derivada = function.deriv()

N = 50
a = 0
b = N
Ks = np.linspace(a, b, N+1)
# Y = function(X)

H = 2 ** (-Ks)

avancada = (function(x0 + H) - function(x0)) / H
atrasada = (function(x0) - function(x0 - H)) / H
centrada = (function(x0 + H) - function(x0 - H)) / (2 * H)

dy = derivada(x0)

plt.plot(Ks, avancada, 'bo', label='Aprox. avancada', color='blue')
plt.plot(Ks, atrasada, 'bo', label='Aprox. atrasada', color='green')
plt.plot(Ks, centrada, 'bo', label='Aprox. centrada', color='red')
# plt.plot(Ks, dy, 'r-', label='Derivada de f', color='grey') ## PREENCHER COM O VALOR DE dy
# plt.yscale('linear', linthreshy=5*(10**-0.01))
# plt.yscale('symlog', linthreshy=5*(10**-0.01))

plt.title('Teste doido')
plt.legend(loc='best')
plt.grid(True)
plt.show()

# plt.yscale('symlog', linthreshy=0.05)

# y_p1 = function(p1)