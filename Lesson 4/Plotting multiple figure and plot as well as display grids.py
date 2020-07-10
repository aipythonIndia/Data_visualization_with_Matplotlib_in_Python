#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
import numpy as np


# # Figures and Subplot

# ### Creating two figures without any data

# In[7]:


# t1 = np.arange(0.0, 5.0, 0.1)
# y1 = np.sin(2*np.pi*t1)
# y2 = np.cos(2*np.pi*t1)

plt.figure(1)
plt.figure(2)

plt.show()


# ### Filling data in these subplots

# In[8]:


t1 = np.arange(0.0, 5.0, 0.1)
y1 = np.sin(2*np.pi*t1)
y2 = np.cos(2*np.pi*t1)

plt.figure(1)
plt.subplot(121)
plt.title("Plot 1")
plt.plot(t1, y1, 'r')
plt.subplot(122)
plt.title("Plot 2")
plt.plot(t1, y2, 'g')

plt.figure(2)
plt.subplot(121)
plt.title("Plot 3")
plt.plot(t1, y2, 'k')
plt.subplot(122)
plt.title("Plot 4")
plt.plot(t1, y1, 'm')

plt.show()


# ### Display GRID in the plot

# In[9]:


t1 = np.arange(0.0, 5.0, 0.1)
y1 = np.sin(2*np.pi*t1)
y2 = np.cos(2*np.pi*t1)

plt.figure(1)
plt.subplot(121)
plt.title("Plot 1")
plt.plot(t1, y1, 'r')
plt.grid(True)

plt.subplot(122)
plt.title("Plot 2")
plt.plot(t1, y2, 'g')

plt.figure(2)
plt.subplot(121)
plt.title("Plot 3")
plt.plot(t1, y2, 'k')

plt.subplot(122)
plt.title("Plot 4")
plt.plot(t1, y1, 'm')
plt.grid(True)

plt.show()

