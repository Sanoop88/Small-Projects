import sys
sys.path.append('/Users/videoqa/Documents/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages')
import praw
import time

#username=input('Username:- ')
#password=input('password:- ')
reddit=praw.Reddit(client_id='redditapiid',client_secret='redditapisecretkey',user_agent='testerAPI',username='yourusername',password='yourpassword')
subred=reddit.subreddit('showerthoughts')
hot=subred.hot(limit=7)
list1=[]
for i in hot:
  list1.append(str(i.title)+' '+str(i.url))
for i in list1[2:7]:
  print (i)