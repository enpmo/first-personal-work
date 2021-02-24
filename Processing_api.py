#!/usr/bin/env python
# coding: utf-8

# In[8]:


import requests
import re
import time
import json

def get_one_page(url):
    # 根据源码分析，构造请求头
    headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/52.0.2743.116 Safari/537.36'
        "authoration":"apicode","apicode":"2b33b36fb2564ecaaac6ae66226e995f"
    }
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        return response.content.decode(encoding='utf-8')
    return None
 
url = 'https://api.yonyoucloud.com/apis/dst/ncov/wholeworld'
html = get_one_page(url)
print(html)


# In[15]:


import json
b = json.dumps(html)
f2 = open('json2.json', 'w',encoding='utf-8')
f2.write(b)
f2.close()


# In[14]:


import json
f = open('global_epidemic_statistics.json.json', 'w',encoding='utf-8')
f.write(html)
f.close()


# In[ ]:




