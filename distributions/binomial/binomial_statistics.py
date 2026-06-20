# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 08:09:23 2017

@author: jdk2py
"""

from scipy import stats
import numpy as np

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