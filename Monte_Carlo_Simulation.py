#!/usr/bin/env python
# coding: utf-8

# In[76]:


import numpy as np
import random
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt 
import pandas as pd
plt.style.use('seaborn-whitegrid') 

#import file
#-----------------------------------------------------------------------------

#steps to clean data beforehand:
#1. copy adjusted close price data to excel file, starting at cell A1
#2. calculate daily returns in column B
#3. copy & paste as values t column C
#4. Delete Columns A & B
#5. Move column C returns to cell A1, so it takes up column A

import xlrd
wb = xlrd.open_workbook('/Users/isaacmartin/Desktop/Python/Files/AAPL.xlsx')
ws = wb.sheet_by_index(0)
data = ws.col_values(0)

#assumptions
#-----------------------------------------------------------------------------
paths = 0
i = 0
starting_stock_price = [115.05]
strike_price = 115
cc_div_rate = .0146
r = .0012
t = 1/252
days_to_expiry = 63
std_dev = .4
route = []
route.append(starting_stock_price[0])
result_of_sim = []
list_of_call_values = []
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
    pi = (1 + random.choice(data)) * x
    pii = (1 + random.choice(data)) * x
    if strike_price < pi:
        up_payoff = pi - strike_price
    else:
        up_payoff = 0
    if strike_price < pii:
        down_payoff = pii - strike_price
    else:
        down_payoff = 0
    p = (np.exp((r-cc_div_rate)*t)-d)/(u-d)
    call_value = np.exp(-r*t)*(p*up_payoff + (1-p)*down_payoff)
    list_of_call_values.append(call_value)

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




