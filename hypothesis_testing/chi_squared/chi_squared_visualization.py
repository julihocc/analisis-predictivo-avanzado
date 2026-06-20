#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 21:36:11 2017

@author: jdk2py
"""

from scipy.stats import chi2
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_palette("husl")
fig, ax = plt.subplots(1, 1)

for df in range(2,15+1):
    x = np.linspace(chi2.ppf(0.01, df),chi2.ppf(0.99, df), 100)
    ax.plot(x, chi2.pdf(x, df), label='chi2 pdf')