from __future__ import unicode_literals


import requests
import bs4

import pandas as pd

import os
import shutil
pathh=''#your path
try:
    shutil.rmtree(pathh)
except:
    pass
if not os.path.exists(pathh):
    os.makedirs(pathh)

realpath=os.path.realpath(pathh)+'/'

def fetcher():
    rest=requests.get("https://www.billboard.com/charts/hot-100")
    rest.raise_for_status()
    soup=bs4.BeautifulSoup(rest.content,'html.parser')
    
    west=soup.find_all(class_="chart-element__information__song text--truncate color--primary")
    east=soup.find_all(class_="chart-element__information__artist text--truncate color--secondary")
    songs=[items.text.lower() for items in west[0:10]]
    artists=[items.text.lower() for items in east[0:10]]
    yt="https://www.youtube.com/results?search_query="
    newlist=[]
    for i in range(len(songs)):
        newlist.append(yt+' '+artists[i]+songs[i])

    data=pd.DataFrame({'Top 10 songs this week':songs,'Top 10 Artists this week':artists})
    data2=data.to_string(index=False)
    filelist=open(realpath+'Top 10 songs.txt','w')
    filelist.write(data2)
    filelist.close()

    newlinks=[]

    for i in newlinks:
        print (i)


        

fetcher()
