#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# ### Generate data and customize it

# In[3]:


y = np.random.normal(loc=0.5, scale=0.4, size=1000)  #loc= mean and scale = Std Deviation

y[(y > 0) & (y < 1)]
y.sort()

x = np.arange(len(y))
plt.plot(x,y)


# ### Plotting symmetric log |  Y scale

# In[4]:


plt.plot(x, (y - y.mean()))
plt.yscale('symlog', linthreshy=0.01)
plt.title('This is a symmetric log', fontsize = 14)
plt.grid(True)


# ### Plotting on logit scale

# In[5]:


plt.plot(x, y)
plt.yscale('logit')
plt.title('A logit plot', fontsize=14)
plt.grid(True)


# In[ ]:




