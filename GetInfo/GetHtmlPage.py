#coding=utf-8
'''
Created on 2015年7月19日

Site:  http://www.sugarguo.com/

@author: 'Sugarguo'
'''

import re
import urllib2
import socket

def getHtmlWithoutProxy(url):
    try:
        i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
        req = urllib2.Request(url,headers=i_headers)
        #i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
        #req = urllib2.Request(url,headers=i_headers)
        page = urllib2.urlopen(req)
        #print page.geturl()
        html = page.read().decode('gbk').encode('utf-8')
        return html
    except:
        print "pass"
        return False

def getHtml(url,useProxy):
    try:
        proxy = {'http':'http://' + useProxy}
        proxy_support = urllib2.ProxyHandler(proxy)
        opener = urllib2.build_opener(proxy_support)
        urllib2.install_opener(opener)
        i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
        socket.setdefaulttimeout(3)
        req = urllib2.Request(url,headers=i_headers)
        page = urllib2.urlopen(req)
        html = page.read().decode('gbk').encode('utf-8')
        return html
    except:
        print "gethtml pass"
        return False

def getPage(Wurl,AllPath,html):
    reg_Page = r'<dd><a href="([\s\S]*?)">([\s\S]*?)</a></dd>'
    pattern_Page = re.compile(reg_Page,re.M)    
    result_Page = re.findall(pattern_Page,html)
    num = 0
    file = open(AllPath,'w')
    for i in result_Page:
        siteUrl = i
        for index,j in enumerate(siteUrl):
            #print j + str(index) + '\r\n'
            if(index % 2 != 0):
                file.write(j +'\n')
                num = num + 1
            else:
                wstring = Wurl + j
                #print wstring
                file.write(wstring +'\n')
                num = num + 1
    print 'Get Page\r\n'
    file.close()