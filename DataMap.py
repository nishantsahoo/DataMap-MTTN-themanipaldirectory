import urllib2
import sys
from bs4 import BeautifulSoup
sys.stdout = open('mttn_data_map.txt','w')
opener = urllib2.build_opener()
opener.add_headers=[('User-agent','Mozilla/5.0')]
url = "http://manipalthetalk.org/guides/the-manipal-directory"
ourUrl = opener.open(url).read()
soup = BeautifulSoup(ourUrl, 'html.parser')
print soup.find('h1', attrs={'class':'post-title entry-title'}).text
mDirectory = soup.find('div', attrs={'id':'mdirectory'})
table_list = mDirectory.findAll('table')
i = 1
for each in table_list:
    thead = each.find('thead').text.encode('utf-8').decode('ascii', 'ignore')
    print str(i) + '. ' + thead,
    tbody = each.findChildren('tbody')
    for each in tbody:
        print each.text.encode('utf-8').decode('ascii', 'ignore')
    i += 1