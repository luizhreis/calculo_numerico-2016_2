#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from mpl_toolkits.mplot3d import Axes3D
from sympy import *
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as spi

print 'É necessário um domínio D = [a, b] × [c, d]'
print 'Informe o intervalo [a, b]:'
a, b = np.float32(input('a, b = '))
#a = -10
#b = 10
print 'Informe o intervalo [c, d]:'
c, d = np.float32(input('c, d = '))
#c = -10
#d = 10
print 'Informe a expressão f(t, y) tal que f:D -> R'
expr_f = raw_input('f(y,t) = ')
#print 'Informe os pontos (t0, u0) e (t1, v1)'

def fun(t, y):
	#return np.sin(np.sqrt(x**2+y**2))/np.sqrt(x**2+y**2+0.1);
	return eval(expr_f)
	# return x**2 + y**2
	# return (1-(x**2+y**3))*np.exp(-(x**2+y**2)/2)

n = 500
nc = 100
qniveis=0.2

fig = plt.figure(figsize=(16, 12))
sup1 = fig.add_subplot(221, projection='3d')
X = np.linspace(a, b, n)
Y = np.linspace(d, c, n)
XV = np.linspace(a, b, nc)
YV = np.linspace(d, c, nc)
X, Y = np.meshgrid(X, Y)
zs = np.array([fun(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)
zmin = np.amin(Z)
zmax = np.amax(Z)
zsv  = np.array([fun(x,y) for x,y in zip(np.ravel(XV), np.ravel(YV))])
ZV = zsv.reshape(XV.shape)
#U = XV#(XV*np.cos(np.sqrt(XV**2+YV**2))/np.sqrt(XV**2+YV**2)*np.sqrt(XV**2+YV**2+0.1))-(XV*np.sin(np.sqrt(XV**2+YV**2))/((XV**2+YV**2+0.1)**(3/2)))
#V = YV#(YV*np.cos(np.sqrt(XV**2+YV**2))/np.sqrt(XV**2+YV**2)*np.sqrt(XV**2+YV**2+0.1))-(YV*np.sin(np.sqrt(XV**2+YV**2))/((XV**2+YV**2+0.1)**(3/2)))
U, V = np.meshgrid(XV, YV, sparse=False)
values = fun(U,V)
UN, VN = np.gradient(values)
#vel = np.sqrt(U**2 + V**2)
#UN = U/vel
#VN = V/vel

sup1.plot_surface(X, Y, Z)

sup1.set_xlabel('X Label')
sup1.set_ylabel('Y Label')
sup1.set_zlabel('Z Label')
# sup1.set_title('Superficie')

graf2 = fig.add_subplot(222)
im = graf2.imshow(Z,cmap=mpl.cm.RdBu)
mpl.cset = graf2.contour(Z,np.arange(zmin,zmax,qniveis),linewidths=2,cmap=mpl.cm.Set2)
graf2.clabel(mpl.cset,inline=True,fmt='%1.1f',fontsize=10)
plt.colorbar(im) # adding the colobar on the right
graf2.set_title('Curvas de nivel')

campo = fig.add_subplot(223)
plt.quiver(U,V, UN, VN,color='Teal', headlength=5)
#plt.quiver(X, Y, UN, VN, color='Teal', headlength=5)
campo.set_title('Campo de vetores')

plt.show()


# n_ptos = np.int(input('n = '))
# ptos = np.linspace(a, b, n_ptos)
# L = 2*np.pi
# def x(t):
# 	return 1-np.cos(L*t)
# def y(t):
# 	return np.sin(2*L*t)
# N = 500
# T = np.linspace(a, b, N)
# X = x(T)
# Y = y(T)
# m_x = np.amin(X)
# M_x = np.amax(X)
# f_x = (M_x - m_x)/20.
# m_y = np.amin(Y)
# M_y = np.amax(Y)
# f_y = (M_y - m_y)/20.
# ptos_x = x(ptos)
# ptos_y = y(ptos)
# tck,u = spi.splprep([ptos_x, ptos_y], s=0)
# Spl = spi.splev(T, tck)
# plt.title('Grafico da funcao e da spline cubica parametrica')
# plt.plot(x(T), y(T), 'b-', label='curva parametrica')
# plt.plot(ptos_x, ptos_y, 'bo', label=str(n_ptos)+' Pontos na curva')
# plt.plot(Spl[0], Spl[1], 'r--', label='spline parametrica')
# plt.legend(loc='best')
# plt.grid(True)
# plt.xticks(np.around([m_x, M_x]))
# plt.yticks(np.around([m_y, M_y]))
# plt.axis([m_x - f_x, M_x + f_x, 1.6*m_y - f_y, M_y + f_y])
# plt.axhline(y=0, color='k')
# plt.axvline(x=0, color='k')
# plt.show()
# plt.close()
