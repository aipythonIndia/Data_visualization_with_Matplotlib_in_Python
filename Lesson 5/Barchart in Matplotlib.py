#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# # Bar chart

# ### Simplest way to create a bar chart (or bar graph)

# In[2]:


avg_score = [60, 20, 57, 98, 26, 55, 88, 19, 74, 60]
sub = ['Math','Phy','Chem','Bio','IT', 'Sci', 'Tec','PT','ECE', 'Comp']
plt.bar(sub,avg_score)
plt.title('Average score for Subjects', fontsize =16)
plt.xlabel('Subjects',fontsize = 14, color = 'm')
plt.ylabel('Scores', fontsize = 14, color = 'g')
plt.show()


# ### Changing color and width of the bar

# In[5]:


avg_score = [60, 20, 57, 98, 26, 55, 88, 19, 74, 60]
sub = ['Math','Phy','Chem','Bio','IT', 'Sci', 'Tec','PT','ECE', 'Comp']
plt.title('Average score for Subjects', fontsize =16)
plt.xlabel('Subjects',fontsize = 14, color = 'm')
plt.ylabel('Scores', fontsize = 14, color = 'g')

plt.bar(sub,avg_score, width = 0.6 ,color = 'c')
plt.show()


# ### Applying different color to each bar

# In[6]:


avg_score = [60, 20, 57, 98, 26, 55, 88, 19, 74, 60]
sub = ['Math','Phy','Chem','Bio','IT', 'Sci', 'Tec','PT','ECE', 'Comp']
plt.title('Average score for Subjects', fontsize =16)
plt.xlabel('Subjects',fontsize = 14, color = 'm')
plt.ylabel('Scores', fontsize = 14, color = 'g')
colors = ['blue', 'orange', 'green', 'cyan', 'magenta', 'yellow', 'black', 'purple', 'red', 'orange']

plt.bar(sub,avg_score, width = 0.6 ,color = colors)
plt.show()


# ### Changing the Orientation to horizontal using -->  plt.barh

# In[7]:


avg_score = [60, 20, 57, 98, 26, 55, 88, 19, 74, 60]
sub = ['Math','Phy','Chem','Bio','IT', 'Sci', 'Tec','PT','ECE', 'Comp']
plt.title('Average score for Subjects', fontsize =16)
plt.xlabel('Subjects',fontsize = 14, color = 'm')
plt.ylabel('Scores', fontsize = 14, color = 'g')
colors = ['blue', 'orange', 'green', 'cyan', 'magenta', 'yellow', 'black', 'purple', 'red', 'orange']

plt.barh(sub,avg_score,color = colors)
plt.show()

