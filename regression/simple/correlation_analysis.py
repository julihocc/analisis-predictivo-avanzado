#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 12:01:07 2017

@author: jdk2py
"""

import os
import pandas as pd
import numpy as np

# Configure data paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
DATA_DIR = os.path.join(REPO_ROOT, 'data')

# Load data
advert = pd.read_csv(os.path.join(DATA_DIR, 'advertising.csv'))
print(advert.head())

advert["dX*dY"] = ( advert["TV"] - np.mean(advert["TV"])) * ( advert["Sales"] - np.mean(advert["Sales"]))
advert["dX**2"] = ( advert["TV"] - np.mean(advert["TV"])) ** 2 
advert["dY**2"] = ( advert["Sales"] - np.mean(advert["Sales"])) ** 2 

sxy = advert.sum()["dX*dY"]
sxx = advert.sum()["dX**2"]
syy = advert.sum()["dY**2"]

r = sxy/np.sqrt(sxx*syy)
print(r)