#coding=utf-8
'''
Created on 2015年7月19日

Site:  http://www.sugarguo.com/

@author: 'Sugarguo'
'''

from xml.dom import minidom, Node
import os,datetime  


WUrl = 'http://dzz.party/dzz/'

listFileName = []
listFileTime = []

def getFileInfo(FindPath):
    filenames=os.listdir(FindPath) 
    for name in filenames:
        filePath = os.path.join(FindPath,name)
        fileName = os.path.basename(name)
        filetime = os.path.getmtime(filePath)
        listFileName.append(fileName)
        listFileTime.append(filetime)
    return listFileName

def JudegeRun(FindPath):
    getFileInfo(FindPath)
    sfile = file('../sitemap.xml','w')
    sstring = file('../xml.dat','r').read()
    for index,item in enumerate(listFileName):
        timestamp = listFileTime[index]
        date = datetime.datetime.fromtimestamp(timestamp)  
        stime =  date.strftime('%Y-%m-%d %H:%M:%S')  
        item = WUrl.strip() + item.strip()
        sstring += '\t<url>\n\t\t<loc>' + item + '</loc>\n\t\t<lastmod>' + stime
        sstring += '</lastmod>\n\t\t<changefreq>daily</changefreq>\n\t\t<priority>0.8</priority>\n\t</url>\n'
        sfile.write(sstring)
        sstring = ''

    sfile.write("</urlset>")
    sfile.close()
    print 'SiteMap is OK\n'