#coding=utf-8
'''
Created on 2015年7月19日

Site:  http://www.sugarguo.com/

@author: 'Sugarguo'
'''


def GetInfo():
    InfoList = []
    print "Get Info from config.dat\r\n"
    fileGetInfo = open('config.dat')
    for index,item in enumerate(fileGetInfo.readlines()):
        if index % 2 == 0:
            print str(index + 1).strip() + '\t' + item
        else:
            print item
            if(index > 12):
                f = file(item.strip())
                InfoList.append(f.read());
                f.close()
            else:
                InfoList.append(item);
    fileGetInfo.close()
    print "FIle read over!\r\n"
    print "Starting!.......\r\nLoading!.......\r\n"
    return InfoList
