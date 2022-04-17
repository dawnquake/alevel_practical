#!/usr/bin/env python
# coding: utf-8

# # Graph Plotting

# ## Relationship Hypothesis and Planning Graph
# 
# After having made several measurement, you will proceed to making a hypothesis about what is the relationship between the independent variable and the dependent variable, as well as what to plot on the graph. Several common relationships are shown below, with the independent variable as $x$ and dependent variable as $y$
# 
# |Relationship    | Name                 | Transform | x-axis | y - axis| Slope | y-intercept (Co - ordinate) | x-axis units | y-axis units | Notes |
# |   ---          | ---                  | ---       | --- | --- | --- | --- | --- | ---| ---|
# | $y = kx$         | Directly proportional| y = kx    | x | y | $k$ | $0$ | x-units | y-units | Must pass origin $(0,0)$ |
# | $y = kx +c$      | Linear| y = kx + c    | x | y | $k$ | $c$ | x-units | y-units |  |
# | $y = k/x$      | Inverse proportional| y = k (1/x)    | 1/x | y|  $k$ | $0$ | $1/x_{unit}$ | y-units |  |
# | $y = k/x +c$      | ???| y = k (1/x) + c    | $k$ | $c$ | 1/x | y |  $1/x_{unit}$ | y-units |  |
# | $y = ax^n$   | ???| ln y = ln a + n ln x    | ln x | ln y |  $n$ | $ln a$ | $ln x_{unit}$ | ln y-units |  |
# | $y = ae^{kx}$ | ???| ln y = ln a + k x    | x | ln y |  $k$ | $ln a$ | $x_{unit}$ | ln y-units |  |

# # Graph Drawing

# 0. Sharpen pencil or use mechanical pencil when drawing graphs to avoid losing marks due to feathering
# 1. When drawing any graph, always have the measured points will span at least half of the graph in both x and y axis!
# 2. x-axis should have the dependent variable with units and y-axis the independent variable with units
# 3. Decide whether your graph should start from (0,0). You might want to make your graph not start from (0,0) if starting from (0,0) prevents you from making the measured points span at least half of the graph
# 4. When drawing data points, use sharp + or x and do NOT use round points. 
# 5. Mark out anomalous/outlier points if there are any, with a circle and an arrow pointing towards passively aggressive "OUTLIER" or "ANOMALY"
# 6. When drawing the best fit line, the best fit line should
#     - NOT include the anomalous/outlier points
#     - NOT have feathering 
#     - HAVE roughly equal number of measured points above and below the best fit line
#     - When the points show a curve, draw a curve, and NOT segmented lines
# 7. Include title, legend. Include error bars if possible
# 

# ## Graph Analysis
# 
# - When finding out gradient or y-intercept (a.k.a the co-ordinate), need to choose points on the best fit line on opposite side of the graph (not include outliers or anomalous points) that span at least half of the graph. Draw a circle around and an arrow to clearly label that these are the chosen points used to find the gradient. 
# - Then draw a big fat right angled triangle with the length of the sides measured clearly shown next to the sides
# - Be very careful about the units on your x-axis and y-axis. For example, on your x-axis, you might have 1 unit for  squares, while on the y-axis, you have 10 units for 5 squares. You need to account for these when finding out the length of the sides of your triangle, which should be in number of units and not number of squares. 
# - You might have to extrapolate a little to the left or right to find the y-intercept (a.k.a the coordinate) or to make some reasonable deductions about what might the relationship between the dependent and independent variable. (i.e. are they directly proportional, inversely proportional etc. )
# - You might have to explain anomalies as either insufficient sth or excessive sth, and do not confuse the two, i.e. attributing and insufficient anomaly with an excessive reason.

# In[ ]:




