#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[2]:


X = np.arange(-5,5,0.25)
Y = np.arange(-5,5,0.25)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)


# In[3]:


plt.figure(1)
plt.subplot(131)
plt.plot(X)

plt.subplot(132)
plt.plot(R)

plt.subplot(133)
plt.plot(Z)


# ### Normal 3D plot

# In[5]:


from mpl_toolkits.mplot3d import Axes3D

# interactive plots embedded within the notebook
get_ipython().run_line_magic('matplotlib', 'notebook')

X = np.arange(-5,5,0.25)
Y = np.arange(-5,5,0.25)
X,Y = np.meshgrid(X,Y)    # Make N-D coordinate arrays for vectorized evaluations
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

fig = plt.figure()
ax  = fig.add_subplot(projection='3d')
surface_plot = ax.plot_surface(X,Y,Z, antialiased=False)


# ### Playing with Antializing and stride

# In[6]:


from mpl_toolkits.mplot3d import Axes3D

# interactive plots embedded within the notebook
get_ipython().run_line_magic('matplotlib', 'notebook')

X = np.arange(-5,5,0.25)
Y = np.arange(-5,5,0.25)
X,Y = np.meshgrid(X,Y)    # Make N-D coordinate arrays for vectorized evaluations
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

fig = plt.figure()
ax  = fig.add_subplot(projection='3d')
surface_plot = ax.plot_surface(X,Y,Z, antialiased=True, rstride=1, cstride=1)

# The rstride and cstride kwargs set the stride used to sample the input data to generate the graph


# ### Adding colormap and colorbar (shrink & aspect) to 3D plot

# In[11]:


from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# interactive plots embedded within the notebook
get_ipython().run_line_magic('matplotlib', 'notebook')

X = np.arange(-5,5,0.25)
Y = np.arange(-5,5,0.25)
X,Y = np.meshgrid(X,Y)    # Make N-D coordinate arrays for vectorized evaluations
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

fig = plt.figure()
ax  = fig.add_subplot(projection='3d')
surface_plot = ax.plot_surface(X,Y,Z, antialiased=True,rstride=1, cstride=1, cmap = cm.coolwarm )   
#other cmap values -> ['PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu','RdYlBu', 
#                     'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic' ]

fig.colorbar(surface_plot, shrink=0.5, aspect=10)


# ### Adjust Axis, if required

# In[12]:


from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# interactive plots embedded within the notebook
get_ipython().run_line_magic('matplotlib', 'notebook')

X = np.arange(-5,5,0.25)
Y = np.arange(-5,5,0.25)
X,Y = np.meshgrid(X,Y)    # Make N-D coordinate arrays for vectorized evaluations
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

fig = plt.figure()
ax  = fig.add_subplot(projection='3d')
surface_plot = ax.plot_surface(X,Y,Z, antialiased=True,rstride=1, cstride=1, cmap = cm.Spectral )   
fig.colorbar(surface_plot, shrink=0.5, aspect=10)

# Customize the axis.
ax.set_zlim(-1, 1)
ax.set_ylim(-6, 6)
ax.set_xlim(-7,7)

