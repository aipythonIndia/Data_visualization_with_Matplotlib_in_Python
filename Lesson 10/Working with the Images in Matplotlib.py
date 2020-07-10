#!/usr/bin/env python
# coding: utf-8

# # Matplotlib only supports PNG images  (Natively)

# In[1]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# In[2]:


image_location = r"D:\Courses\Matplotlib_Python\Code\ship.png"
img = mpimg.imread(image_location)


# In[3]:


print (img)


# In[4]:


get_ipython().run_line_magic('matplotlib', 'notebook')
plt.imshow(img)


# In[5]:


print (img.shape)


# In[6]:


get_ipython().run_line_magic('matplotlib', 'notebook')
plt.imshow(img, cmap = 'gray')


# ### Applying pseudocolor schemes to image plots

# In[ ]:


# Pseudocolor can be a useful tool for enhancing contrast and visualizing your data more easily
# Pseudocolor is only relevant to single-channel, grayscale images.


# In[7]:


get_ipython().run_line_magic('matplotlib', 'notebook')
plt.imshow(img, cmap = 'hot')

#other cmap values -> ['PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu','RdYlBu', 
#                     'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic', 'nipy_spectral' ]


# In[10]:


get_ipython().run_line_magic('matplotlib', 'notebook')
plt.imshow(img, cmap = "coolwarm", alpha= 1 )
plt.colorbar()


# In[13]:


get_ipython().run_line_magic('matplotlib', 'notebook')
plt.imshow(img, cmap = 'nipy_spectral', alpha= 0.8)
plt.colorbar()


# In[14]:


get_ipython().run_line_magic('matplotlib', 'notebook')
plt.hist(img)


# In[15]:


get_ipython().run_line_magic('matplotlib', 'notebook')
image_location = r"D:\Courses\Matplotlib_Python\Code\dog3.png"
img2 = mpimg.imread(image_location)

plt.imshow(img2)
img2.shape


# In[16]:


get_ipython().run_line_magic('matplotlib', 'notebook')
CH_R = img2[:,:,0]

plt.imshow(CH_R)


# In[18]:


get_ipython().run_line_magic('matplotlib', 'notebook')
plt.imshow(CH_R, cmap = 'cool', alpha= 1)
plt.colorbar()


# In[19]:


get_ipython().run_line_magic('matplotlib', 'notebook')

plt.hist(CH_R)


# In[ ]:




