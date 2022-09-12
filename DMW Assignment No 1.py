#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import all necessary libraries
import numpy as np
import pandas as pd
import matplotlib as plt


# In[4]:


#csv file read
df = pd.read_csv("Urban.csv")


# In[5]:


df


# In[6]:


df.head


# In[9]:


#display the shape of Ueban.
df.shape


# In[11]:


#display datatypes of datasetr.
df.dtypes


# In[12]:


#print information.
df.info


# In[14]:


#Print the length of dataset.
print(len(list(df)))


# In[15]:


#describe
df.describe


# In[16]:


#remove Duplicates.
df = df.drop_duplicates()


# In[17]:


#display total of duplicates.
sum(df.duplicated())


# In[18]:


df.head


# In[19]:


#data Manipulation using dummy values.
df = pd.get_ddummies(df,prefix=None,prefix_sep='_')


# In[20]:


df


# In[21]:


df.isnull().sum()


# In[24]:


#plot histogram.
df.hist()


# In[25]:


#plot Boxplot to find outlier.
df.boxplot()


# In[26]:


df


# In[ ]:




