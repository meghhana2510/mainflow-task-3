#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install requests beautifulsoup4 pandas')


# In[3]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[5]:


#parse the website
url = "https://www.netflix.com/in/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")


# In[6]:


#Extract relevant information
paragraphs = [p.text for p in soup.find_all('p')]


# In[7]:


# Extract all links
links = [a['href'] for a in soup.find_all('a', href=True)]


# In[8]:


# Extract all images
images = [img['src'] for img in soup.find_all('img', src=True)]


# In[9]:


# Print extracted information
print("Paragraphs:", paragraphs)
print("Links:", links)
print("Images:", images)


# In[10]:


# Create a DataFrame for paragraphs
df_paragraphs = pd.DataFrame(paragraphs, columns=['Text'])


# In[11]:


# Create a DataFrame for links
df_links = pd.DataFrame(links, columns=['Link'])


# In[12]:


# Create a DataFrame for images
df_images = pd.DataFrame(images, columns=['Image'])


# In[13]:


# Display DataFrames
print("\nDataFrame for Paragraphs:")
print(df_paragraphs)

print("\nDataFrame for Links:")
print(df_links)

print("\nDataFrame for Images:")
print(df_images)


# In[14]:


# Save DataFrames to CSV files
df_paragraphs.to_csv('paragraphs.csv', index=False)
df_links.to_csv('links.csv', index=False)
df_images.to_csv('images.csv', index=False)

print("Data saved to CSV files.")


# In[ ]:




