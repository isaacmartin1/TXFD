#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Print function: anything in quotes is printed
print("hello world")


#Import packages. 
#After importing a package, you can use it. Numpy is a math package, so we use it's sqrt feature
import numpy as np
print("square root of 9 is", np.sqrt(9))


#Assigning a variable
#Here, assign the value of 0 to a. You can see that it's value is 0 when printed
a = 0
print("a is equal to", a)


#Lists
list_of_items = [45, 50, 41, 60]
print("The list of items is:", list_of_items)


#For loop: iterate through each item in a list
for each_variable in list_of_items:
    print(each_variable)

    
#While loop: iterate loop while specified condition is true:
i = 0 
while i < 10:
    print(i)
    i += 1
    

#If statements
Grade = 95
if Grade > 90:
    print("you made an A!")

    
#Else statements: if the "If" statement's value is false, do the "else"
Grade = 80
if Grade > 90:
    print("you made an A!")
else:
    print("B+ or lower received.")
    
    
#Defining & calling a function
def repeater(x):
    print(x, x, x)

repeater(1)


# In[ ]:




