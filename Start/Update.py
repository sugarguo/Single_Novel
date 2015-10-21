#coding=utf-8
'''
Created on 2015年7月19日

Site:  http://www.sugarguo.com/

@author: 'Sugarguo'
'''

import os
import time
import random
import threading
from time import ctime,sleep
from __builtin__ import str, file

import sys

sys.path.append("..")
import GetInfo.GetConfig
import GetInfo.GetHtmlPage
import GetInfo.GetUrlChapterArticle
import GetInfo.JudgeProxy
import GetInfo.GetFileInfoCreateXml


class ThreadRun(threading.Thread):
    def __init__(self,listUrl,listChapter,listindex,UseListProxy):
        threading.Thread.__init__(self)
        self.listurls = listUrl
        self.listchapters = listChapter
        self.listindexs = listindex
        self.listproxys = UseListProxy
    def run(self):
        for index,item in enumerate(self.listurls):
            slice = random.randint(0, len(self.listproxys) - 1)
            Write_Act(item.strip(),self.listchapters[index].strip(),self.listindexs[index],self.listproxys[slice])


def Write_ActText(index,chapter,astring):
    try:
        flistwrite = open('../' + APath + '/' + AcTitle + '_10000_' + str(index) + '.txt','w')
        astring = '\r\n' + str(index) + ' —— ' + chapter + ' \r\n' + astring.replace('&nbsp;','').replace('<br />','') + '\r\n'
        flistwrite.write(astring);
        flistwrite.close()
        print str(index) + ' ' + chapter + ' txt is ok \n'
    except:
        print "Write pass"
        return False

def Write_Act(url,chapter,index,useProxy):
    try:
        flistwrite = open('../' + AcTitle + '/' + AcTitle + '_10000_' + str(index) + '.html','w')
        turl = str(url).strip()
        astring = Get_model_1+ '<meta name="keywords" content="' + chapter.strip() + '大主宰,大主宰最新章节列表,大主宰无弹窗广告全文阅读,大主宰txt全集下载,大主宰epub全集下载" />\r\n    <meta name="description" content="小说大主宰是作者天蚕土豆写的一部玄幻魔法小说,大主宰party第一时间为party友提供大主宰最新章节列表,大主宰txt全集下载,大主宰无弹窗广告全文阅读,最新阅读观看体验尽在大主宰party。" />\r\n\t\t<title>' +chapter + '——' + WTItle + Get_act_1
        html = GetInfo.GetHtmlPage.getHtml(turl,useProxy)
        Write_ActText(index,chapter,html)
        string = GetInfo.GetUrlChapterArticle.getArticle(html).strip()#.replace('&nbsp;','').replace('<br />','').strip()
        footstring = '<div class="alert alert-block alert-info" ><p class="text-center">'
        if index == 0 :
            astring += '../list.html' + Get_act_2
            footstring +='<a href="../list.html" >上一章</a>'
        else:
            astring +=  'dzz_10000_' + str(index -1) + '.html' + Get_act_2
            footstring +='<a href="' + 'dzz_10000_' + str(index -1) + '.html' + '">上一章</a>'
        footstring += ' | <a href="../list.html">回到目录</a> | '
        if index == len(ListUrls):
            astring += '../list.html' + Get_act_3
            footstring +='<a href="../list.html">下一章</a></div>'
        else:
            astring += 'dzz_10000_' + str(index + 1) + '.html' + Get_act_3
            footstring +='<a href="' + 'dzz_10000_' + str(index + 1) + '.html' + '">下一章</a></p></div>'
        
        astring += chapter + Get_act_4 + '<h1>' + chapter + WTItle + '</h1>\t\t\t\t\t\r\n<br />\t\t\t\t\t\t<h4>' + string + '</h4>\r\n\t\t\t\t\t<br />\r\n' + footstring + Get_model_2

        flistwrite.write(astring);
        flistwrite.close()
        astring  = ''
        footstring = ''
        data = open('../' + AcTitle + '/' + AcTitle + '_10000_' + str(index) + '.html').read()
        if len(data) == 0:
            print "\n****************************\nwrite error null\n****************************\n"
            return
        print str(index) + ' ' + chapter + ' is ok \n'
    except:
        print "Write pass"
        return False

