#coding=utf-8
'''
Created on 2015年7月19日

Site:  http://www.sugarguo.com/

@author: 'Sugarguo'
'''

import socket
import urllib
import urllib2
import time
import re
import os

url = 'http://www.ip.cn/'

def getSProxy(sproxy):
    try:
        start = time.clock()
        proxy = {'http':'http://' + sproxy}
        print proxy
        proxy_support = urllib2.ProxyHandler(proxy)
        opener = urllib2.build_opener(proxy_support)
        urllib2.install_opener(opener)
        #添加头信息，模仿浏览器抓取网页，对付返回403禁止访问的问题
        i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
        socket.setdefaulttimeout(3)
        req = urllib2.Request(url,headers=i_headers)
        html = urllib2.urlopen(req)
        html = html.read()
        print 'get'
        if html.strip()!='':
            end = time.clock()
            print "read: %f s" % (end - start)
            #print html + '\r\n\r\n'
            regs = r'<div id="result"><div class="well"><p>当前 IP：<code>([\s\S]*?)</p><p>'
            namel = re.compile(regs)
            name = re.search(namel,html)
            print name.group().replace('<div id="result"><div class="well"><p>','').replace('</code>&nbsp;',' , ').replace('</p><p>',' ; ').replace('<code>','')
            print '\n'
            if name != '':
                return  True
            else:
                return False
    except:
        print "pass"
        return False

