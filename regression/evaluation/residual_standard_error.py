#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 00:37:36 2017

@author: jdk2py
"""

import pandas as pd
import numpy as np

np.random.seed(1234)

x=2.5*np.random.randn(100)+1.5
res=.5*np.random.randn(100)+0
ypred=2+.3*x
yact=2+.3*x+res
xlist=x.tolist()
ypredlist=ypred.tolist()
yactlist=yact.tolist()
df=pd.DataFrame({'Input_Variable(X)':xlist,'Predicted_Output(ypred)':ypredlist,'Actual_Output(yact)':yactlist})

ymean=np.mean(yact)
yavg=[ymean for i in range(1,len(xlist)+1)]

import matplotlib.pyplot as plt

xmean=np.mean(df['Input_Variable(X)'])
ymean=np.mean(df['Actual_Output(yact)'])
df['betan']=(df['Input_Variable(X)']-xmean)*(df['Actual_Output(yact)']-ymean)
df['xvar']=(df['Input_Variable(X)']-xmean)**2
betan=df.sum()['betan']
betad=df.sum()['xvar']
beta=betan/betad
alpha=ymean-beta*xmean
print(beta,alpha)

df['ymodel']=beta*df['Input_Variable(X)']+alpha

df['SSR']=(df['ymodel']-ymean)**2
df['SST']=(df['Actual_Output(yact)']-ymean)**2
SSR=df.sum()['SSR']
SST=df.sum()['SST']
R2 = SSR/SST
print("R2(modelo)=", R2)

plt.plot(x,ypred)
plt.plot(x,df['ymodel'], "b")
plt.plot(x,yact,'ro')
plt.plot(x,yavg)
plt.title('Actual vs Predicted vs Model')

n = len(df['Input_Variable(X)'])
df['SSD']=(df['Actual_Output(yact)']-df['ymodel'])**2
SSD=df.sum()['SSD']
RSE=np.sqrt(SSD/(n-2))

print(df.head())
print(RSE)