def CreateList(listchapters):
    flist = open('../list.html','w')
    pstring = Get_list_1+ WTItle + Get_list_2
    i = 0
    for index,chapter in enumerate(listchapters):
        furl = AcTitle + '/' + AcTitle + '_10000_' + str(index) + '.html'
        if(i == 0):
            pstring += '\n\t\t\t\t<tr><td class="success"><a href="' + furl.strip() + '">' + chapter.strip() + '</a></td>\r\n'
            i = i + 1
        elif(i == 1):
            pstring += '\t\t\t\t<td class="warning"><a href="' + furl.strip() + '">' + chapter.strip() + '</a></td>\r\n'
            i = i + 1
        elif(i == 2):
            pstring += '\t\t\t\t<td class="danger"><a href="' + furl.strip() + '">' + chapter.strip() + '</a></td>\r\n'
            i = i + 1
        else:
            pstring += '\t\t\t\t<td class="info"><a href="' + furl.strip() + '">' + chapter.strip() + '</a></td></tr>\r\n\r\n\t\t\t'
            i = 0    
    pstring += Get_list_3
    flist.write(pstring)
    flist.close()
    print 'list.html 生成ok'

    
def MkdirF(name):
    try:
        if os.path.exists(name):
                print(name + '文件已存在')
        else:
            os.mkdir(name)
            print(name + '文件夹以创建')
    except ZeroDivisionError:
        print(name + '文件已存在，请删除后继续~')


def getIndex():
    for index,item in enumerate(os.listdir('../' + AcTitle)):
        sindex = item.replace('.html','').replace('_','').replace('dzz','').replace('10000','')
        data = open('../' + AcTitle + '/'  + item).read()
        if len(data) == 0:
            ListGet.append(sindex)
        haveone =  sindex
        listHave.append(str(haveone))
    return listHave

def Update():
    listHave = getIndex()
    html = GetInfo.GetHtmlPage.getHtml(Gurl,UseListProxy[0].strip())
    GetInfo.GetHtmlPage.getPage(Gurl, AllPath, html)
    ListUrls = []
    ListChapters = []
    
    ListUrls = GetInfo.GetUrlChapterArticle.getUrl(AllPath, UrlPath)
    ListChapters = GetInfo.GetUrlChapterArticle.getChapter(AllPath, ChapterPath)
    CreateList(ListChapters)
    for index,item in enumerate(ListUrls):
        if str(index).strip() not in listHave:
            ListGet.append(index)
    return ListGet
        
def TryThreads(ListGet):
    threads = []
    i = 0
    listGetUrl = []
    listGetChapter = []
    listGetIndex = []
    for index,item in enumerate(ListGet):
        item = int(item)
        if index % 30 == 0:
            if index == 0:
                listGetUrl.append(ListUrls[item])
                listGetChapter.append(ListChapters[item])
                listGetIndex.append(item)
            elif index == len(ListUrls) -1:
                listGetUrl.append(ListUrls[item])
                listGetChapter.append(ListChapters[item])
                listGetIndex.append(item)
                tread = ThreadRun(listGetUrl,listGetChapter,listGetIndex,UseListProxy)
                threads.append(tread)
            else:
                tread = ThreadRun(listGetUrl,listGetChapter,listGetIndex,UseListProxy)
                threads.append(tread)
                i = i + 1
                listGetUrl = []
                listGetChapter = []
                listGetIndex = []
                listGetUrl.append(ListUrls[item])
                listGetChapter.append(ListChapters[item])
                listGetIndex.append(item)
        else:
            if index == len(ListUrls) - 1:
                listGetUrl.append(ListUrls[item])
                listGetChapter.append(ListChapters[item])
                listGetIndex.append(item)
                tread = ThreadRun(listGetUrl,listGetChapter,listGetIndex,UseListProxy)
                threads.append(tread)
            else:
                listGetUrl.append(ListUrls[item])
                listGetChapter.append(ListChapters[item])
                listGetIndex.append(item)
                
    try:
        for t in threads:
            t.setDaemon(True)
            t.start()
        for t in threads:
            t.join()
            print "update all over %s\n" %ctime()
    except:
        print "treads pass"
        return False


