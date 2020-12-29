#!/usr/bin/env python
# coding: utf-8

# In[36]:


pip install --user splinter


# In[74]:


import requests
import json
from bs4 import BeautifulSoup as bs
import splinter


# In[156]:


executable_path = {'executable_path' : 'chromedriver.exe'}
browser = splinter.Browser('chrome', **executable_path)


# In[76]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)
html = browser.html


# In[81]:


soup = bs(html, 'html.parser')
print(soup.prettify())


# In[82]:


content = soup.find("div", class_='content_page')


# In[83]:


titles = content.find_all("div", class_='content_title')
print(titles[0].text.strip())


# In[84]:


article_text = content.find_all("div", class_='article_teaser_body')
article_text[0].text


# In[157]:


url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
html = browser.html


# In[158]:


soup = bs(html, 'html.parser')
featured_image = soup.find("article", class_='carousel_item')['style']


# In[159]:


latter = featured_image.split('/spaceimages/')[1].split("'")[0]


# In[160]:


former = url.split('?')[0]


# In[161]:


#wallpaper Image
final_url = former + latter
final_url


# In[162]:


browser.find_by_id("full_image").click()


# In[163]:


browser.find_by_text("more info     ").click()


# In[168]:


html = browser.html
soup = bs(html, 'html.parser')
featured_img = soup.find("img", class_="main_image")['src']


# In[169]:


featured_img


# In[170]:


pic_url = former + featured_img
pic_url


# In[ ]:




