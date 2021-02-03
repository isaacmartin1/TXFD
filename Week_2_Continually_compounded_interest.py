#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import math


# time only doing 50 years
t = range(50)
#intrest rate
r = .02
# number of coumpunds per year
n = 1

## just graphing stuff
y = [];
for time in t:
    #we add the amount of money after x years to a list so it can be graphed on teh y axis vs time
    y.append(math.pow(1*(1+(r/n)),n*time))

# setting the axes at the centre

# plot the function
plt.plot(t,y, 'g')
plt.title("stonks")
plt.xlabel("years")
plt.ylabel("that Money")


# In[46]:



def difftime(number):
    t = range(50) 
    #intrest rate
    r = .3
    # number of coumpunds per year
    n = number
    print(n)
    ## just graphing stuff
    y = [];
    for time in t:
        #we add the amount of money after x years to a list so it can be graphed on teh y axis vs time
        y.append(math.pow(1*(1+(r/n)),n*time))
    plt.plot(t,y)

values = [1,12,365]

for x in values:
    difftime(x)
# plot the function

plt.title("stonks")
plt.xlabel("years")
plt.ylabel("that Money")


# In[50]:


high = [10,1000,10000]
for x in high:
    difftime(x)

t = range(50)    
y = []
for time in t:
    #we add the amount of money after x years to a list so it can be graphed on teh y axis vs time
    y.append(np.exp(.3 * time))
plt.plot(t,y)

