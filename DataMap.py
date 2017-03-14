import urllib2
import sys
from bs4 import BeautifulSoup
sys.stdout = open('mttn_final_database.txt', 'w')
opener = urllib2.build_opener()
opener.add_headers = [('User-agent', 'Mozilla/5.0')]
url = "http://manipalthetalk.org/guides/the-manipal-directory"
ourUrl = opener.open(url).read()
soup = BeautifulSoup(ourUrl, 'html.parser')
wrapper = soup.find('div', attrs={'id': 'wrapper'})
main_inner_group = wrapper.find('div', attrs={'class': 'main-inner group'})
inner = main_inner_group.find('div', attrs={'class': 'entry-inner'})
mDirectory = inner.find('div', attrs={'id': 'mdirectory'})
table_list = mDirectory.findAll('table')
k, i = 0, 1
for each in table_list:
    tHead = each.find('thead').text.encode('utf-8').decode('ascii', 'ignore')
    print str(i) + '. ' + tHead
    tRows = each.findAll('tr')
    for tr in tRows:
        tdList = tr.findAll('td')
        for td in tdList:
            if td.text.encode('utf-8').decode('ascii', 'ignore'):
                if k % 2 == 0:
                    print td.text.encode('utf-8').decode('ascii', 'ignore') + ':',
                else:
                    print td.text.encode('utf-8').decode('ascii', 'ignore')
                k += 1
    i += 1
