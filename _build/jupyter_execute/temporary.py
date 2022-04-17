#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import matplotlib.pyplot as plt
import math

x = np.linspace(0, 10, 1000)
y = np.floor(x)

plt.style.use('dark_background')
plt.plot(x, y)
plt.show()

