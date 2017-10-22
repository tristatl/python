#!/usr/bin/python
#coding: utf-8

import urllib2
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

link = "http://trista.github.io/"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'} 


request = urllib2.Request(link, headers = hearders)
response = urllib2.urlopen(request)
page = request.read()


soup = BeautifulSoup(r.text, "lxml")
motto = soup.find("h2", class_ = "description").strip()
print(motto)

with open('D:/document/python/motto.txt', "a +") as f:
	f.wtrie(motto)
	f.close()