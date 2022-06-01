#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[5]:


ti=pd.read_csv('tested.csv')


# In[6]:


ti.head()


# In[7]:


ti.info()


# In[8]:


ti.describe()


# In[11]:


ti.duplicated()


# In[12]:


ti.duplicated().head()


# In[13]:


ti.drop_duplicates()


# In[14]:


ti.drop_duplicates().count()


# In[15]:


ti.isnull().sum()


# In[16]:


ti.isnull().mean()


# In[17]:


ti['Age'].fillna(ti['Age'].mean(), inplace=True)


# In[19]:


ti['Embarked'].value_counts()


# In[20]:


ti['Embarked'].fillna('s', inplace=True)


# In[21]:


ti.drop('Cabin', axis=1, inplace=True)


# In[22]:


ti.head()


# In[23]:


ti.isnull().sum()


# In[24]:


ti['Fare'].fillna(ti['Fare'].mean(), inplace=True)


# In[25]:


ti.head()


# In[27]:


ti.isnull().sum()


# In[29]:


import matplotlib.pyplot as plt


# In[30]:


plt.plot('Age')


# In[ ]:




