#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import libraries
import numpy as np
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd

#import daily returns
import xlrd
wb = xlrd.open_workbook('/Users/isaacmartin/Desktop/Python/Files/AAPL.xlsx')
ws = wb.sheet_by_index(0)
data = ws.col_values(0)

#fit distribution
std = np.std(data)
mean = np.mean(data)

#assumptions
S = 122.54
K = 123
days = 3
t = 1/252
r = .04

#generate stock prices & call values
p = 0
stock_prices = []
call_values = []

while p < 1000:
    path = [S]
    i = 0
    while i < days: 
        path.append((1+np.random.normal(mean, std))*path[-1])
        i+=1
    plt.plot([*range(0, int(days+1))], path)
    stock_prices.append(path[-1])
    p += 1

for S in stock_prices:
    if S > K:
        P = (S-K)*np.exp(-r*days*t)
    else:
        P = 0
    call_values.append(P)

#interpret results
print("Implied Volatility:", std*np.sqrt(252))
print("Daily standard deviation:", std)
plt.title('Distribution of Stock Prices')
plt.xlabel('Time (Days)')
plt.ylabel('Stock Price')
plt.show()

print("Stock price distribution:")
df_describe = pd.DataFrame(stock_prices)
print(df_describe.describe())
plt.hist(stock_prices)
plt.title('Distribution of Stock Prices')
plt.xlabel('Stock Price')
plt.ylabel('# times in distribution')
plt.show()

df_describe = pd.DataFrame(call_values)
print("Call value distribution:")
print(df_describe.describe())
plt.hist(call_values)
plt.title('Distribution of Call Values')
plt.xlabel('Call Value')
plt.ylabel('# times in distribution')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




