#!/usr/bin/env python
# coding: utf-8

# # Basic Concepts in A level Practical

# ## Independent, Dependent and Control Variables
# 
# What is the independent variable, the dependent variable and the control variable depends on the question asked. For example, for the question "How does temperature affect the rate of reaction?"
# 
# Temperature is the independent variable. When you do the experiment you will change temperature a little in every reaction to see how does the rate of reaction change with temperature.
# 
# Rate of reaction is the dependent variable because rate of reaction is measured to judge the effect of changing temperature, the independent variable. 

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


# ## Vocabulary
# 
# Often in chemistry practical, they will give chemicals with scary names that you have never seen before. Ignore the scariness of the name, and simply focus on what ions the chemical contain, or what descriptive term was used for the chemical (i.e. strong acid, strong base, strong oxidizer etc.). Chemical reactions are determined not by the scariness of the name, but by the structure of the chemical compound. 
# 
# | Bad | Good | Why |
# | --- | --- | --- |
# | - or None or nothing | no visible or observable change | obvious |
# | proves, disproves | supports, does not support the hypothesis | Given the experimental conditions you have, it is not possible for you to prove or disprove, but only to say if the experiment result support or not support the hypothesis |
# 
# 
# When really not know, bullshit reasonably. 

# ## Uncertainty 
# 
# There are two ways to express uncertainty, either as an absolute uncertainty or as percentage uncertainty. You should master how to flawlessly interchange between them. 
# 
# - In absolute uncertainty, the uncertainty is expressed as $\pm$ number. 
# - In percentage uncertainty, the uncertainty is expressed as $\pm 5\%$ 
# 
# It should be obvious from the examples how to convert from absolute uncertainty to percentage uncertainty and vice versa
# 
# |Absolute Uncertainty | Percentage Uncertainty |
# | --- | --- |
# | $1\pm 0.2$ | $1 \pm 20 \%$|
# | $5\pm 0.2$ | $5 \pm 4 \%$|
# 
# Often, you will have to do math with values having some uncertainty. These operations include addition, subtraction, division and multiplication. 
# 
# - When doing addition or subtraction, you should always use absolute uncertainty. The uncertainty of the result will be the sum of the absolute uncertainties NOT the sum of the percentage uncertainty.
# 
# - When doing multiplication and division, you should always percentage uncertainty. The uncertainty of the result will be the sum of the percentage uncertainties NOT the sum of absolute uncertainty.
# 
# Examples for addition and subtraction of absolute and percentage uncertainty
# 
# $$
# (5 \pm 1) + (7 \pm 2) = (12 \pm 3)
# $$
# 
# $$
# (7 \pm 2) - (6 \pm 1) = (1 \pm 3)
# $$
# 
# $$
# (5 \pm 20\%) + (10 \pm 10\%) = (5 \pm 1) + (10 \pm 1) = (15 \pm 2)
# $$
# 
# $$
# (20 \pm 10\%) - (15 \pm 20\%) = (20 \pm 2) - (15 \pm 3)  = (5 \pm 5)
# $$
# 
# Example for multiplication and division of absolute and percentage uncertainty
# 
# $$
# (5 \pm 1) * (8 \pm 2) = (5 \pm 20\%) * (8 \pm 25\%) = (40 \pm 45\%)
# $$
# 
# $$
# (16 \pm 4) / (4 \pm 2) = (16 \pm 25\%) / (4 \pm 50\%) = (4 \pm 75%)
# $$
# 
# $$
# (5 \pm 20\%) * (10 \pm 10\%) = (50 \pm 30\%)
# $$
# 
# $$
# (20 \pm 10\%) / (15 \pm 20\%) = (0.75 \pm 30\%)
# $$
# 
# Another uncertainty that you will not likely encounter will be uncertainty for logarithm, i.e. if we have $(x \pm \Delta x)$ then how what will it become if we do $\ln$ on $x$?
# 
# Well it becomes 
# 
# $$
# \frac{\ln(x + \Delta x) + \ln(x - \Delta x)}{2} \pm \frac{\ln(x + \Delta x) - \ln(x - \Delta x)}{2}
# $$
# 
# You should know how to change uncertainties to error bars on graphs

# In[ ]:




