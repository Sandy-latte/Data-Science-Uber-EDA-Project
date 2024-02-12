#!/usr/bin/env python
# coding: utf-8

# In[37]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta 


# In[38]:


uber  = pd.read_csv(r"\\studata08\home\LI\Liq23sc\ManW10\Desktop\uber.csv")


# In[39]:


uber.head(10)


# In[40]:


uber.info()


# In[41]:


uber = uber.drop_duplicates() 
uber 


# In[42]:


uber = uber.drop(columns=['Request id'])


# In[43]:


#instead of using drop, subset the valid data 
uber = uber[uber['drop'].notna()]
uber


# In[44]:


#convert column to date format by pd.to_datetime 
#uber["Request"] = pd.to_datetime(uber["request"])
#uber["Drop"] = pd.to_datetime(uber["drop"])

uber[['request_time', 'drop']] = uber[['request_time', 'drop']].apply(pd.to_datetime)
uber


# In[45]:


#create a new column to return driving time 
uber['driving_time'] = uber['drop'] - uber['request_time']
#print(pd.Timedelta(uber['drop']-uber['request_time'])).seconds / 60.0
uber 


# In[ ]:


#uber['driving_time1'] = uber['driving_time'].dt.strftime('%H:%M')

#your column 'time' is of dtype timedelta as the error tells you; 
#you could use the total_seconds() method to convert to seconds and divide by 60 to get the minutes.



# In[46]:


#create a column to store total minutesinfo
uber['Total_Minutes'] = uber['driving_time'].dt.total_seconds() /60

uber 


# In[35]:


#this worked the first try 
#uber = uber.groupby('Driver id', sort = False)[['Status', 'Total_Minutes',]].mean()
#uber


# In[18]:


#x = uber['Total_Minutes'].max()
#y = uber['Total_Minutes'].min()
#print(x)
#print(y)


# In[48]:


uber = uber[uber['Total_Minutes'] > 0]
uber 


# In[57]:


#uber['Total_Minutes'].value_counts().sort_index().plot(c='darkblue')

#plt.hist(uber['Total_Minutes'], bins=10)  
#plt.xlabel('Value')
#plt.ylabel('Frequency')
#plt.title('Value Distribution within Column')

#plt.show()


# In[60]:


#add a new time column from existing info 

def time_group(Total_Minutes):
    if Total_Minutes < 10:
        return 'Less than 10min'
    elif Total_Minutes >= 10 and Total_Minutes < 20:
        return '10-19min'
    elif Total_Minutes >= 20 and Total_Minutes < 30:
        return '20-29min'
    elif Total_Minutes >= 30 and Total_Minutes < 40:
        return '30-39min'
    elif Total_Minutes >= 40 and Total_Minutes < 60:
        return '40-59min'
    else:
        return '60+min'
    
    


# In[62]:


#aaply the function to create a new column 
uber['time_group'] = uber['Total_Minutes'].apply(time_group)
uber


# In[63]:


#find the most frequent driving time group 
plt.hist(uber['time_group'], bins=10, edgecolor='black')  
plt.show()


# In[65]:


uber.info()


# In[67]:


uber['Hour'] = uber['request_time'].dt.hour
uber 


# # now we find the peak demand hours 

# In[112]:


uber1  = pd.read_csv(r"\\studata08\home\LI\Liq23sc\ManW10\Desktop\uber.csv")


# In[113]:


uber1= uber1.drop(columns=['Request id'])


# In[114]:


uber1[['request_time', 'drop']] = uber1[['request_time', 'drop']].apply(pd.to_datetime)
uber1


# In[123]:


#investigate the status frequency 
#uber 
#uber 1 

#use the uber data to see the frequency groups 
plt.hist(uber['Status'], bins=10, edgecolor='black', color='green')  
plt.show()


# In[116]:


#let's look at the 2: trip completed and no cars available 


#get the hour info from busy time period (no cars available)
#uber1 = uber1[(uber1['Status'] =='No Cars Available')  | (uber1['Status'] == 'Trip Completed')]

uber2 = uber1[uber1['Status'] != 'Cancelled']

uber2


# In[117]:


uber2['Peak Hour'] = uber2['request_time'].dt.hour
uber2


# In[122]:


#plot the peak hrs distribution
plt.hist(uber2['Peak Hour'], bins=10, edgecolor='black', color = 'pink')  
plt.show()


# 

# # now let's find out the hrs with no cars available -can consider increase the demand during these rush hrs 

# In[127]:


uber3  = pd.read_csv(r"\\studata08\home\LI\Liq23sc\ManW10\Desktop\uber.csv")


# In[128]:


uber3[['request_time', 'drop']] = uber3[['request_time', 'drop']].apply(pd.to_datetime)
uber3


# In[129]:


uber3 = uber3[uber3['Status'] == 'No Cars Available']

uber3


# In[130]:


uber3['No Cars Available Peak Hour'] = uber3['request_time'].dt.hour
uber3


# In[133]:


plt.hist(uber3['No Cars Available Peak Hour'], bins=10, edgecolor='black', color = 'purple')  
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




