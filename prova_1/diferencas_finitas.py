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
funtion = np.poly1d(coeficients, 0, variable)
print tr * '-'
print 'Função informada:'
print(np.poly1d(funtion))
print tr * '-'
