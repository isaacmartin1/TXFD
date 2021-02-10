#!/usr/bin/env python
# coding: utf-8

# In[41]:


#import  libraries
#-----------------------------------------------------------------------------
import matplotlib.pyplot as plt 


#import file
#takes in excel file of daily returns of security 
#-----------------------------------------------------------------------------
import xlrd
wb = xlrd.open_workbook('/Users/isaacmartin/Desktop/Python/Files/SCHG.xlsx')
ws = wb.sheet_by_index(0)
data = ws.col_values(0)

#stock price distribution
#-----------------------------------------------------------------------------

plt.hist(data, bins = 150)
plt.title("SCHG Returns")
plt.xlabel("% return")
plt.ylabel("Frequency")
plt.show()





# In[ ]:


#normal distribution

