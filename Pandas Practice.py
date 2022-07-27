#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[6]:


np.array([1,2,3,4,5])


# In[3]:


pd.Series([10,20,30,40,50])


# In[4]:


s= pd.Series([10,20,30,40,50])


# In[5]:


type(s)


# In[6]:


s.axes


# In[8]:


s.dtype


# In[9]:


s.size


# In[10]:


s.ndim


# In[12]:


s.values


# In[13]:


s.head


# In[14]:


s.head(2)


# In[15]:


s.tail


# In[16]:


s.tail(2)


# In[17]:


s.tail(3)


# In[ ]:





# In[23]:


mytail = np.array([8,9,7,10,14,2,8])


# In[24]:


mytail


# In[25]:


mytail = pd.Series([8,9,7,10,14,2,8])


# In[26]:


mytail


# In[27]:


mytail.index


# In[28]:


mytail.values


# In[29]:


mytail.tail


# In[30]:


mytail.tail(3)


# In[31]:


pd.Series([13,214,210,440,53])


# In[32]:


pd.Series([13,214,210,440,52],index=[4,6,7,3,87])


# In[34]:


s=pd.Series([13,214,210,440,53],index=["First","Second","Third","Fourth","Fith"])


# In[35]:


s


# In[36]:


s["Second"]


# In[40]:


ages = {"john" :42, "Jude" :43, "Dan" :21}


# In[41]:


ages


# In[42]:


pd.Series(ages)


# In[43]:


pd.Series(ages ,index=["John","Dan"])


# In[ ]:





# In[44]:


s1 = pd.Series([2,3,55,2,6,44])
s2 = pd.Series([421,325,3426,2,1,4,42])


# In[47]:


pd.concat([s1,s2])


# In[48]:


s.index


# In[50]:


list(s.items())


# In[51]:


s=pd.Series([13,214,210,440,53],index=["First","Second","Third","Fourth","Fith"])


# In[52]:


s


# In[53]:


list(s.items())


# In[56]:


3 in s1


# 34 in s1

# In[57]:


34 in s1


# In[58]:


s[["First","Second"]]


# In[59]:


s1 = pd.Series([2,3,55,2,6,44])


# In[60]:


s1


# In[65]:


s1[2]


# In[66]:


s1 = pd.Series([2,3,55,2,6,44])
s2 = pd.Series([421,325,3426,2,1,4,42])


# In[67]:


pd.concat([s1,s2])


# In[69]:


pd.DataFrame({"Name": [ "Mallon","Josh","Mary"], "Age": [17,34,45], 'Location': ["Kumasi","Accra","Tamale"]})


# In[70]:


Me = ({"Name": [ "Mallon","Josh","Mary"], "Age": [17,34,45], 'Location': ["Kumasi","Accra","Tamale"]})


# In[71]:


dataframe = pd.DataFrame(Me)


# In[72]:


dataframe


# In[73]:


dataframe["Age"]


# In[74]:


dataframe[["Age"]]


# In[75]:


Ama = [25,30,25,40,45,50,55,60]


# In[80]:


df = pd.DataFrame(Ama,columns=["Variable"])


# In[81]:


df


# In[83]:


Name = ["John","Mike","Julia","Anastcia"]


# In[85]:


df = pd.DataFrame(Name,columns=["Name"])


# In[86]:


df


# In[88]:


arr = np.array([5,6,7,8,3,2,1,2,42]).reshape(3,3,)


# In[89]:


arr


# In[90]:


pd.DataFrame(arr,columns=["Variable 1","Variable 2","Variable 3"])


# In[91]:


df.axes


# In[92]:


df.shape


# In[93]:


df.size


# In[94]:


df.ndim


# In[96]:


df.values


# In[ ]:




