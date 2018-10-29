import requests
import bs4
#import os
res =requests.get('https://aravinthvp.github.io')
type(res)
res.text()  # it is for page full source code


#Beautifulsoup
soup = bs4.BeautifulSoup(res.text,'lxml')
type(soup)

#it is for Specific needs
need = soup.select('title')
need


need [0].getText()
