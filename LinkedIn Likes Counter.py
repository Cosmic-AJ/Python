m# -*- coding: utf-8 -*-
"""
Created on Sat May 29 13:06:22 2021

@author: Ayush Jain
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

html = urlopen("file:/C:/Users/msimp/Downloads/new.html").read()
soup = BeautifulSoup(html, "html.parser")

names = [] 
for div in soup.findAll('span', {'class': 'feed-shared-actor__name'}):
    names.append(div.text.strip())

likes = [] 
for div in soup.findAll('span', {'class': 'social-details-social-counts__reactions-count'}):
    likes.append(div.text.strip())
    
total_likes=0
for i in likes:
    total_likes += int(i.replace(',',''))

print('\nNumber of Posts Posted  : ',str(len(likes)))
print('Total Likes on all post : ',str(total_likes))
print('Average Likes per post  : ',str(total_likes/len(likes)),'\n')

data = pd.DataFrame({"Name":names[:len(likes)],"Like":likes})
print(data.head())

print("\n",data.shape)

data.to_csv('C:/Users/msimp/Downloads/Like_Counter.csv',index=False)