#!/usr/bin/env python
#!-*-coding:utf-8-*-
#!@Time :9/20/18 11:32 AM
#!@Author   :qiyu
#!@File :.py


import requests
import threading
import time
import socket

total = 0   #总数
succ = 0    #成功数
fail = 0    #失败数
exc = 0     #异常数

class Tcpsend():
    def tcpsend(self, ip, port, xmlbw):

        global total
        global succ
        global fail
        global exc

        try:
            address = (ip, port)
            client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            resp = client.connect(address)
            print(resp)
            # by = xmlbw.encode('utf8')   #转为字节数组
            # print by
            # client.send(by)
            resp1 = client.sendall(xmlbw)
            print(resp1)
            print "发送成功"
            try:
                data = client.recv(1024)      #接受响应信息
                print "接受响应成功"
                print data
                client.close()
                total += 1
                succ += 1
            except Exception as e:
                print(e)
                total += 1
                fail += 1
        except Exception as e:
            print(e)
            total += 1
            exc += 1


def start():  # 定义接口函数
    start = Tcpsend()
    with open("sockets.xml") as fp:
        xmlbw = fp.read()
    xmlbw = xmlbw.replace(' ','')
    print(xmlbw)
    start.tcpsend(ip='192.168.2.37', port=7022, xmlbw=xmlbw)


def main():
    try:
        i = 0
        tasks = []  # 任务列表
        task_number = 1
        while i < task_number:
            t = threading.Thread(target=start)
            t.start()  # 多线程并发
            time.sleep(2)
            i += 1
        print '===========task end==========='

        # print "total:%d,succ:%d,fail:%d,except:%d"%(total,succ,fail,exc)
        print "total:%d,succ:%d,fail:%d,exc:%d"%(total,succ,fail,exc)

    except Exception as e:
        print (e)


if __name__ == "__main__":
    main()


