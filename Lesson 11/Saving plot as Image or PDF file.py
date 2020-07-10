#!/usr/bin/env python
# coding: utf-8

# # Saving plots as PNG/PDF in Matplotlib

# In[1]:


import numpy as np
from matplotlib import pyplot as plt

X = np.linspace(-10, 10, 1024)
Y = np.sinc(X)
plt.plot(X, Y)
plt.savefig('my_fig.png')
# 800 x 600 pixels, in 8-bit colors


# ### Saving with DPI option

# In[2]:


t1 = np.arange(0.0, 5.0, 0.1)
y1 = np.sin(2*np.pi*t1)
y2 = np.cos(2*np.pi*t1)
plt.plot(t1, y1, 'r')
plt.plot(t1, y2, 'g')

plt.savefig('y1 and y2_over_t1.png', dpi= 300) #Dots per Inch , 2400 x 1800 pixels
plt.show()


# ### Saving with Transparent option

# In[3]:


t1 = np.arange(0.0, 5.0, 0.1)
y1 = np.sin(2*np.pi*t1)
y2 = np.cos(2*np.pi*t1)

plt.figure()

plt.subplot(211)
plt.plot(t1, y1, 'r')
plt.subplot(212)
plt.plot(t1, y2, 'g')
plt.savefig("y1y2_over_t1.png", transparent = True)
plt.show()


# ### Saving plot as PDF file

# In[4]:


import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D   

X = np.arange(-5,5,0.25)
Y = np.arange(-5,5,0.25)
X,Y = np.meshgrid(X,Y)    # Make N-D coordinate arrays for vectorized evaluations
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

fig = plt.figure()
ax  = fig.add_subplot(projection='3d')
surface_plot = ax.plot_surface(X,Y,Z, antialiased=False)
plt.savefig("3Dsurface.pdf")


# In[ ]:




