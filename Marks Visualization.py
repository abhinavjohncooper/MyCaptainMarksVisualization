#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install matplotlib')



# In[4]:


get_ipython().system('pip install pandas')


# In[16]:


import matplotlib.pyplot as plt
import pandas as pd


# In[14]:


df = pd.read_csv(r"C:\Users\asus\Desktop\Marks.csv")


# In[17]:


mar = df.plot(kind='bar' , alpha = 0.4, color='b')







