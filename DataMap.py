import urllib2
import sys
from bs4 import BeautifulSoup
sys.stdout = open('mttn_data_map.txt','w')
opener = urllib2.build_opener()
opener.add_headers=[('User-agent','Mozilla/5.0')]
url = "http://manipalthetalk.org/guides/the-manipal-directory"
ourUrl = opener.open(url).read()
soup = BeautifulSoup(ourUrl, 'html.parser')
title = soup.find('h1', attrs={'class':'post-title entry-title'}).text
print title
TDlist = soup.findAll('td')
i = 0
for each in TDlist:
    if i % 2 == 0:
        print each.text.encode('utf-8').decode('ascii', 'ignore') + ':',
    else:
        print each.text.encode('utf-8').decode('ascii', 'ignore')
        print
    i += 1
