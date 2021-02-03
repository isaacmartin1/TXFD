#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Value of European option at expiration
price = 75
strike = 70

if price > strike:
    payoff = price - strike
else:
    payoff = 0

print("the payoff is", payoff)


#What if you have multiple possible prices for an option
import numpy as np
end_prices = [75, 70, 65, 60]
strike = 70
payoffs = []

for x in end_prices:
    if x > strike:
        payoffs.append(x-70)
    else:
        payoffs.append(0)

print("the average payoff is", np.average(payoffs))


#Same as above but with definition to do calculations
import numpy as np
end_prices = [75, 70, 65, 60]
strike = 70
payoffs = []

def value(x):
    if x > strike:
        payoffs.append(x-70)
    else:
        payoffs.append(0)

for x in end_prices:
    value(x)

print("the average payoff is", np.average(payoffs))




# In[ ]:




