from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj
    except AttributeError as e:
        return None
    return title


title = getTitle("https://www.soumu.go.jp/senkyo/senkyo_s/data/chiji/index.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
