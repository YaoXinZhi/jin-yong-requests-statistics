# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 20:23:40 2018

@author: yaoxinzhi
"""

import jieba 
import re
import os

#读取已经爬取的金庸所有小说文章目录
book_list = os.listdir('books')
#print (book_list)

# 读取已经爬取的金庸所有小说中的角色名称
role_list = []
with open('role/role.txt') as f:
    for line in f:
        l = re.sub(u"([^\u4e00-\u9fa5])","",line)
        role_list.append(l)
        
#利用结巴分词将小说分词
#print (role_list)

for book in book_list:
    with open('books/{0}'.format(book)) as f:
        doc = f.read()
        result = []
        seg_list = jieba.cut(doc, cut_all=True)
        seg_word = ' '.join(seg_list)
        seg_word = seg_word.split()
        for role in role_list:
            count = 0
# 分别计算每本小说中每个角色名字出现的次数
            for word in seg_word:
                if role == word:
                    count += 1
            if count != 0:
                result.append((role, count))
                
# 将统计结果进行排序，将出现次数排名前5的角色写入结果
        result_sort = sorted(result, key = lambda x: x[1], reverse=True)
        with open('count/{0}_count.txt'.format(book[:-4]), 'w') as wf:
            for k in result_sort[:5]:
                wf.write('{0}\t{1}\n'.format(k[0], k[1]))
print ('Done')