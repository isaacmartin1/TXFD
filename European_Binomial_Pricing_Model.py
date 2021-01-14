#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Values European call options using binomial pricing model

#import appropriate libraries
#-----------------------------------------------------------------------------
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt 
import pandas as pd
plt.style.use('seaborn-whitegrid') 

#assumptions
#-----------------------------------------------------------------------------
i = 0 #leave this at 0, as it is a counter for later calculations
stock_price = 130.83 #current stock price
strike_price = 131 #strike price
div_rate = np.log(1+.0064)#Continuously compounded dividend rate of stock
r = np.log(1+.0011)#continuously compounded US TB 1-yr risk free rate
t = 1/252 #time incriments. This is one day at a time, out of 252 trading days
days_to_expiry = 2 #number of trading days to expiry
std_dev = .424 #annualized volatility (standard deivation) of option. Just look up "annualized volatility of X stock"
adj_stock_price = [stock_price*np.exp(-days_to_expiry*t*div_rate)] #calc to adjust stock price for PV of dividends
u = np.exp((r-div_rate)*t + std_dev*np.sqrt(t)) #multiplier for how much stock goes up each time
d = np.exp((r-div_rate)*t - std_dev*np.sqrt(t)) #multiplier for how much stock goes down each time
print("u is", u, "d  is", d)
list_of_call_values = []
list_of_prices = []
new_list = []
list_of_prices.append(adj_stock_price[0])

#generate stock prices & call values
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
    if strike_price < x:
        payoff = x - strike_price
    else:
        payoff = 0
    list_of_call_values.append(payoff)

#interpret results
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

#Beta = -Delta*up_price*np.exp(-r+div_rate)
#print("Beta is", Beta)

#put_value = call_value - stock_price*np.exp(-div_rate*t) + strike_price*np.exp(-r*t)
#print("put value is", put_value)


# In[ ]:




