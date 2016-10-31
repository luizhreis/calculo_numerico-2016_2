import scipy as sc
import scipy.sparse as sparse
import scipy.sparse.linalg
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt

print 'Informe o tamanho L da barra:'
L = np.float32(input())
 
N = 100
 
h = 1/(N+1.0)

k = h/2

x = np.linspace(0, L, N+2)
x = x[1:-1]

u = np.transpose(np.mat(10*np.sin(np.pi*x)))

data = np.ones((3, N))
data[1] = -2*data[1]
diags = [-1,0,1]
D2 = sparse.spdiags(data,diags,N,N)/(h**2)

I = sparse.identity(N)

A = (I -k/2*D2)
b = ( I + k/2*D2 )*u
u = np.transpose(np.mat( sparse.linalg.spsolve( A,  b ) ))

plt.plot(x, u, 'r-', color='blue')
plt.show()
