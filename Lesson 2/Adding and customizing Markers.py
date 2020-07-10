#!/usr/bin/env python
# coding: utf-8

# ### Importing Modules (Library)

# In[1]:


import matplotlib.pyplot as plt


# ### Adding Markers to the plot - circle marker

# In[2]:


x_data = [1,2,3,4,5]
y_data = [1, 4, 9, 16, 25]
plt.plot(x_data, y_data, 'o-g') # Marker as circle "o"
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# ### Adding Markers to the plot - Traingular marker

# In[3]:


x_data = [1,2,3,4,5]
y_data = [1, 4, 9, 16, 25]
plt.plot(x_data, y_data, 'v--b') # Marker as "Traingle"
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# ### Linewidth option with plot

# In[4]:


plt.plot(x_data, y_data, 'v--b', linewidth = 5)
plt.show()


# ### Plotting multiple lines on the same plot

# In[6]:


plt.plot(x_data, y_data, 'v--b')
plt.plot(y_data, x_data, 'o-g')
plt.show()


# ### Plotting multiple lines using single plot method

# In[7]:


plt.plot(x_data, y_data, 'v--b',y_data, x_data, 'o-g')
plt.show()


# In[ ]:




