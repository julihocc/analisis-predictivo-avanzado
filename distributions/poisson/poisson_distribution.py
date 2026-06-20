# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 22:44:05 2017

@author: jdk2py
"""

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

def f(x, mu=1):
    return stats.poisson.pmf(x, mu)
    
def F(x, mu=1):
    return stats.poisson.cdf(x, mu)

x1 = np.arange(0,100+1)
plt.plot(x1, f(x1, mu=5), 'bo')
plt.show()

s = np.random.poisson(5,365)
M = np.max(s)
myBins = np.arange(0,M+1)
plt.hist(s, bins = myBins)
plt.show()

print(F(3, mu=5))
print(1 - F(7, mu=5))

for k in range(20):
    print(k, F(k, 5))