#!/usr/bin/env python
# coding: utf-8

# In[34]:


#import libraries
import matplotlib.pyplot as plt


#plot pie chart of SCHG assets
labels = 'AAPL', 'AMZN', 'FB','GOOG', 'Other'
percents = [13.06, 8.57, 4, 6.28, 68.09]
fig1, ax1 = plt.subplots()
ax1.pie(percents, labels=labels, autopct='%1.0f%%')
plt.title('Assets as % of SCHG')
plt.show()


#plot last week of AAPL & SCHG prices
AAPL = [143.16, 142.06, 137.09, 131.96, 134.14, 134.99]
x1 = ['Tue', 'Wed', 'Thu', 'Fri', 'Mon', '2nd Tue']
plt.plot(x1, AAPL, label = "AAPL Price")
SCHG = [132.82, 129.28, 130.29, 127.49, 130.74, 132.95]
x2 = ['Tue', 'Wed', 'Thu', 'Fri', 'Mon', '2nd Tue']
plt.title('AAPL vs. SCHG Price')
plt.plot(x2, SCHG, label = "SCHG Price")
plt.legend()
plt.show()




# In[6]:


100-(13.06+8.57+4+6.28)


# In[ ]:




