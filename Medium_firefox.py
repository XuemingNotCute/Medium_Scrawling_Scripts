
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import urllib
import urllib.request
from bs4 import BeautifulSoup


# In[5]:


def unique(it):
        s = set()
        for el in it:
            if el not in s:
                s.add(el)
                yield el


# In[6]:


import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()



browser.get("https://medium.com/topic/design")
time.sleep(1)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 2500

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1
    
    
#page = requests.get("https://medium.com/topic/design")
#soup = BeautifulSoup(page.content, 'html.parser')

#post_elems = browser.find_elements_by_class_name("a")


#for post in post_elems:
    #print(post.text)
    
#print("------------------")

#print(browser)


print("printed all links")

time.sleep(1)
data = browser.page_source
soup = BeautifulSoup(data, "html.parser")


# In[114]:


time.sleep(200)
data = browser.page_source
soup = BeautifulSoup(data, "html.parser")


# In[108]:


text=[]
i=0
for link in soup.find_all("h3", {"class": "bu bv bw w bx x ck ea eb d ct ec ed"}):
    #print(i)
    text.append(link.text.replace('\n', ''))
    i=i+1


# In[109]:


links_with_text = []
for a in soup.find_all('a', href=True): 
    if a.text: 
        links_with_text.append(a['href'])
res = [k for k in links_with_text if 'source=topic_page' in k]
res1 = [k for k in res if '/p' in k]
res2=list(unique(res1))


# In[110]:


res2


# In[111]:


text1= pd.DataFrame(text)
#category1= pd.DataFrame(category)
link= pd.DataFrame(res2)
frames = [link, text1]
result = pd.concat(frames, axis=1)
result.columns = ['Link1', 'Title']


# In[112]:


result


# In[113]:


result.to_csv('links.csv')

