#!/usr/bin/env python
# coding: utf-8

# In[1]:


#FIN 367 Case-Like. Valuing a Call option
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt 
import pandas as pd
plt.style.use('seaborn-whitegrid') 

#assumptions
#-----------------------------------------------------------------------------
i = 0
stock_price = [115.05]
strike_price = 115
cc_div_rate = .0146
r = .0012
t = 1/252
days_to_expiry = 24
std_dev = .4
u = np.exp((r-cc_div_rate)*t + std_dev*np.sqrt(t))
d = np.exp((r-cc_div_rate)*t - std_dev*np.sqrt(t))
print("u is", u, "d  is", d)
list_of_call_values = []
list_of_prices = []
new_list = []
list_of_prices.append(stock_price[0])
#-----------------------------------------------------------------------------
def new_tree(x):
    up_price = u * x
    down_price = d * x
    new_list.append(up_price)
    new_list.append(down_price)

while i < days_to_expiry: 
    new_list = []
    for x in list_of_prices:
        new_tree(x)
    list_of_prices = []
    list_of_prices = new_list
    i+=1
    print(i)

for x in list_of_prices:
    up_price = u * x
    down_price = d * x
    if strike_price < up_price:
        up_payoff = up_price - strike_price
    else:
        up_payoff = 0
    if strike_price < down_price:
        down_payoff = down_price - strike_price
    else:
        down_payoff = 0
    p = (np.exp((r-cc_div_rate)*t)-d)/(u-d)
    call_value = np.exp(-r*t)*(p*up_payoff + (1-p)*down_payoff)
    list_of_call_values.append(call_value)

#final value
#-----------------------------------------------------------------------------
print("--------------------------------------")
print("Stock price distribution:")
df_describe = pd.DataFrame(list_of_prices)
print(df_describe.describe())


df_describe = pd.DataFrame(list_of_call_values)
print("--------------------------------------")
print("Call value distribution:")
print(df_describe.describe())

plt.hist(list_of_call_values)
plt.title('Distribution of Call Values')
plt.xlabel('Call Value')
plt.ylabel('# times in distribution')


#extra information
#-----------------------------------------------------------------------------
#Delta = (up_payoff-down_payoff)/(up_price-down_price)
#print("Delta is", Delta)

#Beta = -Delta*up_price*np.exp(-r+cc_div_rate)
#print("Beta is", Beta)

#put_value = call_value - stock_price*np.exp(-cc_div_rate*t) + strike_price*np.exp(-r*t)
#print("put value is", put_value)


# In[ ]:




