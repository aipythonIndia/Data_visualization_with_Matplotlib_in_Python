#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# # Pie Chart

# ### Simplest way to plot a pie chart

# In[2]:


percent_result = [12, 42, 20, 18, 8]
sub = ['Math','Phy','Chem','Bio','IT']

plt.pie(percent_result, labels = sub)
plt.show()


# ### Poping out or focusing region(s) of Pie

# In[6]:


percent_result = [12, 42, 20, 18, 8]
sub = ['Math','Phy','Chem','Bio','IT']

plt.pie(percent_result,  explode = (0,0.1,0.1,0,0), labels = sub)
plt.show()


# ### Displaying shadow in pie chart

# In[7]:


percent_result = [12, 42, 20, 18, 8]
sub = ['Math','Phy','Chem','Bio','IT']

plt.pie(percent_result,  explode = (0,0,0.1,0,0), labels = sub, shadow =  True)
plt.show()


# ### Displaying portion percentage on each part

# In[10]:


percent_result = [12, 42, 20, 18, 8]
sub = ['Math','Phy','Chem','Bio','IT']

plt.pie(percent_result,  explode = (0,0,0.1,0,0), labels = sub, autopct='%1.0f%%')
plt.show()


# In[ ]:




