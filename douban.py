import requests
from bs4 import BeautifulSoup
import time
word="金庸"
for i in range(0,5,1):
    url="https://www.douban.com/j/search?q="+word+"&start="+str(20*i)+"&cat=1001"
    r=requests.get(url)
    if(r.status_code==200):
        r.encoding='UTF-8'
        soup=BeautifulSoup(r.text,"lxml")
        s=[]
    for a in soup.find_all('a'):
        s.append(a['href'].replace('\\',''))
    s1=list(set(s))
    s1.sort(key=s.index)
    for ss in s1:
        res=requests.get(ss.replace('\"',''))
        if(res.status_code==200):
            soup1=BeautifulSoup(res.text,'lxml')
            a=soup1.find('h1')
            b=soup1.find(href="https://book.douban.com/author/4508301/")
            c=soup1.find('div',class_='intro')
        if(a):
            print("书名：",a.text.replace('\n',''))
        if(b):
            print("作者：",b.text.replace('\n''            ',''))
        if(c):
            print("内容：",c.text.replace('\n',''),"\n")
    time.sleep(2)
    
