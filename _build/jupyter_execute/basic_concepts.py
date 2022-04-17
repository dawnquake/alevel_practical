#!/usr/bin/env python
# coding: utf-8

# # Basic Concepts in A level Practical

# ## Accuracy vs Precision
# 
# In essence, precision has nothing to do with true value. Precision simply means how close together are the measured data. If the measured data is very close together, then it is precise. 
# 
# Accuracy has everything to with true value. Accurate simply means that the measured value is close to the true value. 
# 
# The following plot has been made to show the difference between precision and accuracy, suggested inputs to precision or accuracy is from 0 to 10. Bigger numbers means more precision/accuracy. 

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
from source import accuracy_vs_precision

accuracy_vs_precision(precision = 10,
                      accuracy = 10,
                      title = 'Precise and Accurate')

accuracy_vs_precision(precision = 10,
                      accuracy = 1,
                      title = 'Precise and Not Accurate')

accuracy_vs_precision(precision = 2,
                      accuracy = 7,
                      title = 'Not Precise but Accurate')

accuracy_vs_precision(precision = 1,
                      accuracy = 1,
                      title = 'Not Precise and Not Accurate')


# In[ ]:





# In[ ]:




