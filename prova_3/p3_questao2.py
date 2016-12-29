# -*- coding: utf-8 -*-

from mpl_toolkits.mplot3d import Axes3D
from scipy.sparse import coo_matrix
from sympy import *
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as spi
import scipy.sparse.linalg as linalg

#X = [0,0,100,100,150,150]
#Y = [0,100,100,50,50,0]

#plt.fill(X,Y, color='r')
#plt.show()
print '\nEscolhendo o número de pontos'
print ' Entre com o número Np de pontos'
Np = np.int16(input('  -->Np = '))
print '\nEntre com os dados da linha da matriz A'
row = map(int, raw_input().split())
print '\nEntre com os dados da coluna da matriz A'
col = map(int, raw_input().split())
print '\nEntre com os dados da matriz A'
data = map(int, raw_input().split())
A = coo_matrix((data, (row, col)), shape=(Np, Np)).toarray()
print (A)
print '\nEntre com a matriz B'
B = map(int, raw_input().split())
X = linalg.spsolve(A,B)
print (X)