#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: readfile.py
# @Time: 2018/2/12 11:36
# @Last Modified time: 2018/2/12 11:36
# @Explain: This file is for ...


def txtread(Fpath):
    txtpath=open(Fpath,"rb")
    while True:
        data=txtpath.readline()
        yield data.decode("utf-8",'ignore')
        if data==b'':
            txtpath.close()
            break

path1=r"E:\python\资料教程\千峰视频\day11\newchina.txt"
path2=r"E:\python\资料教程\千峰视频\day6\kaifangX.txt"
data=txtread(path2)
while True:
    readdata=next(data)
    if readdata=='':
        break
    print(readdata,end='')





