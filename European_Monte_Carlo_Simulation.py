#!/usr/bin/env python
# coding: utf-8

# In[114]:


#values European call options

#import appropriate libraries
#-----------------------------------------------------------------------------
import numpy as np
import random
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt 
import pandas as pd
plt.style.use('seaborn-whitegrid') 

#import file
#takes in excel file of daily returns of security 
#-----------------------------------------------------------------------------
import xlrd
wb = xlrd.open_workbook('/Users/isaacmartin/Desktop/Python/Files/AAPL.xlsx')
ws = wb.sheet_by_index(0)
data = ws.col_values(0)

#assumptions
#-----------------------------------------------------------------------------
paths = 0
i = 0
stock_price = 130.89 #current stock price
strike_price = 130 #strike price of option
div_rate = np.log(1+.0064)#Continuously compounded dividend rate of stock
r = np.log(1+.0011)#continuously compounded US TB 1-yr risk free rate
t = 1/252
days_to_expiry = 80 #days in whole numbers (ex:not 6.5 days, but 7 days works)
std_dev = .4
adj_stock_price = [stock_price*np.exp(-days_to_expiry*t*div_rate)] #adjusts for PV of dividends
route = []
route.append(adj_stock_price[0])
result_of_sim = []
list_of_call_values = []
counter = 0

#generate stock prices & call values
#-----------------------------------------------------------------------------
def new_tree(x):
    new_price = (1+ random.choice(data)) * x #need randomly chosen movement
    route.append(new_price)

while paths < 1000:
    route = []
    route.append(adj_stock_price[0])
    i = 0
    while i < days_to_expiry: 
        new_tree(route[-1])
        i+=1
    dl = days_to_expiry+1
    time = [*range(0, dl)]
    plt.plot(time, route)
    result_of_sim.append(route[-1])
    paths += 1
    
for x in result_of_sim:
    if strike_price < x:
        payoff = x - strike_price
    else:
        payoff = 0
    list_of_call_values.append(payoff)

#interpret results
#-----------------------------------------------------------------------------
plt.title('Distribution of Stock Prices') #puts labels on graph of simulated trees
plt.xlabel('Time (Days)')
plt.ylabel('Stock Price')

print("--------------------------------------")
print("Stock price distribution:")
df_describe = pd.DataFrame(result_of_sim)
print(df_describe.describe())

#plt.hist(result_of_sim)
#plt.title('Distribution of Stock Prices')
#plt.xlabel('Stock Price')
#plt.ylabel('# times in distribution')

df_describe = pd.DataFrame(list_of_call_values)
print("--------------------------------------")
print("Call value distribution:")
print(df_describe.describe())

#plt.hist(list_of_call_values)
#plt.title('Distribution of Call Values')
#plt.xlabel('Call Value')
#plt.ylabel('# times in distribution')


# In[ ]:





# In[ ]:




