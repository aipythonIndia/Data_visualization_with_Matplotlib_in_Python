#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[3]:


r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r


# ### Create a separate axe and put a subplot

# In[4]:


ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_rmax(2) # outer radial limit


# ### Set the number of Ticks

# In[5]:


ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2]) # to set the radial ticks


# ### Change the orientation of Tick lable

# In[7]:


ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2]) # to set the radial ticks
ax.set_rlabel_position(180)


# ### Adding Title to the plot

# In[8]:


ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2]) # to set the radial ticks

ax.set_title("A line plot on a polar axis", fontsize=14)
plt.show()


# In[ ]:




