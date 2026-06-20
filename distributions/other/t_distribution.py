# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 18:56:31 2017

@author: jdk2py
"""
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

def tp(x, nu):
    return stats.t.ppf(x, df=nu)

print(tp(0.05, 9))
print(tp(1-0.05, 9))
