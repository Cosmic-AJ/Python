# The program will use urllib to read the HTML from the data files below,
# extract the href= values from the anchor tags, scan for a tag that
# is in a particular position relative to the first name in the list,
# follow that link and repeat the process a number of times and 
# report the last name you find
# http://py4e-data.dr-chuck.net/known_by_Travis.html

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
no = int(input('Enter count: '))
pos = int(input('Enter position: '))
print()
print('Retrieving:',url)
while no>0:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    c = 1
    for tag in tags:
        if(c==pos):
            print('Retrieving:',tag.get('href',None))
            url = tag.get('href',None)
            if(no-1 == 0):
                print()
                print("Final Name - " , end='')
                name = re.findall('.*/known_by_(.*).html',tag.get('href',None))
                print(name[0])
        c = c + 1
    no = no - 1                