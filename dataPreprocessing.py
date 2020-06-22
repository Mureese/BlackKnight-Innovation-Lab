#!/usr/bin/env python
# coding: utf-8

# In[8]:


get_ipython().system('ls')


# In[9]:


get_ipython().system('unzip shuff*')


# In[10]:


get_ipython().system('ls')


# In[81]:


import csv
import pandas as pd
from sklearn.model_selection import train_test_split
import sagemaker

sess = sagemaker.Session()

#reading data from csv
data = pd.read_csv("shuffled-full-set-hashed.csv", header = None)

#giving column names to pandas dataframe
data.rename( columns={0 :'labels',1: "text"}, inplace=True )
    
#checking number of categories 
labels = list(data.labels.unique())

#buiding map of categories for __label__category that blazing text expects
maps = {}
counter = 0
for i in labels:
    maps[i] = "__label__" + str(counter)
    counter += 1
    
data1 = data['labels'].map(maps) + " " + data['text']
print(maps)


#splitting data into training and test data with a 15% hold out for testing
train, test = train_test_split(data1, test_size = .15)

#transform into files to push into S3
train.to_csv('train_text.csv', index = 0, header = 0)
test.to_csv('test_text.csv', index = 0, header=0)

#push files into s3
sess.upload_data(path='train_text.csv', bucket="mureese-testing", key_prefix = "Train")
sess.upload_data(path='test_text.csv', bucket="mureese-testing", key_prefix = "Test")


# In[ ]:





