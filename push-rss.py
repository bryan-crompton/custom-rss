import datetime
from rfeed import *
import feedparser
import random
import os

num = random.randint(0, 1000000)

f = open("/home/bryan/tidy/myweb/bookmarks/article-html/d00148e4314a87df.html.art.html")
description = f.read()
f.close()

# year, month, date, hh, mm, ss
item1 = Item(
        title = "Mighty have the fallen",
        link = f"https://www.{num}.com",
        description = description,
        author = "Vivek Gite",
        guid = Guid(f"https://www.{num}.com"),
        pubDate = datetime.datetime.now())
        
dfmt = "%a, %d %b %Y %H:%M:%S %Z" 
 
stuff = feedparser.parse("test-feed.xml")

LEN = 3

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
items.reverse()

print([item.pubDate for item in items])    

if len(items) > LEN:
    items = items[:LEN]


feed = Feed(
        title = "My Reading List",
        link = "https://raw.githubusercontent.com/bryan-crompton/custom-rss/main/test-feed.xml",
        description = "My personal reading list feed created from bookmarks",
        language = "en-US",
        lastBuildDate = datetime.datetime.now(),
        items = items)



f = open("test-feed.xml",'w')
f.write(feed.rss() + "\n")

path = "/home/bryan/tidy/projects/custom-rss"
