#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# ### Generating sample data for plots

# In[2]:


t = np.arange(0.01, 20.0, 0.01)
y1 = np.exp(-t / 5.0)
y2 = np.sin(2 * np.pi * t)
plt.plot(t,y1,'--r',t,y2,'-g')
plt.show()


# #### Normal plot y1 over t

# In[3]:


plt.plot(t, y1)
plt.title("Normal plot of y1 over t", fontsize=14)
plt.xlabel('Time')
plt.ylabel('Data is y1')
plt.grid(True)
plt.show()


# #### Plotting y1 over t  |  BUT making Y axis as logrithmic(base 10)

# In[4]:


plt.semilogy(t, y1)
plt.title("Y axis as Logrithmic axis", fontsize=14)
plt.xlabel('Time')
plt.ylabel('Data is y1')
plt.grid(True)
plt.show()


# #### Plotting y2 over t  |  BUT making X axis as logrithmic(base 10)

# In[5]:


plt.semilogx(t, y2)
plt.title("X axis as Logrithmic axis", fontsize=14)
plt.xlabel('Time')
plt.ylabel('Data is y2')
plt.grid(True)
plt.show()


# #### Plotting y2 over t  |  BUT making X axis as logrithmic(base 2)

# In[6]:


plt.semilogx(t, 20 * y1, basex=2)
plt.title("X axis as Log with base 2", fontsize=14)
plt.xlabel('Time')
plt.ylabel('Data is y1')
plt.grid(True)
plt.show()


# In[ ]:




