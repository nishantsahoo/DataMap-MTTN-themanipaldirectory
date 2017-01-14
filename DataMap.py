import urllib2
import sys
from bs4 import BeautifulSoup
sys.stdout = open('mttn_data_map.txt','w')
opener = urllib2.build_opener()
opener.add_headers=[('User-agent','Mozilla/5.0')]
url = "http://manipalthetalk.org/guides/the-manipal-directory"
ourUrl = opener.open(url).read()
soup = BeautifulSoup(ourUrl, 'html.parser')
print soup