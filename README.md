import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}

def GetSoup():
    Resp = requests.get(url,headers=headers)
    Resp.encoding = Resp.apparent-encoding
    Soup = BeautifulSoup(Resp.text,'html.parser')
    return Soup
Url = ''
Soup = GetSoup(Url)
