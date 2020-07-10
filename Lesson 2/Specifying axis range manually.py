#!/usr/bin/env python
# coding: utf-8

# ### Importing Modules (Library)

# In[1]:


import matplotlib.pyplot as plt


# ### manual axis (X & Y) assignment - Part 1 

# In[2]:


x_data = [1,2,3,4,5]
y_data = [1, 4, 9, 16, 25]
plt.plot(x_data, y_data, '--r')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axis([0,6,0,30]) # axis range
plt.show()


# ### manual axis (X & Y) assignment - Part 2

# In[3]:


x_data = [1,2,3,4,5]
y_data = [1, 4, 9, 16, 25]
plt.plot(x_data, y_data, '--r')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axis([2,4,5,20]) # axis range
plt.show()


# In[ ]:




