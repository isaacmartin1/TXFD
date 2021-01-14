#!/usr/bin/env python
# coding: utf-8

# In[107]:


#values american call options
import numpy as np
import random
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
starting_stock_price = [130.89] #price of stock today
strike_price = 131 #strike price of call
div_rate = np.log(1+.0064)#Continuously compounded dividend rate of stock
r = np.log(1+.007)#continuously compounded US TB 1-yr risk free rate
t = 1/225 #incriments, each day is 1 of 252 trading days
days_to_expiry = 400 #trading days to expiry on option
t_left = t*days_to_expiry
route = []
early_exercise = []
route.append(starting_stock_price[0])
result_of_sim = []
list_of_call_values = []
counter = 0
periods_of_routes = []

#generate stock prices & call values
#-----------------------------------------------------------------------------

while paths < 1000:
    route = []
    route.append(starting_stock_price[0])
    t_left = t*days_to_expiry
    days = 1
    i = 0
    while i < days_to_expiry:
        new_price = (1+ random.choice(data)) * route[-1]
        route.append(new_price)
        optimal_exercise = ((strike_price*(1-np.exp(-t_left*r))+1)/(1-np.exp(-t_left*div_rate)))
        days += 1
        if new_price > optimal_exercise: #biggest issue is optimal exercise price gets too low as time goes up
            early_exercise.append(new_price)
            break
        t_left += -1/252
        i+=1
    days_graphed = int(days)
    time = [*range(0, days_graphed)]
    periods_of_routes.append(days)
    x = np.array(time)
    y = np.array(route)
    plt.plot(x, y)
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
plt.title('Distribution of Stock Prices')#puts labels on graph of simulated trees
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

print("")
print("exercised early #:", len(early_exercise))

print("# of days each route took before expiry", periods_of_routes)

#plt.hist(list_of_call_values)
#plt.title('Distribution of Call Values')
#plt.xlabel('Call Value')
#plt.ylabel('# times in distribution')


# In[ ]:




