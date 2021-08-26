import sys
sys.path.append('/Users/videoqa/Documents/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages')
import requests
from bs4 import BeautifulSoup

import re


def concerts():
	rest=requests.get('http://justshows.com/toronto/just-announced/')
	soup=BeautifulSoup(rest.content, features='html.parser')
	test=soup.find_all(href=re.compile('/toronto/2021'))
	list1=[x.get('title') for x in test][0:10]
	for i in list1:
		print (i)
concerts()




  