print "/************************单本小说爬虫  By:Sugarguo************************/"
InfoList = GetInfo.GetConfig.GetInfo()
WTItle = InfoList[0].strip()
Gurl = InfoList[1].strip()
Turl = InfoList[2].strip()
APath = InfoList[3].strip()
UrlPath = '../' + APath + '/' + APath + InfoList[4].strip()
ChapterPath = '../' + APath + '/' + APath + InfoList[5].strip()
Get_act_1 = InfoList[6].strip()
Get_act_2 = InfoList[7].strip()
Get_act_3 = InfoList[8].strip()
Get_act_4 = InfoList[9].strip()
Get_model_1 = InfoList[10].strip()
Get_model_2 = InfoList[11].strip()
Get_list_1 = InfoList[12].strip()
Get_list_2 = InfoList[13].strip()
Get_list_3 = InfoList[14].strip()
AllPath = '../' + APath + '/' + APath + '.dat'
AcTitle = APath.replace('txt','').strip()

print APath
print AllPath
print AcTitle
print UrlPath
print ChapterPath

MkdirF('../' + APath)
MkdirF('../' + AcTitle)

f= open("../proxy_list.txt",'r')
ListProxy = []
UseListProxy = []
for item in f.readlines():
    ListProxy.append(item)
    judge = GetInfo.JudgeProxy.getSProxy(item.strip())
    if judge:
        UseListProxy.append(item.strip())
    time.sleep(1)
f.close()

print "ok\n"
for item in UseListProxy:
    print item

html = GetInfo.GetHtmlPage.getHtml(Gurl,UseListProxy[0].strip())
GetInfo.GetHtmlPage.getPage(Gurl, AllPath, html)
ListUrls = []
ListChapters = []

ListUrls = GetInfo.GetUrlChapterArticle.getUrl(AllPath, UrlPath)
ListChapters = GetInfo.GetUrlChapterArticle.getChapter(AllPath, ChapterPath)
CreateList(ListChapters)

ListGet = []
listHave = []

GetInfo.GetFileInfoCreateXml.JudegeRun('../' + AcTitle)  
Update()

for item in ListGet:
    print str(item)
while 1:
    print '\n\nstart!\n' 
    if len(ListGet) == 0:
        GetInfo.GetFileInfoCreateXml.JudegeRun('../' + AcTitle) 
        print 'Every Is OK!\n'
        exit
    elif len(ListGet) <= 50:
        print "********************************************************\n"
        print '还有 ' + str(len(ListGet)) + ' 个未采集\n'
        print 'Len < 50'
        for item in ListGet:
            print str(item)
            item = int(item)
            print str(item) + ' ' + ListUrls[item].strip() + ' ' + ListChapters[item].strip() + ' \n'
            slice = random.randint(0, len(UseListProxy) - 1)
            Write_Act(ListUrls[item].strip(),ListChapters[item].strip(),item,UseListProxy[slice])
        ListGet = []
        ListGet = Update()
        GetInfo.GetFileInfoCreateXml.JudegeRun('../' + AcTitle) 
        print "========================================================\n"
    else:
        print "********************************************************\n"
        print "********************************************************\n"
        print "tread start\n"
        ListGet = []
        ListGet = Update()
        print '还有 ' + str(len(ListGet)) + ' 个未采集\n'
        time.sleep(10)
        #CreateRunTread(ListGet)
        TryThreads(ListGet)
        print "========================================================\n"
        print "========================================================\n"
