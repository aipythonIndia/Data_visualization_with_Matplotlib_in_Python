#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np #install using pip ==> pip install numpy


# ## Plotting categorical data

# ### Plot city population vs age group as a category

# In[2]:


age_group = ['<18','19-30','31-50','51-70', '>70']
total_num = [12, 18, 17, 8, 6]  # value in multiple of 100000
plt.bar(age_group, total_num)
plt.xlabel("Age Group")
plt.ylabel("Population x100000")
plt.title("Population Stats for Bangalore")
plt.show()


# ### Applying various bar properties like color, width, edgecolor

# In[3]:


age_group = ['<18','19-30','31-50','51-70', '>70']
total_num = [12, 18, 17, 8, 6]  # value in multiple of 100000
plt.bar(age_group, total_num, color = 'g', edgecolor= 'r', width =0.4) #default is 0.8
plt.xlabel("Age Group")
plt.ylabel("Population x100000")
plt.title("Population Stats for Bangalore")
plt.show()


# ### Different colors for each bar

# In[4]:


age_group = ['<18','19-30','31-50','51-70', '>70']
total_num = [12, 18, 17, 8, 6]  # value in multiple of 100000
colors = ['r', 'g', 'b', 'c', 'y']
plt.bar(age_group, total_num, color = colors, width =0.4)
plt.xlabel("Age Group")
plt.ylabel("Population x100000")
plt.title("Population Stats for Bangalore")
plt.show()


# In[ ]:




