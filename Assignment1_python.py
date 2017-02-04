
# coding: utf-8

# In[1]:

import numpy


# In[2]:

data = numpy.genfromtxt('classFile.csv', dtype='str',delimiter=',')


# In[3]:

data


# In[4]:

minGPA=min(float(column[1].replace(',', '')) for column in data)


# In[5]:

minGPA


# In[6]:

maxGPA=max(float(column[1].replace(',', '')) for column in data)


# In[7]:

maxGPA


# In[8]:

import statistics


# In[9]:

medianGPA=statistics.median(float(column[1].replace(',', '')) for column in data)


# In[10]:

medianGPA


# In[11]:

meanGPA=statistics.mean(float(column[1].replace(',', '')) for column in data)


# In[12]:

meanGPA


# In[13]:

minWEX = min(float(column[2].replace(',', '')) for column in data)


# In[14]:

minWEX


# In[15]:

maxWEX = max(float(column[2].replace(',', '')) for column in data)


# In[16]:

maxWEX


# In[17]:

medianWEX = statistics.median(float(column[2].replace(',', '')) for column in data)


# In[18]:

medianWEX


# In[19]:

meanWEX=statistics.mean(float(column[2].replace(',', '')) for column in data)


# In[20]:

meanWEX


# In[21]:

modeSal = statistics.mode(str(column[3].replace(',', '')) for column in data)


# In[22]:

modeSal


# In[23]:

from collections import Counter


# In[24]:

c = Counter((column[6].replace(',', '')for column in data))


# In[25]:

c


# In[26]:

l = len(data)


# In[27]:

l


# In[28]:

print(c['N']/l)


# In[29]:

print(c['Y']/l)


# In[30]:

import csv


# In[31]:

with open("ClassData.csv") as f:
    reader = csv.DictReader(f)
    rows = [row for row in reader if row['Number of contacts on Linkedin'] > '500']


# In[32]:

rows


# In[33]:

StudentsWith500Cont = len(rows)


# In[34]:

StudentsWith500Cont


# In[35]:

a=sorted((column[8].replace(',', '')for column in data))


# In[36]:

a


# In[37]:

value_list = [int(x) for x in a if x]


# In[38]:

value_list


# In[39]:

q75, q25 = numpy.percentile(value_list, [75 ,25])


# In[40]:

iqr = q75 -q25


# In[41]:

iqr


# In[ ]:



