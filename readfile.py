#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: readfile.py
# @Time: 2018/2/12 11:36
# @Last Modified time: 2018/2/12 11:36
# @Explain: This file is for ...


def txtread(Fpath):
    txtpath=open(Fpath,"rb")
    #while True:
    for i in range(10000000000):
        data=txtpath.readline()
        yield data.decode("gbk",'ignore')
        if data==b'':
            txtpath.close()
            break
        if i ==10000000000-1:
            txtpath.close()
            yield ''

path1=r"E:\python\资料教程\千峰视频\day11\newchina.txt"
path2=r"E:\python\资料教程\千峰视频\day6\kaifangX.txt"
data=txtread(path2)
while True:
    readdata=next(data)
    if readdata=='':
        break
    if readdata.find("张三丰,")!=-1 :
        print(readdata, end='')




