# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 21:13:14 2019

@author: KK NIKHIL MOHAN
"""


#importing the modules and libraries
from bs4 import BeautifulSoup
import urllib
import os
import warnings
warnings.simplefilter('ignore')


"""this program navigates to a twitter account and finds all the hyperlinks 
from the page to navigate to them and find the pdfs present in them.
The pdf files found on the corresponding pages are downloaded into a local
directory on the system
"""
#site you want to navigate and perform the operations
response = urllib.request.urlopen('https://twitter.com/arXiv__ml')
soup = BeautifulSoup(response)


#finding the tags which 
link = soup.find_all('span', class_='js-display-url')
lst=list(i.get_text() for i in link)
lst=lst[2:]

#navigating to all the links obtained from the current page
e='https://'+lst[0]
response = urllib.request.urlopen(e)
soup = BeautifulSoup(response)
lsty=[]


"""obtaining all the pdf links from the navigated links by searching for 
specific tags and obtaining their content(names)
"""
for i in lst:
    q='https://'+i
    response = urllib.request.urlopen(q)
    soup = BeautifulSoup(response)
    linke = soup.find_all('a',href=True,text="PDF")
    for o in linke:
        lsty.append('https://arxiv.org'+o['href'])

"""creating a pdf in a local directory and saving the contents of the online
pdf into the file and saving it"""
for i in range(len(lsty)):
    url=lsty[i]
    nm=lsty[i].split('/')
    os.chdir("D:\Webc")
    import requests
    pdf = requests.get(url)
    with open('D:\Webc\\'+nm[4]+'.pdf', 'wb') as f:  
        f.write(pdf.content)
