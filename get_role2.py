# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 19:59:51 2018

@author: yaoxinzhi
"""

'''
所需要的库下载
sudo pip install requests
sudo pip install bs4
'''

import requests
from bs4 import BeautifulSoup

#获得金庸所有角色名的网址
url = 'http://www.jinyongwang.com/data/renwu/'

#利用requests库解析网址
def get_HTML(url):
    r = requests.get(url)
    return r.content
    
#利用bs4库解析网址的源代码
def parse_HTML(html):
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.body
    main = body.find('div',attrs={'class':'main'})
    booklist = main.find('div',attrs={'class':'booklist'})

#将爬取结果写入文件
    with open('role/role.txt', 'w') as f:
        for datapice in booklist.find_all('div',attrs={'class':'datapice'}):
            for a in datapice.find_all('a'):
                f.write(a.get_text().replace(' ','')+'\n')
            
            
            
html = get_HTML(url);
print('Done')
