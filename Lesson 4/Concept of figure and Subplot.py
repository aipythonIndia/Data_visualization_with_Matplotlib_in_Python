#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np


# ### Traditional way of plotting multiple lines on the same plot

# In[3]:


t1 = np.arange(0.0, 5.0, 0.1)
y1 = np.sin(2*np.pi*t1)
y2 = np.cos(2*np.pi*t1)
plt.plot(t1, y1, 'r')
plt.plot(t1, y2, 'g')
plt.show()


# ### Create a subplot with 2 row , 1 col and the data

# In[4]:


t1 = np.arange(0.0, 5.0, 0.1)
y1 = np.sin(2*np.pi*t1)
y2 = np.cos(2*np.pi*t1)

plt.figure()

plt.subplot(211)
plt.plot(t1, y1, 'r')

plt.subplot(212)
plt.plot(t1, y2, 'g')

plt.show()


# ### Create a subplot with 1 row , 2 col and the data

# In[5]:


t1 = np.arange(0.0, 5.0, 0.1)
y1 = np.sin(2*np.pi*t1)
y2 = np.cos(2*np.pi*t1)

plt.figure()

plt.subplot(121)
plt.plot(t1, y1, 'r')

plt.subplot(122)
plt.plot(t1, y2, 'g')

plt.show()

