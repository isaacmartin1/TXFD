#!/usr/bin/env python
# coding: utf-8

# In[36]:


import matplotlib.pyplot as plt
import numpy as np

values = [1,12,365]
t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = 1

for x in values:
    n = x
    y = []
    for t in time:
        y.append((1+r/n)**(n*t))
    plt.plot(time,y)

#list_of_e = []
#for t in time:
#    list_of_e.append(np.exp(r*t))
#plt.plot(time, list_of_e)

plt.title("Compound Interest on Initial Deposit")
plt.xlabel("Time (Years)")
plt.ylabel("$'s'")


# In[35]:





# In[12]:





# In[ ]:




