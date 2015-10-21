#coding=utf-8
'''
Created on 2015年7月19日

Site:  http://www.sugarguo.com/

@author: 'Sugarguo'
'''

import socket
import urllib2
import urllib
import time
import re
import os

rawProxyList = []
checkedProxyList = []
f= open("../proxy_list.txt",'a')


target = "http://www.xici.net.co/nn"
print target + '\n'

#targets = []
#for i in xrange(0,9):
#        target = r"http://www.xici.net.co/nn"# /%d" % i
#        targets.append(target)
#print targets + "\r\n"
#print targets[1] + "\n"


def getHtml(url):
    i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
    req = urllib2.Request(url,headers=i_headers)
    page = urllib2.urlopen(req)
    #page = urllib.urlopen(url)
    #print page.geturl()
    html = page.read()
    return html

def getProxy(html):
    regip = r"<td>(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})</td>"
    regport = r"<td>(\d{1,5})</td>"
    #此处为正则表达式，用于匹配页面中的图片链接，不同的网页图片链接的格式有所不用，此处需按需调整
    dailiip = re.compile(regip)
    daililistip = re.findall(dailiip,html)
    dailiport = re.compile(regport)
    daililistport = re.findall(dailiport,html)
    x = 0
    
    for dailiurl in daililistip:
        ip = dailiurl
        port = daililistport[x]
        proxy = [ip,port]
        rawProxyList.append(proxy)
        print str(x + 1) + " " + dailiurl + " " + port
        x+=1


def checkProxy(ip,port):
    try:        
        proxy = {'http':'http://' + ip + ':' + port}
        print proxy
        proxy_support = urllib2.ProxyHandler(proxy)
        opener = urllib2.build_opener(proxy_support)
        urllib2.install_opener(opener)
        #添加头信息，模仿浏览器抓取网页，对付返回403禁止访问的问题
        i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
        starttime = time.clock()
        socket.setdefaulttimeout(3)
        req = urllib2.Request('http://www.ip.cn/',headers=i_headers)
        html = urllib2.urlopen(req)
        html = html.read()
        print 'get'
        if html.strip()!='':
            endtime = time.clock()
            usetime = endtime - starttime
            print "read: %f s" % usetime
            proxy = [ip,port]
            checkedProxyList.append(proxy)
            f= open("../proxy_list.txt",'a')
            f.write("%s:%s\n"%(ip,port))
            f.close()
        regs = r'<div id="result"><div class="well"><p>当前 IP：<code>([\s\S]*?)</p><p>'
        namel = re.compile(regs)
        name = re.search(namel,html)
        print name.group().replace('<div id="result"><div class="well"><p>','').replace('</code>&nbsp;',' , ').replace('</p><p>',' ; ').replace('<code>','')
        #f= open("proxy_list.txt",'a')
        #site = name.group().replace('<div id="result"><div class="well"><p>','').replace('</code>&nbsp;',' , ').replace('</p><p>',' ; ').replace('<code>','')
        #f.write("%s\r\n"%site)
        #f.close()
        
    except Exception,e:
        print e.message

def tryget():
        html = getHtml(target)
        getProxy(html)
        print "ok\n"
        n = 1
        for proxy in rawProxyList:
                print str(n)
                checkProxy(proxy[0],proxy[1])
                n = n + 1
        print "ok\n"
        f = file('../proxy_list.txt','a')
        for item in checkedProxyList:
            f.write('\n' + item)
        f.close()

tryget()