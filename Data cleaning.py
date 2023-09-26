#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
from IPython.display import FileLink, FileLinks
uploaded_file = FileLink('E:\Data analyst\Project\Data cleaning\sample_data.csv')
data = pd.read_csv('E:\Data analyst\Project\Data cleaning\sample_data.csv', encoding='latin1')


# In[8]:


data.head()


# In[9]:


data.info()


# In[15]:


data.head()


# In[21]:


data['Age']


# In[23]:


data['Age'] = data['Age'].astype('Int64')
median_age = data['Age'].median()
median_age=round(median_age)
data['Age'].fillna(median_age, inplace=True)


# In[24]:


data['Age']


# In[25]:


data['Gender'].fillna('Unknown', inplace=True)
data['Phone'].fillna('Unknown', inplace=True)
data['Address'].fillna('Unknown', inplace=True)


# In[26]:


data['Gender']


# In[27]:


data['Phone']


# In[28]:


data['Address']


# In[30]:


most_recent_date=pd.to_datetime(data['Last_Purchase_Date']).max()
data['Last_Purchase_Date'].fillna(most_recent_date,inplace=True)


# In[31]:


data['Last_Purchase_Date']


# In[32]:


data['Credit_Score']=pd.to_numeric(data['Credit_Score'],errors='coerce')
mean_credit_score=data['Credit_Score'].mean()
data['Credit_Score'].fillna(mean_credit_score,inplace=True)


# In[33]:


data['Credit_Score']


# In[34]:


data.drop_duplicates(inplace=True)
print(data.head())


# In[37]:


df=pd.DataFrame(data)
file_path = 'cleaned_sample_data.csv'
df.to_csv(file_path,index=False)


# In[ ]:




