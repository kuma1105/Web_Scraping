from bs4 import BeautifulSoup
from urllib.request import HTTPError
from urllib.request import urlopen

html = urlopen("http://www.pythonscraping.com/pages/page1.html")

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found')
else:
    print(title)

