#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 22:38:10 2017

@author: jdk2py
"""

from scipy.stats import chi2

def F(x, df=1):
    return chi2.cdf(x, df)

def iF(x, df=1):
    return chi2.ppf(x, df)

beta = 0.05
print(iF(1-beta))
##3.84145882069

beta = 0.01
print(iF(1-beta))
##6.63489660102