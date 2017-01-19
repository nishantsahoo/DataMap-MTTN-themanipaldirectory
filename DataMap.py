import urllib2
import sys
from bs4 import BeautifulSoup
sys.stdout = open('mttn_final_database.txt','w')
opener = urllib2.build_opener()
opener.add_headers=[('User-agent','Mozilla/5.0')]
url = "http://manipalthetalk.org/guides/the-manipal-directory"
ourUrl = opener.open(url).read()
soup = BeautifulSoup(ourUrl, 'html.parser')
# print soup.find('h1', attrs={'class':'post-title entry-title'}).text
# print
mDirectory = soup.find('div', attrs={'id':'mdirectory'})
table_list = mDirectory.findAll('table')
i = 1
k = 0
for each in table_list:
    thead = each.find('thead').text.encode('utf-8').decode('ascii', 'ignore')
    print str(i) + '. ' + thead
    tRows = each.findAll('tr')
    for tr in tRows:
        tdList = tr.findAll('td')
        for td in tdList:
            if td.text.encode('utf-8').decode('ascii', 'ignore'):
                if k %2 == 0:
                    print td.text.encode('utf-8').decode('ascii', 'ignore') + ':',
                else:
                    print td.text.encode('utf-8').decode('ascii', 'ignore')
                k += 1
            # print
    i += 1