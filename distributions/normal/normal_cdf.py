# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 21:05:15 2017

@author: jdk2py

Obtenido de Haslwnat
"""

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

mu = 3.5
sigma = 0.76
nd = stats.norm(mu, sigma)

x = np.arange(mu - 4*sigma,mu + 4*sigma,0.01)
y = nd.cdf(x)

fig, ax = plt.subplots()
plt.plot(x, y, 'r', linewidth=2)
plt.ylim(ymin=0)

for k in range(1,5):
    print(nd.cdf(mu+k*sigma)-nd.cdf(mu-k*sigma))