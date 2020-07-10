#!/usr/bin/env python
# coding: utf-8

# In[7]:


import matplotlib.pyplot as plt
import numpy as np #install using pip ==> pip install numpy


# ## Simple scatter plot

# In[8]:


y1 = np.random.randn(70)
y2 = np.random.randn(70)
# Both y1 and y2 should be of same size
plt.scatter(y1, y2)
plt.show()


# ## Adjust axis, if required

# In[9]:


y1 = np.random.randn(70)
y2 = np.random.randn(70)
plt.scatter(y1,y2)
plt.axis([-3,3, -3, 3])
plt.show()


# ## Specify a common X-axis and assign separate markers for both 

# In[14]:


x = np.arange(70)
y1 = np.random.randn(70)
y2 = np.random.randn(70)
plt.scatter(x, y1, marker ='o', label="y1 with x")
plt.scatter(x, y2, marker ='v', label="y2 with x")
plt.legend(loc = 'upper left')
plt.show()


# ## Specifying colors

# In[16]:


x = np.arange(70)
y1 = np.random.randn(70)
y2 = np.random.randn(70)
plt.scatter(x, y1, marker ='o', c='r')
plt.scatter(x, y2, marker ='v', c='b')
plt.title("This is scatter plot")
plt.show()


# In[ ]:


# apart from this axis label, plot title as well as legends can be added

