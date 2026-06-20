#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 03:11:11 2017

@author: jdk2py
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import numpy as np

# Configure data paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
DATA_DIR = os.path.join(REPO_ROOT, 'data')

# Load data
advert = pd.read_csv(os.path.join(DATA_DIR, 'advertising.csv'))
print(advert.head())


model1=smf.ols(formula='Sales~TV',data=advert).fit()

print("params", model1.params)
print("pvalues", model1.pvalues)
print("R2", model1.rsquared)
print("Resumen", model1.summary(), "\n")

sales_pred=model1.predict(pd.DataFrame(advert['TV']))
print("sales_pred.head()\n",sales_pred.head())


advert.plot(kind='scatter', x='TV', y='Sales')
plt.plot(pd.DataFrame(advert['TV']),sales_pred,c='red',linewidth=2)
plt.show()


advert['sales_pred']=0.047537*advert['TV']+7.03
advert['RSE']=(advert['Sales']-advert['sales_pred'])**2
SSD=advert.sum()['RSE']
n = len(advert["Sales"])
RSE=np.sqrt(SSD/(n-2))
print("RSE", RSE)
salesmean=np.mean(advert['Sales'])
print("salesmean", salesmean)
error=RSE/salesmean
print("error", error)
