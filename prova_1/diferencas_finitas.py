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

h = 0.5
N = 1000000
p1 = ((b-a)/2)+a
p2 = p1 + h
y_p1 = function(p1)
y_p2 = function(p2)

X = np.linspace(a, b, N)#, retstep=True)
Y = function(X)
alpha = (y_p2 - y_p1)/(p2 - p1)
secante = alpha * (X - p1) + y_p1
delta = (alpha * (0 - p1) + y_p1) - ((function(0 + h) - function(0))/h)
derivative = ((function(X + h) - function(X))/h) + delta
# d = function.deriv()
# derivative = d(X)

print y_p1, y_p2
print (function(0+h)-function(0))/h
print function.deriv()
print function.r

plt.plot(p1, y_p1, 'bo', color='red')
plt.plot(p2, y_p2, 'bo', color='red')
plt.plot(X, Y, 'r-', label='f(' + variable + ')', color='blue')
plt.plot(X, secante, 'r-', label='reta secante', color='red')
plt.plot(X, derivative, 'r-', label='reta tangente', color='green')
plt.legend(loc='best')
plt.grid(True)
plt.show()

# hs = [0.5, 0.2, 0.05]
# for h in hs:
# 	print function(h)
# h = 0.5
# N = 1000000
# X,h = np.linspace(a, b, N, retstep=True);
# Y1 = function(X)
# Y2 = np.tan(X)
# f_h = (b-a)/20.
# M = np.amax(Y1)
# m = np.amin(Y1)
# f_v = (M-m)/20.
# plt.plot(X, Y1, 'r-', label='f(' + variable + ')', color='blue')
# plt.plot(X, Y2, 'r-', label='tangente', color='green')
# plt.plot([a,a], [0.,Y1[0]], 'k--')
# plt.plot([b,b], [0.,Y1[-1]], 'k--')
# plt.title('Grafico de f(' + variable + ')')
# plt.legend(loc='best')
# plt.xlabel(variable)
# plt.ylabel('f(' + variable + ')')
# y_eixo_x = 0.
# x_eixo_y = 0.
# A = min(0. , a)-f_h
# B = max(0. , b)+f_h
# Ym = min(0. , m)-f_v
# YM = max(0. , M)+f_v
# plt.grid(True)
# plt.axhline(y=y_eixo_x, xmin=A, xmax=B, c='k')
# plt.axvline(x=x_eixo_y, ymin=Ym, ymax=YM, c='k')
# plt.axis([A, B, Ym, YM])
# plt.show()