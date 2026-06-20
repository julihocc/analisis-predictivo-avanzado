#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:39:01 2017

@author: jdk2py
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# Configure data paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
DATA_DIR = os.path.join(REPO_ROOT, 'data')

# Load data
advert = pd.read_csv(os.path.join(DATA_DIR, 'advertising.csv'))

plt.plot(advert['TV'],advert['Sales'],'ro')
plt.title('TV vs Sales')
plt.show()

plt.plot(advert['Radio'],advert['Sales'],'ro')
plt.title('Radio vs Sales')
plt.show()

plt.plot(advert['Newspaper'],advert['Sales'],'ro')
plt.title('Newspaper vs Sales')
plt.show()