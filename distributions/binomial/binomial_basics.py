# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 08:09:23 2017

@author: jdk2py
"""

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

#DISTRIBUCIÓN BINOMIAL

#Supongamos que realizamos 4 experimentos con probabilidad de éxito 1/2
p=0.5
num=4
binomDist = stats.binom(num,p)
print(np.arange(5))
binDistExmp = binomDist.pmf(np.arange(5))
print(binDistExmp)
print(np.sum(binDistExmp))

#Consideremos 6 experimentos con p de éxito 1/2
p=0.5
N=6
binDist = stats.binom(N,p)
#probabilidad de obtener dos éxitos
print(binDist.pmf(2))
#probabilidad de obteber al menos 4 éxitos
print(sum(binDist.pmf(np.arange(4,6+1))))

#coeficientes de (p+q)^4
p=.5
N=4
binomDist = stats.binom(N,p)
binDistExmp = binomDist.pmf(np.arange(5))
print(binDistExmp*2**N)

#Ejemplo de distribución binomial
N,p=100, 0.5
s = np.random.binomial(N,p,1000)
plt.hist(s, bins = np.arange(100+1))
plt.show()
miHist = np.histogram(s, bins = np.arange(100+1))
print(miHist[0])
print(miHist[1])
print(np.mean(s))
print(N*p)
print(np.var(s))
print(N*p*(1-p))