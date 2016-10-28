#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

# polinomio 1 1 1 1 -47 18
# PONTO 0.813

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

difcentrada = np.array(centrada)
difavancada = np.array(avancada)
difatrasada = np.array(atrasada)
difcentrada[:] = [value - dy for value in difcentrada]
difavancada[:] = [value - dy for value in difavancada]
difatrasada[:] = [value - dy for value in difatrasada]

fig = plt.figure(figsize=(16, 12))

graf1 = fig.add_subplot(221)
graf1.plot(Ks, avancada, 'bo', label='Aprox. avancada', color='blue')
graf1.plot(Ks, atrasada, 'bo', label='Aprox. atrasada', color='green')
graf1.plot(Ks, centrada, 'bo', label='Aprox. centrada', color='red')
#graf1.ylim([-38,-40])
graf1.legend(loc='best')
graf1.grid(True)
graf1.set_title('Teste doido')

graf2 = fig.add_subplot(222)
graf2.plot(Ks, avancada, 'bo', label='Aprox. avancada', color='blue')
graf2.plot(Ks, atrasada, 'bo', label='Aprox. atrasada', color='green')
graf2.plot(Ks, centrada, 'bo', label='Aprox. centrada', color='red')
graf2.set_ylim([-45,-30])
graf2.legend(loc='best')
graf2.grid(True)
graf2.set_title('Teste doido')

graf3 = fig.add_subplot(223)
graf3.plot(Ks, avancada, 'bo', label='Aprox. avancada', color='blue')
graf3.plot(Ks, atrasada, 'bo', label='Aprox. atrasada', color='green')
graf3.plot(Ks, centrada, 'bo', label='Aprox. centrada', color='red')
graf3.set_ylim([-40,-38])
graf3.legend(loc='best')
graf3.grid(True)
graf3.set_title('Teste doido')

graf4 = fig.add_subplot(224)
graf4.plot(Ks, difavancada, 'bo', label='Dif. avancada', color='blue')
graf4.plot(Ks, difatrasada, 'bo', label='Dif. atrasada', color='green')
graf4.plot(Ks, difcentrada, 'bo', label='Dif. centrada', color='red')
graf4.set_yscale('symlog')
graf4.legend(loc='best')
graf4.grid(True)
graf4.set_title('Teste doido')

# plt.plot(Ks, dy, 'r-', label='Derivada de f', color='grey') ## PREENCHER COM O VALOR DE dy
# plt.yscale('linear', linthreshy=5*(10**-0.01))
# plt.yscale('symlog', linthreshy=5*(10**-0.01))

plt.show()

# y_p1 = function(p1)