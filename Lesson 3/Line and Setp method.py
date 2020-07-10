#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np #install using pip ==> pip install numpy


# ## Line and setp methods

# ### Recap of the line plot

# In[4]:


x = np.arange(10)
y1 = [1, 9, 7, 10, 3, 16, 2, 20, 5, 22]
y2 = [11, 22, 7, 1, 14, 6, 8, 2, 15, 3]
plt.plot(x, y1, '--r', linewidth = 4)
plt.plot(x, y2, '--b', linewidth = 3)
plt.show()


# ### Assign plots to lines variable and apply individual settings

# In[5]:


x = np.arange(10)
y1 = [1, 9, 7, 10, 3, 16, 2, 20, 5, 22]
y2 = [11, 22, 7, 1, 14, 6, 8, 2, 15, 3]
lines = plt.plot(x, y1, '--r', x, y2, '-b')
plt.show()


# ### Use setp method to apply bulk settings using single statement

# In[7]:


x = np.arange(10)
y1 = [1, 9, 7, 10, 3, 16, 2, 20, 5, 22]
y2 = [11, 22, 7, 1, 14, 6, 8, 2, 15, 3]
lines = plt.plot(x, y1, x, y2)
plt.setp(lines, color='g', linewidth=5)
plt.show()

