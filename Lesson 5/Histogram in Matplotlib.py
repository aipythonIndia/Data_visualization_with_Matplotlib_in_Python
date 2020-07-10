#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# # Histogram

# ### Simplest way to create a histogram

# In[4]:


data = np.random.randn(1000)
h1 = 0.23*data+4
plt.hist(h1)
plt.title("Histogram plot for Random Data", fontsize=12)
plt.show()


# ### Apply bins, alignment and color to histogram

# In[5]:


data = np.random.randn(1000)
h1 = 0.23*data+4
plt.hist(h1, 5, align= 'mid', color = 'm')
plt.title("Histogram plot for Random Data", fontsize=12)
plt.show()


# ### Change histogram orientation

# In[6]:


data = np.random.randn(1000)
h1 = 0.23*data+4
plt.hist(h1, 5, align= 'mid', color = 'm', orientation = 'horizontal')
plt.title("Histogram plot for Random Data", fontsize=12)
plt.show()


# ### Apply Histogram display type and bottom threshold

# In[7]:


data = np.random.randn(1000)
h1 = 0.23*data+4
plt.hist(h1, 5, align= 'mid', color = 'm',histtype = 'step', bottom = 100)
plt.title("Histogram plot for Random Data", fontsize=12)
plt.show()


# ### Displaying values over log scale 

# In[8]:


data = np.random.randn(1000)
h1 = 0.23*data+4
plt.hist(h1, 5, align= 'mid', color = 'm',histtype = 'bar', bottom = 100, log = True)
plt.title("Histogram plot for Random Data", fontsize=12)
plt.show()

