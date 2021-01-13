#!/usr/bin/env python
# coding: utf-8

# In[89]:


import numpy as np
import random
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt 
import pandas as pd
plt.style.use('seaborn-whitegrid') 

#import file
#-----------------------------------------------------------------------------

#takes in excel file of daily returns of security 

import xlrd
wb = xlrd.open_workbook('/Users/isaacmartin/Desktop/Python/Files/AAPL.xlsx')
ws = wb.sheet_by_index(0)
data = ws.col_values(0)

#assumptions
#-----------------------------------------------------------------------------
paths = 0
i = 0
starting_stock_price = [128.80]
strike_price = 131
cc_div_rate = .0146
r = .0012
t = 1/252
days_to_expiry = 3
std_dev = .424
route = []
route.append(starting_stock_price[0])
result_of_sim = []
list_of_call_values = []
counter = 0
#data = [-.05, .05, 0, .1, -.4] #to be replaced by the file
#-----------------------------------------------------------------------------
def new_tree(x):
    new_price = (1+ random.choice(data)) * x #need randomly chosen movement
    route.append(new_price)

while paths < 1000:
    route = []
    route.append(starting_stock_price[0])
    i = 0
    while i < days_to_expiry: 
        new_tree(route[-1])
        i+=1
    #graph the route here & add new route each time through, to get monte-carlo visualized
    result_of_sim.append(route[-1])
    paths += 1
    
for x in result_of_sim:
    if strike_price < x:
        payoff = x - strike_price
    else:
        payoff = 0
    list_of_call_values.append(payoff)

#final value
#-----------------------------------------------------------------------------
print("--------------------------------------")
print("Stock price distribution:")
df_describe = pd.DataFrame(result_of_sim)
print(df_describe.describe())

plt.hist(result_of_sim)
plt.title('Distribution of Stock Prices')
plt.xlabel('Stock Price')
plt.ylabel('# times in distribution')

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




