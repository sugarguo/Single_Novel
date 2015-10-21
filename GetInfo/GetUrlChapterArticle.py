#coding=utf-8
'''
Created on 2015年7月19日

Site:  http://www.sugarguo.com/

@author: 'Sugarguo'
'''

import re

def getChapter(allpath,chapterpath):
    file = open(allpath,'r')
    listname = []
    ff = open(chapterpath,'w')
    for index,item in enumerate(file):
          if index % 2 != 0:
                listname.append(item + '\n')
                ff.write(str(item))
    #f.close()
    ff.close()
    print 'Get Chapter\r\n'
    return listname

def getUrl(allpath,urlpath):
    file = open(allpath,'r')
    listurl = []
    f = open(urlpath,'w')
    for index,item in enumerate(file):
          if index % 2 == 0:
                listurl.append(item + '\n')
                f.write(str(item))
    f.close()
    print 'Get Url\r\n'
    return listurl

def getArticle(html):
    reg_Article = r'<div id="content">([\s\S]*?)</div>'
    pattern_Article = re.compile(reg_Article)  
    result_Article = re.search(pattern_Article,html)
    #print result_Article.groups(0)
    Article = result_Article.group(1)
    print 'Get Article\r\n'
    return str(Article)
