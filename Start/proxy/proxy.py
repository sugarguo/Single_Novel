#coding=utf-8
'''
Created on 2015年9月27日

@FileName: ../Proxy/Proxy.py

@Description: (获取代理列表并验证保存) 

@Site:  http://www.sugarguo.com/

@author: 'Sugarguo'

@version V1.0.0
'''

import urllib2
import time,re
import socket
from bs4 import BeautifulSoup
from time import sleep

listGetProxy = []
listJudgeProxy = []
Jf_proxy = open("proxy.txt",'w')

def GetProxy(url):
    # get the proxy
    #Ff_proxy = open('proxy.txt', 'w')
    user_agent = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
    request = urllib2.Request(url)
    request.add_header("User-Agent", user_agent)
    content = urllib2.urlopen(request)
    soup = BeautifulSoup(content)
    trs = soup.find('table', {"id":"ip_list"}).findAll('tr')
    for tr in trs[1:]:
        tds = tr.findAll('td')
        ip = tds[2].text.strip()
        port = tds[3].text.strip()
        protocol = tds[6].text.strip()
        if protocol == 'HTTP' or protocol == 'HTTPS':
            sproxy = '%s://%s:%s\n' % (protocol.lower(), ip, port)
            getSProxy(protocol.lower(),sproxy)
            listGetProxy.append('%s://%s:%s\n' % (protocol.lower(), ip, port))
            #of.write('%s://%s:%s\n' % (protocol.lower(), ip, port))
            #print '%s://%s:%s' % (protocol.lower(), ip, port)
    return listGetProxy


def getSProxy(protocol,sproxy):
    try:
        start = time.clock()
        proxy = {protocol:sproxy}
        print proxy
        proxy_support = urllib2.ProxyHandler(proxy)
        opener = urllib2.build_opener(proxy_support)
        urllib2.install_opener(opener)
        #添加头信息，模仿浏览器抓取网页，对付返回403禁止访问的问题
        i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
        socket.setdefaulttimeout(3)
        req = urllib2.Request('http://www.ip.cn/',headers=i_headers)
        html = urllib2.urlopen(req)
        html = html.read()
        J_soup = BeautifulSoup(html)
        print 'get'
        if html.strip()!='':
            end = time.clock()
            print "read: %f s" % (end - start)
            #print J_soup.find_all('div',class_="well")[0]
            print BeautifulSoup(str(J_soup.find_all('div',class_="well")[0])).p.get_text()
            print '\n'
            listJudgeProxy.append(sproxy)
            Jf_proxy.write(sproxy)

    except:
        print "pass"
        return False



for page in range(1,50):
    url = 'http://www.xicidaili.com/nn/%s' %page
    list = GetProxy(url)
    #print listJudgeProxy
    #print list[len(list)-1]
    #print len(list)

Jf_proxy.close()

