# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 19:59:51 2018

@author: yaoxinzhi
"""

#引入爬虫常用的包
#下面两个开源包一般需要自己安装
#打开Anaconda Prompt （或者终端） 输入命令
#sudo pip install urllib
#sudo pip install bs4

'''
所需要的库下载 
sudo pip install urllib.requests
sudo pip install bs4
sudo pip install urllib
sudo pip install requests
'''
import urllib.request         
from bs4 import BeautifulSoup

#编写获取每本书章节内容的函数
def get_chapter(url):
    # 获取网页的源代码
    html = urllib.request.urlopen(url)  
    content = html.read().decode('utf8')
    html.close()
    # 将网页源代码解析成HTML格式
    soup = BeautifulSoup(content, "lxml")
    title = soup.find('h1').text    #获取章节的标题
    text = soup.find('div', id='htmlContent')    #获取章节的内容
    #处理章节的内容，使得格式更加整洁、清晰
    content = text.get_text('\n','br/').replace('\n', '\n    ')
    content = content.replace('　　', '\n　　')
    return title, '    '+content

#编写爬虫运行的主程序（函数）
#小说所在的网站：http://jinyong.zuopinj.com
#打开网页看看小说分布的特点和对应页码

def main():
    books = ['射雕英雄传','天龙八部','鹿鼎记','神雕侠侣','笑傲江湖','碧血剑','倚天屠龙记','飞狐外传','书剑恩仇录','连城诀','侠客行','越女剑','鸳鸯刀','白马啸西风','雪山飞狐']
    order = [1,2,3,4,5,6,7,8,10,11,12,14,15,13,9]  #对应的书籍列表
    #网页上存储相应书籍的页码
    page_range = [1,43,94,145,185,225,248,289,309,329,341,362,363,364,375,385]

    for i,book in enumerate(books):
        for num in range(page_range[i],page_range[i+1]):
            url = "http://jinyong.zuopinj.com/%s/%s.html"%(order[i],num)
            try:
                title, chapter = get_chapter(url)
                #下面写入的是本人电脑对应文件夹地址，请手动修改
                with open('books/%s.txt'%book, 'a') as f:
                    print(book+':'+title+'-->写入成功！')
                    f.write(title+'\n\n\n')
                    f.write(chapter+'\n\n\n')
            except Exception as e:
                print(e) 
    print('全部写入完毕!')
main() #运行主程序函数

