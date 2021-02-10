#!/usr/bin/env python
# coding: utf-8

# In[4]:


#import library
import numpy as np


#set assumptions
#counter
i = 0

#standard deviation each day
sigma = .00302

#list prices will be stored in
l = [] #list

#stock price
p = 112


while i < 100:
    p = np.random.normal(1, sigma) * p
    l.append(p)
    i += 1


print(l)
    
    



# In[17]:


#import library
import numpy as np
import matplotlib.pyplot as plt

#set assumptions
#counter
i = 0

#standard deviation each day
sigma = .00302

#list prices will be stored in
l = [] 

#time will be stored in
#needed to set up x axis for graphing
t = []

#stock price
p = 112


while i < 100:
    p = np.random.normal(1, sigma) * p
    l.append(p)
    i += 1
    t.append(i)

    
plt.plot(t, l)
plt.show()

print(l)
    


# In[ ]:





# In[ ]:




