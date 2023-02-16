#!/usr/bin/env python
# coding: utf-8

# # Notebook Imports

# In[21]:


from sklearn.datasets import load_boston
import pandas as pd
import numpy as np


data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]


# # Gather Data

# In[16]:


boston_dataset


# In[17]:


dir(boston_dataset)


# In[18]:


print(boston_dataset.DESCR)


# # Data points and features

# In[34]:


import pandas as pd
from colorama import Fore
from sklearn.datasets import load_boston
from tabulate import tabulate
boston_dataset = load_boston()


# In[9]:


print(Fore.LIGHTMAGENTA_EX,boston_dataset.data.shape)


# In[10]:


boston_dataset.feature_names


# In[11]:


boston_dataset.target


# # Data exploration with pandas dataframes

# In[13]:


data = pd.DataFrame(data=boston_dataset.data,columns=boston_dataset.feature_names)
data['PRICE'] = boston_dataset.target


# In[15]:


data.head()


# In[17]:


data.count()


# In[20]:


timp = 180
s_n_cump = 2100
s_n_e = s_n_cump / timp
print(s_n_e)


# In[21]:


12*180


# # Cleaning data - check for missing values

# In[31]:


print(pd.isnull(data).any())


# In[33]:


print(data.info())


# In[36]:


print(tabulate(boston_dataset, headers='keys', tablefmt="grid"))


# In[38]:


from tabulate import tabulate
from colorama import Fore,Back,Style


# In[47]:


sh_ip_int_br = [('FastEthernet0/0', '15.0.15.1', 'up', 'up'),
        ('FastEthernet0/1', '10.0.12.1', 'up', 'down'),
        ('FastEthernet0/2', '10.0.13.1', 'up', 'up'),
        ('Loopback0', '10.1.1.1', 'up', 'up'),
        ('Loopback100', '100.0.0.1', 'down', 'up')]
data= [('Interface', 'IP', 'Status', 'Protocol'),
     ('FastEthernet0/0', '15.0.15.1', 'up', 'down'),
     ('FastEthernet0/1', '10.0.12.1', 'up', 'up'),
     ('FastEthernet0/2', '10.0.13.1', 'up', 'up'),
     ('Loopback0', '10.1.1.1', 'up', 'up'),
     ('Loopback100', '100.0.0.1', 'down', 'up')]
list_of_dict= [{'IP': '15.0.15.1',
      'Interface': 'FastEthernet0/0',
      'Protocol': 'up',
      'Status': 'up'},
     {'IP': '10.0.12.1',
      'Interface': 'FastEthernet0/1',
      'Protocol': 'up',
      'Status': 'up'},
     {'IP': '10.0.13.1',
      'Interface': 'FastEthernet0/2',
      'Protocol': 'up',
      'Status': 'up'},
     {'IP': '10.1.1.1',
      'Interface': 'Loopback0',
      'Protocol': 'up',
      'Status': 'up'},
     {'IP': '100.0.0.1',
      'Interface': 'Loopback100',
      'Protocol': 'up',
      'Status': 'up'}]

columns = ['Interface', 'IP', 'Status', 'Protocol']
print(Fore.BLUE,tabulate(sh_ip_int_br))
print(Fore.BLACK, tabulate(data, headers='firstrow'))
print(Fore.BLUE, tabulate(sh_ip_int_br, headers=columns))
print(Fore.MAGENTA,tabulate(list_of_dict, headers='keys', tablefmt="grid"))
print(Fore.BLACK,tabulate(list_of_dict, headers='keys'))


# In[50]:


vlans = {"sw1": [10, 20, 30, 40], "sw2": [1, 2, 10], "sw3": [1, 2, 3, 4, 5, 10, 11, 12]}
print(Fore.GREEN, tabulate(vlans, headers='keys'))
print(Fore.GREEN,tabulate(list_of_dict, headers='keys', tablefmt="grid"))
print(Fore.GREEN,tabulate(list_of_dict, headers='keys', tablefmt='pipe', stralign='center'))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




