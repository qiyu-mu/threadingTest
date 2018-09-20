#!/usr/bin/env python
#!-*-coding:utf-8-*-
#!@Time :9/20/18 11:32 AM
#!@Author   :qiyu
#!@File :.py


import requests
import threading
import time

total = 0   #总数
succ = 0    #成功数
fail = 0    #失败数
exc = 0     #异常数

class postRequest():
    def __init__(self, url, values, interface_name):
        self.url = url
        self.values = values
        self.interface_name = interface_name    #接口名

    def post(self):

        global total
        global succ
        global fail
        global exc

        parms = self.values
        try:
            resp = requests.post(url=self.url,data=parms)
            code = resp.status_code
            print(code)

            print(u"接口名字为：\n", self.interface_name)
            print (u"所传递的参数为：\n", parms)
            # print (u"服务器返回值为：\n", resp.text)
            print (u"resp对象的状态：\n", code)
            if code == '200':
                total += 1
                succ += 1
            else:
                total += 1
                fail += 1

        except Exception as e:
            print(exc)
            print (e)
            total += 1
            exc += 1


def start():  # 定义接口函数
    # 实例化接口对象
    login = postRequest('https://www.baidu.com', {"MSG": '1', "name": u"张三", "password": "123456"},
                        "1.login")
    return login.post()


try:
    i = 0
    tasks = []  # 任务列表
    task_number = 10
    while i < task_number:
        print(i)
        t = threading.Thread(target=start)
        t.start()  # 多线程并发
        time.sleep(2)
        i += 1
    print '===========task end==========='

    print "total:%d,succ:%d,fail:%d,except:%d"%(total,succ,fail,exc)

except Exception as e:
    print (e)

