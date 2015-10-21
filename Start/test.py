#coding=utf-8
'''
Created on 2015年7月21日

Site:  http://www.sugarguo.com/

@author: 'Sugarguo'
'''


import os

listGet = []

for index,item in enumerate(os.listdir('../dzz')):
    slen = os.path.getsize('../dzz/' + item)
    if slen == 0:
        listGet.append(item.replace('.html','').replace('_','').replace('dzz','').replace('10000',''))
AcTitle = 'dzz'
filepath = '../dzz/dzz_10000_0.html'
f = file(filepath,'r')
data = len(f.read())
print str(data)
slen = os.path.getsize('../dzz/dzz_10000_0.html')
print str(slen)

s = os.getcwd()
print s
