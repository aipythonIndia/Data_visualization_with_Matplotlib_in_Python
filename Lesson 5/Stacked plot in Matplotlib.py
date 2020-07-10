#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# # Stack plot

# ### Plotting basic Stack plot

# In[2]:


avg_score = [50, 20, 57, 60, 26, 55, 88, 19, 74, 60]
sub = ['Math','Phy','Chem','Bio','IT', 'Sci', 'Tec','PT','ECE', 'Comp']
grace_marks = [12, 24, 6, 5, 7, 10, -7, 20, 4, 9]

plt.title('Average score for Subjects', fontsize =16)
plt.xlabel('Subjects',fontsize = 14, color = 'm')
plt.ylabel('Scores', fontsize = 14, color = 'g')

plt.bar(sub,avg_score, label ='Average Score' )
plt.bar(sub, grace_marks , bottom = avg_score)

plt.show()


# ### Changing colors and width of each bar

# In[3]:


avg_score = [50, 20, 57, 60, 26, 55, 88, 19, 74, 60]
sub = ['Math','Phy','Chem','Bio','IT', 'Sci', 'Tec','PT','ECE', 'Comp']
grace_marks = [12, 24, 6, 5, 7, 10, -7, 20, 4, 9]

plt.title('Average score for Subjects', fontsize =16)
plt.xlabel('Subjects',fontsize = 14, color = 'm')
plt.ylabel('Scores', fontsize = 14, color = 'g')
colors = ['blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'black', 'purple', 'red', 'orange']

plt.bar(sub,avg_score, width = 0.7,color = colors)
plt.bar(sub, grace_marks, width = 0.7, bottom = avg_score, color = 'green')

plt.show()


# ### Adding legends to the Stack plot

# In[4]:


avg_score = [50, 20, 57, 60, 26, 55, 88, 19, 74, 60]
sub = ['Math','Phy','Chem','Bio','IT', 'Sci', 'Tec','PT','ECE', 'Comp']
grace_marks = [12, 24, 6, 5, 7, 10, -7, 20, 4, 9]

plt.title('Average score for Subjects', fontsize =16)
plt.xlabel('Subjects',fontsize = 14, color = 'm')
plt.ylabel('Scores', fontsize = 14, color = 'g')
colors = ['blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'black', 'purple', 'red', 'orange']

plt.bar(sub,avg_score, width = 0.7,color = colors, label ='Average Score' )
plt.bar(sub, grace_marks, width = 0.7, bottom = avg_score, color = 'green', label = 'Grace Mark')

plt.legend(loc ='best')
plt.show()


# ### Adding error or deviations in the stack

# In[5]:


avg_score = [50, 20, 57, 60, 26, 55, 88, 19, 74, 60]
sub = ['Math','Phy','Chem','Bio','IT', 'Sci', 'Tec','PT','ECE', 'Comp']
grace_marks = [12, 24, 6, 5, 7, 10, -7, 20, 4, 9]

plt.title('Average score for Subjects', fontsize =16)
plt.xlabel('Subjects',fontsize = 14, color = 'm')
plt.ylabel('Scores', fontsize = 14, color = 'g')
colors = ['blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'black', 'purple', 'red', 'orange']

plt.bar(sub,avg_score, width = 0.7,color = colors, label ='Average Score', yerr = grace_marks )
plt.bar(sub, grace_marks, width = 0.7, bottom = avg_score, color = 'green', label = 'Grace Mark')

plt.legend(loc ='best')
plt.show()

