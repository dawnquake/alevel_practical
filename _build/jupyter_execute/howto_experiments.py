#!/usr/bin/env python
# coding: utf-8

# # Howto Experiment 
# 
# ## Experiment Tips
# 
# - Read to within half the value of the fine line division on the scale, i.e. a thermometer where is smallest interval is 1 C should be read to 0.5 C. There is only two modes, between the fine line division, and on the fine line division. When stating the uncertainty of the reading, if it is direct reading, then the uncertainty is always half of the fine line division. However, if you add, subtract, multiply or divide between several readings, then the uncertainty might be different from a direct reading. See the calculate uncertainty part
# 
# - Fair spread of reading, generally do uniform reading, but you might be able to justify more concentrated measurement around any point of change of particular interest (color change)
# 
# ## Experiment Design
# 
# 1. Identify the hypothesis, the independent variable, the dependent variable and the control variable
# 2. How to vary the independent variable?
# 3. How to measure the dependent variable?
# 4. How to control any other key variable?
# 5. What are the apparatus used?
# 
#     - Draw and sketch the experiment setup
#     - Make sure that apparatus is large enough to fit, but not ridiculously large compared to amount of substance. For example, small volume are best with pipette or burette, while large volumes are best with measuring cylinder
#     - You can always note that if you are using a small apparatus, you will have larger percentage errors
#     - If you are making subjective judgment (i.e. when does a color change) note that that this is a source of error and note that subjective judgment means you cannot measure to high precision or accuracy. 
# 
# 6. Record all the steps as if you were doing the experiment in chronological order, and give special notice to what are the sources of error during the experiment, and ways to solve these sources of error. Especially judge what is the largest source of error. Always say that you will repeat the experiment several times to seek to remove random error. 
# 7. Note down all sources of hazard and the safety precautions you will take to prevent these hazards. Write these in the format of do something to protect/prevent/avoid something bad. Some examples are provided below
# 
#     - wear goggles to protect against fumes
#     - wear gloves when handling sharp objects
#     - use safety screen to protect against strong light
#     - stabilize apparatus to prevent toppling
#     - sand tray under heavy weight to prevent falling on feet
#     - switch off current when not in use to prevent overheating
# 
# 8. Provide a sketch of the table columns used to record the result of the experiment
# 
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
# 

# ## Example: Measuring the mass of reactants and product
# 
# We have reactant 1 and reactant 2 and we want to react the reactants to get the product, and under how does mass change
# 
# 1. Measure the mass of empty instrument 1
# 2. Measure the mass of instrument 1 with reactant 1
# 3. Measure the mass of empty instrument 2
# 4. Measure the mass of instrument 2 with reactant 2
# 5. Pour reactant 1 in instrument 1 into reactant 2 in instrument 2 (if solid, might need water to rinse to ensure all is transferred, thus have to also measure the amount of water added)
# 6. Record mass after the reaction between reactant 1 and reactant 2

# In[ ]:




