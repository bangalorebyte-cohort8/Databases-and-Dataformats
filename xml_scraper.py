import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as xml
import csv

base_url = 'http://planetpython.org/rss20.xml'

rows = []
cells = []

target_url = (base_url)
r = requests.get(target_url)
content = r.content

with open('xml_scraper.xml', 'w') as xmlfile:
    xmlfile.write(content.decode()) #decode() necessary cuz content in bytes format

tree = xml.parse('xml_scraper.xml')
root = tree.getroot()
#print(root)
#print(root.tag)
#print(root.getchildren())

channel = root.find('channel')
#print(channel)
#links = channel.findall('link')
#print(links)

items = channel.findall('item')
#print(len(items))

for x in range(0, len(items)):
    print(items[x].findtext('title'))
    print(items[x].findtext('link'))
    print(items[x].findtext('pubDate'))
