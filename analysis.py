#!/usr/bin/env python
# coding: utf-8

# ## Import

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import numpy as np


# # DF's

# In[2]:


disney = pd.read_csv("data/Disney_Stocks_NASDAQ.csv",delimiter=',')
disney[disney.columns[1:]] = disney[disney.columns[1:]].replace(r'[\$,]', '', regex=True).astype(float)
disney


# In[3]:


disney['date'] = pd.to_datetime(disney['Date']).dt.date
disney = disney.drop("Date", axis = 1)
disney


# In[4]:


rc = pd.read_csv("data/comments.csv")
rc['Date'] = pd.to_datetime(rc['date']).dt.date
rc['Time'] = pd.to_datetime(rc['date']).dt.time
rc = rc.drop(["date","Time"], axis='columns')
rc


# In[5]:


rp = pd.read_csv("data/posts.csv")
rp['Date'] = pd.to_datetime(rp['date']).dt.date
rp['Time'] = pd.to_datetime(rp['date']).dt.time
rp = rp.drop(["date","Time"], axis='columns')
rp


# In[6]:


reddit = rp.merge(rc,on = "post_id")
reddit = reddit.drop("Date_y", axis = 1)
reddit


# ## EDA 

# In[7]:


plt.plot("date", "Low", data = disney)
plt.title("Lows per day (DISNEY)")

plt.savefig('data/Lows per day (DISNEY)')


# In[8]:


plt.plot("date", "High", data = disney)
plt.title("Highs per day")

plt.savefig('data/Highs per day (DISNEY)')


# In[9]:


reddit.groupby("post_id").agg("count").reset_index()
reddit.to_csv('data/reddit.csv')


# ## Sentiment Analysis

# In[10]:


rc_list = []
for i in range(len(rc)):
    p_1 = TextBlob(rc["body"][i]).sentiment.polarity
    rc_list.append(p_1)


# In[11]:


rc_list


# In[12]:


rp_list = []
for i in range(12):
    p_1 = TextBlob(rp["title"][i]).sentiment.polarity
    rp_list.append(p_1)


# In[13]:


rp_list


# In[14]:


rc_dict = {"comments":rc["comment_id"], "sentiment": rc_list, "date":rc['Date']}
df = pd.DataFrame.from_dict(rc_dict)
df['sentiment'].mean()


# In[15]:


ndf = df.merge(disney, on = "date")
ndf


# In[16]:


np.corrcoef(ndf["sentiment"], ndf["Close/Last"])


# In[17]:


plt.scatter(ndf["sentiment"],ndf["Close/Last"], color = "r", marker = "o", s = 30)
plt.title("Closing Stock to Comment Sentiment")

plt.savefig('data/Closing Stock to Comment Sentiment')


# In[18]:


rp_dict = {"comments":rp["post_id"], "sentiment": rp_list,"date":rp['Date']}
df1 = pd.DataFrame.from_dict(rp_dict)
df1['sentiment'].mean()


# In[19]:


ndf1 = df1.merge(disney, on = "date")
ndf


# In[20]:


np.corrcoef(ndf1["sentiment"], ndf1["Close/Last"])


# In[21]:


plt.scatter(ndf1["sentiment"],ndf1["Close/Last"], color = "r", marker = "o", s = 30)
plt.title("Closing Stock to Post Sentiment")

plt.savefig('data/Closing Stock to Post Sentiment')


# In[ ]:




