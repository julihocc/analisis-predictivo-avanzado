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
print(df.head())


import matplotlib.pyplot as plt

x=2.5*np.random.randn(100)+1.5
res=.5*np.random.randn(100)+0
ypred=2+.3*x
yact=2+.3*x+res

ymean=np.mean(yact)
yavg=[ymean for i in range(1,len(xlist)+1)]

plt.plot(x,ypred)
plt.plot(x,yact,'ro')
plt.plot(x,yavg)
plt.title('Actual vs Predicted')

df['SSR']=(df['Predicted_Output(ypred)']-ymean)**2
df['SST']=(df['Actual_Output(yact)']-ymean)**2
SSR=df.sum()['SSR']
print("SSR=", SSR)
SST=df.sum()['SST']
print("SST=", SST)
R2 = SSR/SST
print("R2=",R2)
