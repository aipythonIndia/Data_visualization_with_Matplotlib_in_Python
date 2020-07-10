#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


# This data is EURO to INR exchange rates for some duration
file_path = r'D:\Courses\Matplotlib_Python\Code\EUR_INR.csv'
data = pd.read_csv(file_path)


# ### Some insight about Data

# In[4]:


data.head(10)


# In[5]:


data = pd.read_csv(file_path, index_col = 0)
data.head()


# In[7]:


data.shape


# In[8]:


data.describe()


# ### Slicing the required data for plotting

# In[9]:


high_val = data['High']
high_val


# In[10]:


low_val = data['Low']
low_val


# In[11]:


high_val.shape, low_val.shape


# In[12]:


get_ipython().run_line_magic('matplotlib', 'notebook')
plt.plot(high_val,'v--r' ,label = 'Highest Val')
plt.plot(low_val, label = 'Lowest Val')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('EURO vs INR price', fontsize =14)
plt.grid()
plt.legend()


# In[15]:


open_val = data['Open']


# In[16]:


get_ipython().run_line_magic('matplotlib', 'notebook')
plt.plot(high_val,'v--r' ,label = 'Highest Val')
plt.plot(low_val, label = 'Lowest Val')
plt.plot(open_val, label = 'Open Val')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('EURO vs INR price', fontsize =14)
plt.grid()
plt.legend()


# In[17]:


get_ipython().run_line_magic('matplotlib', 'notebook')
adj_close = data['Adj Close']

plt.plot(high_val,'v--r' ,label = 'Highest Val')
plt.plot(low_val, label = 'Lowest Val')
plt.plot(open_val, label = 'Open Val')
plt.plot(adj_close, label = 'Ajusted close')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('EURO vs INR price', fontsize =14)
plt.grid()
plt.legend()

