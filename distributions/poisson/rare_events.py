# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 21:22:03 2017

@author: jdk2py
"""


from scipy import stats

#7.28
#a
N = 2000
p = 0.001
print(stats.binom(N,p).pmf(3))
print(stats.poisson(N*p).pmf(3))
#(b)
print(1-stats.binom(N,p).cdf(2))
print(1-stats.poisson(N*p).cdf(2))