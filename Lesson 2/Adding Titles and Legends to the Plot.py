#!/usr/bin/env python
# coding: utf-8

# ### Importing Modules (Library)

# In[1]:


import matplotlib.pyplot as plt
import numpy as np # pip install numpy


# ### Generate data using Numpy module and augment the data

# In[2]:


x_data = np.linspace(0,10, 100) #Generate data
y1 = x_data**2
y2 = x_data**3
y3 = x_data*2.5

plt.plot(x_data, y1)
plt.plot(x_data, y2)
plt.plot(x_data, y3)

plt.xlabel("Number from 0 to 10")
plt.ylabel("Various calculations")

plt.show()


# ### Adding Plot Title

# In[3]:


plt.plot(x_data, y1)
plt.plot(x_data, y2)
plt.plot(x_data, y3)
plt.xlabel("Number from 0 to 10")
plt.ylabel("Various calculations")
plt.title("3 lines on the same plot")
plt.show()


# ### Adding Plot Title at Runtime - Dynamically

# In[4]:


plt.plot(x_data, y1)
plt.plot(x_data, y2)
plt.plot(x_data, y3)
plt.xlabel("Number from 0 to 10")
plt.ylabel("Various calculations")
plot_title = input("Enter your plot title: ")
plt.title(plot_title)
plt.show()


# ### Adding Legends - Method 1

# In[5]:


plt.plot(x_data, y1)
plt.plot(x_data, y2)
plt.plot(x_data, y3)
plt.xlabel("Number from 0 to 10")
plt.ylabel("Various calculations")
plt.title("3 lines on the same plot")
plt.legend(['Square','Cube','Mul_by_2.5'])
plt.show()


# ### Adding Legends - Method 2 (using label in the plot method)

# In[7]:


plt.plot(x_data, y1, label = "Square") #using label
plt.plot(x_data, y2, label = "Cube")
plt.plot(x_data, y3, label = "Mul_by_2.5")
plt.xlabel("Number from 0 to 10")
plt.ylabel("Various calculations")
plt.title("3 lines on the same plot")
plt.legend()
plt.show()


# ### Adjusting the location of Legend

# In[8]:


plt.plot(x_data, y1, label = "Square") #using label
plt.plot(x_data, y2, label = "Cube")
plt.plot(x_data, y3, label = "Mul_by_2.5")
plt.xlabel("Number from 0 to 10")
plt.ylabel("Various calculations")
plt.title("3 lines on the same plot")
plt.legend(loc="center")
plt.show()


# ### Format Line style with Legend

# In[9]:


plt.plot(x_data, y1,'--r', label = "Square")
plt.plot(x_data, y2,'-g', label = "Cube", linewidth = 4)
plt.plot(x_data, y3, label = "Mul_by_2.5")
plt.xlabel("Number from 0 to 10")
plt.ylabel("Various calculations")
plt.title("3 lines on the same plot")
plt.legend(loc="center")
plt.show()


# In[ ]:




