# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 08:09:23 2017

@author: jdk2py
"""

import numpy as np
import matplotlib.pyplot as plt

#Ejemplo de distribución binomial
N =100
p = 0.5
s = np.random.binomial(N,p,1000)
#print s
miHist = np.histogram(s, bins = np.arange(100+1))
#print miHist[0]
#print miHist[1]
me = np.mean(s)
print(me)
mt = N*p
print(mt)
ve = np.var(s); print(ve)
vt = N*p*(1-p); print(vt)
sde = np.sqrt(np.var(s)); print(sde)
sdt = np.sqrt(N*p*(1-p)); print(sdt)

plt.hist(s, bins = np.arange(100+1))
plt.show()

def miFunc(otraLista, p1, p2):
    miLista = []    
    for _ in otraLista:
        if p1-p2 <= _ <= p1+p2:
            miLista.append(_)
    return len(miLista)*1.0

for k in range(1,4+1):
    SDe = miFunc(s, me, k*sde)
    print(SDe/1000)
    SDt = miFunc(s, mt, k*sdt)
    print(SDt/1000)
