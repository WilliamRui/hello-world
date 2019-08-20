'''
V01  20190820  Initial Version 
'''
####################################################################################################################
from bs4 import BeautifulSoup
import requests

def GetSoup(url):
#因程序中多出用到BeautifulSoup，为避免重复使用，此处直接定义函数获取Soup
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}
    Resp = requests.get(url,headers = headers)
    Resp.encoding = Resp.apparent_encoding
    #定义get到的网页信息的编码方式为网页html中的编码方式
    Soup = BeautifulSoup(Resp.text,"lxml")
    return Soup
    
def GetBookInfo():
#让用户输入小说名称，以一定格式返回搜索结果
#让用户根据显示的搜索结果选择小说对应的编号，然后函数反馈用户选择小说的地址
    SearchName = input('请输入小说名：')
    SearchUrl = 'https://www.xbiquge6.com/search.php?keyword=' + SearchName
    #拼凑搜索地址
    Soup = GetSoup(SearchUrl)
    Books = Soup.findAll('div',class_='result-item result-game-item')
    print('{1:{0}<3}\t{2:{0}<8}\t{3:{0}<8}\t{4}'.format(chr(12288),'序号','书名','作者','链接'))
    i=1
    for Book in Books:
        BookName = Book.find('a',cpos='title').get('title')
        BookLink = Book.find('a',cpos='title').get('href')
        Author = Book.find('p',class_='result-game-item-info-tag').findAll('span')[1].get_text().strip()
        print('{1:{0}<3}\t{2:{0}<8}\t{3:{0}<8}\t{4}'.format(chr(12288),i,BookName,str(Author),BookLink))
        i = i + 1
    BookID = int(input('请输入目标小说ID：'))
    if BookID>0 and BookID<11:
    #防止用户输入的小说编号不符合要求
        return Books[BookID-1].find('a',cpos='title').get('title').strip(),Books[BookID-1].find('a',cpos='title').get('href')
    else:
        print('小说序号输入有误，请重新输入！')

def GetChapterLinks(url):
#获取小说的章节链接
    ChapterLinks = []
    Soup = GetSoup(url)
    DDs = Soup.find('div',id='list').find('dl').findAll('dd')
    for DD in DDs:
        ChapterLinks.append('https://www.xbiquge6.com' + DD.find('a').get('href'))
    return ChapterLinks
    
def GetContent(url):
#获取小说章节正文
    Soup = GetSoup(url)
    Content = Soup.find('div',class_='bookname').find('h1').get_text() + '\n' + Soup.find('div',id='content').get_text().replace('\u00A0\u00A0\u00A0\u00A0','\n    ')
    #将取到的章节名和正文结合作为一章
    #获取的正文没有段落换行，但是首行缩进还是识别了，这里我们将首行缩进替换为换行加四个空格，变相实现段落换行
    return Content

BookName,BookUrl = GetBookInfo()
ChapterLinks = GetChapterLinks(BookUrl)
with open(BookName+'.txt','a',encoding='utf-8')as T:
#以小说名保存小说内容，编码方式为utf-8，此处默认是GBK，编码方式必须要修改
    for ChapterLink in ChapterLinks:
    #按章节保存小说
        T.write(GetContent(ChapterLink))
        T.write('\n\n')
        #在两个章节直接预留换行，更加美观。

    
