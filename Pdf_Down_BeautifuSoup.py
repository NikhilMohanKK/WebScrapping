# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 21:13:14 2019

@author: KK NIKHIL MOHAN
"""

from bs4 import BeautifulSoup
import urllib
import warnings
warnings.simplefilter('ignore')

response = urllib.request.urlopen('https://twitter.com/arXiv__ml')
soup = BeautifulSoup(response)


link = soup.find_all('span', class_='js-display-url')
lst=list(i.get_text() for i in link)
lst=lst[2:]


e='https://'+lst[0]
response = urllib.request.urlopen(e)
soup = BeautifulSoup(response)
lsty=[]



for i in lst:
    q='https://'+i
    response = urllib.request.urlopen(q)
    soup = BeautifulSoup(response)
    linke = soup.find_all('a',href=True,text="PDF")
    for o in linke:
        lsty.append('https://arxiv.org'+o['href'])


for i in range(len(lsty)):
    url=lsty[i]
    nm=lsty[i].split('/')
    import os
    os.chdir("D:\Webc")
    import requests
    pdf = requests.get(url)
    with open('D:\Webc\\'+nm[4]+'.pdf', 'wb') as f:  
        f.write(pdf.content)
