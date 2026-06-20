#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 17:53:21 2017

@author: jdk2py
"""

from scipy import stats
import numpy as np

M = np.array([[68,52,90],[28,37,35],[96,89,125]])
totalFila = np.sum(M, axis=1)

xx = totalFila[0]
xy = totalFila[1]
total = totalFila[2]

E = [M[2]*xx/total, M[2]*xy/total]
print("E=",E)
O = [M[0],M[1]]
print("O=",O)

def desv(e,o):
    return (e-o)**2/e

desv = np.vectorize(desv)

print("desv(E,O)=",desv(E,O))
chi2 = np.sum(desv(E,O), axis=None)

print("chi2 %.4f" % (chi2))

nu = 6-1

def F(x):
    return stats.chi2(nu).cdf(x)
def iF(p):
    return stats.chi2(nu).ppf(p)


valorp = 1 - F(chi2)
print("valor p =", valorp)

b = 0.05

print("Con un nivel de significación: "+str(b))
if valorp > b:
    print("La hipotesis nula se acepta")
else:
    print("La hipótesis nula se rechaza")
    
print(iF(1-0.05))