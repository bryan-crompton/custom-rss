import datetime
from rfeed import *
import feedparser
import random
import os

num = random.randint(0, 1000000)

# year, month, date, hh, mm, ss
item1 = Item(
        title = "My 10 UNIX Command Line Mistakes",
        link = "https://www.{num}.com",
        description = f"{num}",
        author = "Vivek Gite",
        guid = Guid("https://www.{num}.com"),
        pubDate = datetime.datetime.now())
        
dfmt = "%a, %d %b %Y %H:%M:%S %Z" 
 
stuff = feedparser.parse("my-reading-list.xml")

LEN = 5

items = [item1]

for entry in stuff.entries:

    link = entry['link']
    description = entry['description']
    title = entry['title']
    guid = Guid(link)
    date = datetime.datetime.strptime(entry['published'], dfmt)

    item = Item(title=title, link=link, description=description, guid=guid,  pubDate=date)
    items.append(item)

items.sort(key = lambda x: x.pubDate)

print([item.pubDate for item in items])    

if len(items) > LEN:
    items = items[-LEN:]


feed = Feed(
        title = "My Reading List",
        link = "https://raw.githubusercontent.com/bryan-crompton/custom-rss/main/my-reading-list.xml",
        description = "My personal reading list feed created from bookmarks",
        language = "en-US",
        lastBuildDate = datetime.datetime.now(),
        items = items)



f = open("my-reading-list.xml",'w')
f.write(feed.rss())

os.system("git add .")
os.system("git commit -m 'update'")
os.system("git push")
