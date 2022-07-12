#!/usr/bin/env python
# -*- coding:utf-8 -*-

#批量列出归档文件中的归档内容

from cgitb import html
import os
import time
import zipfile
import rarfile

def list_file(dir):
    newdir = dir
    obname = os.path.basename(dir)
    # 获取不含路径的文件名
    if os.path.isfile(dir):
        obtype = dir.split('.')[-1]
        # 获取文件后缀以便于判断文件类型格式
        if(obtype in ["ZIP", "zip"]):
            # 如果是指定类型
            try:
                printhtml("<details><summary>🍎"+obname+"</summary><ul>")
                printlog("🍎🍎zip归档:"+dir)
                myfile = zipfile.ZipFile(dir, "r")
                list = myfile.infolist()
                for rec in list:
                    printhtml("<li style=\"list-style-type:none;\">📄文件:"+rec.filename+"</li>")
                    printlog("📄文件:"+rec.filename)
                myfile.close()
                printhtml("</ul></details>")
                printlog("🍏🍏zip归档文件已全部输出")
            except zipfile as e:
                printlog("处理zip时出现错误，请查看代码。")
        elif(obtype in ["RAR", "rar"]):
            try:
                printhtml("<details><summary>🍎"+obname+"</summary><ul>")
                printlog("🍎🍎rar归档:"+dir)
                myfile = rarfile.RarFile(dir)
                list = myfile.infolist()
                for rec in list:
                    printhtml("<li style=\"list-style-type:none;\">📄文件:"+rec.filename+"</li>")
                    printlog("📄文件:"+rec.filename)
                myfile.close()
                printhtml("</ul></details>")
                printlog("🍏🍏rar归档文件已全部输出")
            except Exception as e:
                printlog("处理rar时出现错误，请查看代码。")
        else:
            printhtml("📄"+obname+"<br>")
            printlog("📄文件:"+dir)
    elif os.path.isdir(dir):
        printhtml("<details><summary>📁"+obname+"</summary><ul>")
        for s in os.listdir(dir):
            newdir = os.path.join(dir, s)
            list_file(newdir)
        printhtml("</ul></details>")

def printlog(strlog):
    #输出到日志文件函数
    #设置文件名
    scan_log="文件列表.txt"
    #打开文件
    fplog = open(scan_log, "a",encoding="utf-8")
    #写入内容
    fplog.write(os.linesep+strlog)
    #关闭函数
    fplog.close()
    #同时输出到终端
    print(strlog)

def printhtml(strhtml):
    #输出到html文件函数
    #设置文件名
    scan_html="文件列表.html"
    #打开文件
    fphtml = open(scan_html, "a",encoding="utf-8")
    #写入内容
    fphtml.write(strhtml)
    #关闭函数
    fphtml.close()



if __name__ == '__main__':

    printhtml("开始执行时间:"+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    printlog("\n\n开始执行时间:"+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+"\n\n")
    list_file(r'./')
    printhtml("结束执行时间:"+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+"<hr>")
    printlog("\n\n结束执行时间:"+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+"\n\n")