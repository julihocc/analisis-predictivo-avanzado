# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 08:09:23 2017

@author: jdk2py
"""

from scipy import stats
import numpy as np

#DISTRIBUCIÓN BINOMIAL

#coeficientes de (p+q)^4
p=.5
N=4
binomDist = stats.binom(N,p)
binDistExmp = binomDist.pmf(np.arange(5))
print(binDistExmp*2**N)
##[ 1.  4.  6.  4.  1.]