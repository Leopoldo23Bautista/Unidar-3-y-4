# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:36:26 2020

@author: Leopoldo Bautista
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)
y = x*np.cos(x)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lab DLS')
plt.show()